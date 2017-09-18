# coding=utf-8
import os


def rename_files():
    file_list = os.listdir(r"D:\MyDocuments\工作记录\学习文件夹\PythonLearning\PhotoTest\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("当前目录是：" + saved_path)
    os.chdir(r"D:\MyDocuments\工作记录\学习文件夹\PythonLearning\PhotoTest\prank")
    for file_name in file_list:
        print('旧文件夹名：' + file_name)
        print('新文件夹名：' + file_name.translate(file_name.maketrans('', '', '0123456789')))
        os.rename(file_name, file_name.translate(file_name.maketrans('', '', '0123456789')))
    os.chdir(saved_path)


rename_files()
