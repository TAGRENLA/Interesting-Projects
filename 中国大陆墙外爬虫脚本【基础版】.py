
"""
主要进行的是chrome翻墙浏览器
需要提前下载chromeDriver程序
用户使用过程中主要更改main函数部分
作者微信：S64959
仅供个人娱乐使用，切勿用于违法途径！
如违反上述规定，使用者自行承担责任！
"""
# ecoding:utf-8

from selenium import webdriver
from selenium.common.exceptions import WebDriverException


def save_html_to_txt(file_name, html_content):
    """
    将 HTML 内容保存到指定的文本文件
    :param file_name: 文件名
    :param html_content: HTML 源码内容
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)
        print(f"HTML 源码已保存到文件: {file_name}\n")


def close_the_browser(driver):
    """
    提示用户是否关闭浏览器
    :param driver:初始化 Chrome 浏览器
    :return: None
    """
    close_browser = input("是否关闭浏览器？（是/否）: ").strip().lower()
    if close_browser in ['是', 'y', 'yes']:
        driver.quit()
        print("浏览器已关闭。")
    else:
        print("浏览器保持打开状态。")


def get_all_urls(driver):
    """
    获取当前的Google浏览器的所有的标签的的网址打印并返回
    :param driver: 初始化 Chrome 浏览器
    :return: 所有标签页的网址
    """
    # 获取所有标签页的句柄
    all_window_handles = driver.window_handles
    urls = []
    # 遍历所有标签页，打印每个标签页的网址
    for handle in all_window_handles:
        # 切换到该标签页
        driver.switch_to.window(handle)
        # 获取当前标签页的网址
        current_url = driver.current_url
        urls.append(current_url)
    print("==========所有网站集合已经生成==========")
    return urls

def open_browser():
    """
    初始化 Chrome 浏览器
    :return: driver
    """
    # 设置 Chrome 浏览器选项
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36")
    # 初始化 Chrome 浏览器
    driver = webdriver.Chrome(options=options)
    return driver


def open_one_urls(driver):
    """
    打开单个的网站
    :param driver: 初始化 Chrome 浏览器
    :return:
    """
    driver.get(input("请输入网址（如：https://chatgpt.com/）："))


def open_all_urls(driver,urls = []):
    """
    打开所有的网站
    :param driver: 初始化 的Chrome 浏览器
    :param urls: 预计爬取的所有网站的网址
    :return:
    """
    for url in urls:
        driver.execute_script(f"window.open('{url}');")



def get_html_from_one_tabs(driver, url=None):
    """
    提取单个网址的源码
    :param driver: 浏览器驱动
    :param url: 要提取源码的网址（如果为 None，则提取当前标签页的源码）
    :return: html_page
    """
    if url:
        # 导航到目标网址
        driver.get(url)
    # 获取当前页面源码
    html_page = driver.page_source
    return html_page



def get_html_from_all_tabs(driver):
    """
    提取所有标签页的网址及其源码【一般的代码中不用】
    :param driver: 浏览器驱动
    :return: 包含网址和源码的列表
    """
    print('正在提取所有的网站源码【get_html_from_all_tabs方法】！！！')
    all_window_handles = driver.window_handles
    html_pages = []

    for handle in all_window_handles:
        driver.switch_to.window(handle)
        current_url = driver.current_url
        html_page = driver.page_source
        html_pages.append((current_url, html_page))
        print(f"已提取【全部网址源代码】：{current_url}")
    return html_pages


def main(driver):
    """
    主要更改这部分内容
    """
    while True:
        do = int(input("""=====请选择相关的操作【直接输入数字即可】=====：
        1.打开单一网址
        2.打开多级网址
        3.提取网址的所有源码并保存为TXT文件
        0.关闭浏览器，结束程序!
----------------------------------------请输入>>>"""))
        if do == 1:
            open_one_urls(driver=driver)
        elif do == 2:
            file_path = input("请输入TXT文件路径【不加引号】：")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    urls_list = [line.strip() for line in file if line.strip()]
                open_all_urls(driver=driver, urls=urls_list)
            except FileNotFoundError:
                print("文件未找到，请检查路径并重试。")
            except Exception as e:
                print(f"读取文件时发生错误：{e}")
        elif do == 3:
            a = input("请输入txt文件前缀名【例如：天涯神贴】：")
            save_path = input("请输入TXT文件保存路径【例如：C:/保存路径/】【不加引号】：")
            urls = get_all_urls(driver)
            for i, j in enumerate(urls):
                html_page = get_html_from_one_tabs(driver=driver,url = j)
                print(f"网站{j}源码提取成功")
                save_html_to_txt(file_name=f"{save_path}{a}{i+1}.txt", html_content=html_page)
        elif do == 0:
            close_the_browser(driver=driver)
            break
        else:
            print("无效的选项，请重新输入。")



try:
    # 初始化 Chrome 浏览器
    driver = open_browser()

    main(driver)  # 用户主要更改这个部分

except WebDriverException as e:
    print(f"WebDriver 错误: {e}")
except Exception as ex:
    print(f"其他错误: {ex}")
finally:
    # 确保资源释放
    if 'driver' in locals() and driver.service.process:
        print("程序已结束，但浏览器可能仍在运行。")
