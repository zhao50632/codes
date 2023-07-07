import tkinter as tk
from selenium import webdriver
from PIL import Image, ImageChops
 # 打开IE浏览器，并截取页面截图
def take_ie_screenshot():
    driver = webdriver.Ie()  # 需要安装IE浏览器和对应的驱动
    driver.get(url_entry.get())
    driver.save_screenshot("ie_screenshot.png")
    driver.quit()
    result_label.config(text="IE截图完成！")
 # 打开Edge浏览器，并截取页面截图
def take_edge_screenshot():
    driver = webdriver.Edge()  # 需要安装Edge浏览器和对应的驱动
    driver.get(url_entry.get())
    driver.save_screenshot("edge_screenshot.png")
    driver.quit()
    result_label.config(text="Edge截图完成！")
 # 计算两个截图的匹配度
def compare_screenshots():
    image1 = Image.open("ie_screenshot.png")
    image2 = Image.open("edge_screenshot.png")
    diff = ImageChops.difference(image1, image2)
    if diff.getbbox():
        diff.show()  # 显示差异图像
        result_label.config(text="差异很大，页面显示存在差异")
    else:
        result_label.config(text="兼容性很好，页面显示一致")
 # 创建主窗口
window = tk.Tk()
window.title("截图与对比")
window.geometry("400x200")
 # 创建URL输入框和按钮
url_label = tk.Label(window, text="URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()
 ie_button = tk.Button(window, text="IE截图", command=take_ie_screenshot)
ie_button.pack()
 edge_button = tk.Button(window, text="Edge截图", command=take_edge_screenshot)
edge_button.pack()
 compare_button = tk.Button(window, text="对比", command=compare_screenshots)
compare_button.pack()
 result_label = tk.Label(window, text="")
result_label.pack()
 # 运行主循环
window.mainloop()