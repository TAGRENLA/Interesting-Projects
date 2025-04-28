# ecoding:utf-8
# 作者：Tagrenla
# 声明：半成品项目，因作者技术有限，暂时搁置，如有大神尽管开发，标明出处即可！
# 禁止用于非法用途，如有后果自负，与作者无关！！！【特此郑重声明】
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import edge_tts
import asyncio
import threading
import os


class EdgeTTSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Edge TTS 朗读工具")

        # 初始化语音列表
        self.voices = []
        self.load_voices()

        # 创建界面
        self.create_widgets()

    def load_voices(self):
        """异步加载可用语音列表"""

        def _load():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                voices = loop.run_until_complete(edge_tts.list_voices())
                self.voices = [v['ShortName'] for v in voices if 'zh-' in v['ShortName']]
            finally:
                loop.close()

        threading.Thread(target=_load).start()

    def create_widgets(self):
        """创建界面组件"""
        # 语音选择
        ttk.Label(self.root, text="选择语音:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.voice_combo = ttk.Combobox(self.root, values=self.voices, state="readonly")
        self.voice_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.voice_combo.set("zh-CN-YunxiNeural")  # 设置默认语音

        # 参数调节
        ttk.Label(self.root, text="语速 (+/-%):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.rate_entry = ttk.Entry(self.root)
        self.rate_entry.insert(0, "+0%")
        self.rate_entry.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.root, text="音调 (+/-Hz):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.pitch_entry = ttk.Entry(self.root)
        self.pitch_entry.insert(0, "+0Hz")
        self.pitch_entry.grid(row=2, column=1, padx=5, pady=5)

        # 文本输入
        ttk.Label(self.root, text="输入文本:").grid(row=3, column=0, padx=5, pady=5, sticky="nw")
        self.text_input = tk.Text(self.root, height=10, width=40)
        self.text_input.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

        # 文件导入按钮
        self.import_btn = ttk.Button(self.root, text="导入 TXT 文件", command=self.import_txt)
        self.import_btn.grid(row=4, column=0, padx=5, pady=5)

        # 朗读按钮
        self.speak_btn = ttk.Button(self.root, text="开始朗读", command=self.start_tts)
        self.speak_btn.grid(row=4, column=1, padx=5, pady=5)

        # 使界面元素自适应窗口大小
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(3, weight=1)

    def import_txt(self):
        """导入 TXT 文件"""
        filepath = filedialog.askopenfilename(filetypes=[("文本文件", "*.txt")])
        if filepath:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.text_input.delete(1.0, tk.END)
                    self.text_input.insert(tk.END, f.read())
            except Exception as e:
                messagebox.showerror("错误", f"无法读取文件: {str(e)}")

    def start_tts(self):
        """启动 TTS 朗读"""
        text = self.text_input.get(1.0, tk.END).strip()
        if not text:
            messagebox.showwarning("警告", "请输入需要朗读的文本")
            return

        voice = self.voice_combo.get()
        rate = self.rate_entry.get()
        pitch = self.pitch_entry.get()

        # 在新线程中运行异步任务
        threading.Thread(target=self.run_tts, args=(text, voice, rate, pitch)).start()

    def run_tts(self, text, voice, rate, pitch):
        """执行 TTS 生成和播放"""

        async def _tts():
            try:
                communicate = edge_tts.Communicate(
                    text=text,
                    voice=voice,
                    rate=rate,
                    pitch=pitch
                )

                # 生成临时音频文件
                output_file = "temp_audio.mp3"
                await communicate.save(output_file)

                # 播放音频（需要系统有默认播放器）
                os.startfile(output_file)

            except Exception as e:
                messagebox.showerror("错误", f"生成语音失败: {str(e)}")

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(_tts())
        finally:
            loop.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = EdgeTTSApp(root)
    root.mainloop()
