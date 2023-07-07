from selenium import webdriver
from PIL import Image, ImageChops
import tkinter as tk
def check_browser_open(browser):
    driver = None
    if browser == "IE":
        try:
            driver = webdriver.Ie()
        except:
            result_label.config(text="IE浏览器未打开页面！")
    elif browser == "Edge":
        try:
            driver = webdriver.Edge()
        except:
            result_label.config(text="Edge浏览器未打开页面！")
    return driver
def take_screenshot(browser):
    driver = check_browser_open(browser)
    if driver:
        driver.save_screenshot(f"{browser.lower()}_screenshot.png")
        driver.quit()
        result_label.config(text=f"{browser}截图完成！")
        compare_screenshots()
    else:
        result_label.config(text="浏览器未打开页面！")
def compare_screenshots():
    try:
        image1 = Image.open("ie_screenshot.png")
        image2 = Image.open("edge_screenshot.png")
        diff = ImageChops.difference(image1, image2)
        if diff.getbbox():
            diff.show()  # 显示差异图像
            result_label.config(text="差异很大，页面显示存在差异")
        else:
            result_label.config(text="兼容性很好，页面显示一致")
    except FileNotFoundError:
        result_label.config(text="请先进行截图！")
 # 创建主窗口
window = tk.Tk()
window.title("截图与对比")
window.geometry("400x200")
 # 创建URL输入框和按钮
url_label = tk.Label(window, text="URL:")
url_label.pack()
url = ""  # 存储URL
def store_url():
    global url
    url = url_entry.get()
url_entry = tk.Entry(window)
url_entry.pack()
store_url_button = tk.Button(window, text="保存URL", command=store_url)
store_url_button.pack()
ie_button = tk.Button(window, text="IE截图", command=lambda: take_screenshot("IE"))
ie_button.pack()
edge_button = tk.Button(window, text="Edge截图", command=lambda: take_screenshot("Edge"))
edge_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
 # 运行主循环
window.mainloop()
