#使用python编写程序实现的搜索文件夹里面所有文件包括子目录文件，将文件内容包含primarykey的行内容写入到csv文件里面

import os
import csv

def search_files(primarykey, folderpath, outputfile):
    with open(outputfile, "w", newline='') as outfile:
        writer = csv.writer(outfile)
        for root, dirs, files in os.walk(folderpath):
            for file in files:
                if file.endswith(".java"):
                    filepath = os.path.join(root, file)
                    with open(filepath, "r") as infile:
                        for line in infile:
                            if primarykey in line:
                                writer.writerow([filepath, line.strip()])

search_files("SpringApplicationBuilder", "C:\abc\wara", "E:\Jason2020\wara\output.csv")
