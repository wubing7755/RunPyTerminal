# -*- coding: GBK -*-

import subprocess

from FilePDF import read_pdf

from Stack import Stack


def main():
    # 读取pdf文件，并写入txt文件中
    #read_pdf()

    stack = Stack()

    nums = input("请输入一串数字，以 ',' 分隔：").split(',')

    for num in nums:
        stack.push(num)

    stack.print_stack()

    # 复原
    stack.pop(stack)
    stack.print_stack()

    # 撤销
    stack.push(stack)
    stack.print_stack()

if __name__ == "__main__":
    # 打开命令提示符并执行 'cls' 命令
    subprocess.run("cmd.exe /c cls", shell=True)
    main()