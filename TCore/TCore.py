# -*- coding: GBK -*-

import subprocess

from FilePDF import read_pdf

from Stack import Stack


def main():
    # ��ȡpdf�ļ�����д��txt�ļ���
    #read_pdf()

    stack = Stack()

    nums = input("������һ�����֣��� ',' �ָ���").split(',')

    for num in nums:
        stack.push(num)

    stack.print_stack()

    # ��ԭ
    stack.pop(stack)
    stack.print_stack()

    # ����
    stack.push(stack)
    stack.print_stack()

if __name__ == "__main__":
    # ��������ʾ����ִ�� 'cls' ����
    subprocess.run("cmd.exe /c cls", shell=True)
    main()