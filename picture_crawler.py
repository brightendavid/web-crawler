# -*- coding: utf-8 -*-


# picture_crawler.py
import urllib.request  # 主要用于打开和阅读url
import os, re
import urllib.error  # 用于错误处理

dirpath = r"image1/"


def picCraw(url, theme, imgref):
    count = 1
    file_name = os.path.join(dirpath, theme + ".html")
    print("正在保存:" + file_name)
    m = urllib.request.urlopen(url).read()
    new_path = os.path.join(dirpath, theme)
    if not os.path.isdir(new_path): os.makedirs(new_path)  # 创建目录保存图片
    page_data = m.decode('gbk')
    MatchedImages = re.findall(imgref, page_data)  # 找出所有匹配
    print("MatchedImages:", MatchedImages)
    for image in MatchedImages:  # 用正则表达式匹配所有的图片
        pattern = re.compile(r'//.*\.jpg$')  # 匹配jpg格式的文件
        if pattern.search(image):  # 如果匹配成功，则获取图片信息；若不成功继续下一个
            try:
                if "http" not in image: image = "http:" + image
                image_data = urllib.request.urlopen(image).read()  # 获取图片信息
                image_path = os.path.join(dirpath, theme, str(count) + ".jpg")  # 给图片命名
                count += 1
                with open(image_path, "wb") as image_file:
                    image_file.write(image_data)  # 将图片写入jpg文件
            except urllib.error.URLError as e:
                print("Download failed")
        with open(file_name, "wb") as file:  # 将页面写入文件
            file.write(m)


if __name__ == "__main__":
    url = 'http://www.jituwang.com/tuku/biology/'
    imgpattern = r'<img src=\"(.+\.jpg)\"'  # 匹配图片的pattern,可通过查看网页源代码获悉
    picCraw(url, "fenxi", imgpattern)
