# Python_Notes
Record some magic commands or codes!
# Ipython

1. %run xxx.py 运行python文件
2. 若.py不在当前目录下，在ipython终端可以使用系统命令，比如cd、ls等等；cd 时，可以直接把文件拖到终端窗口，自动生成文件路径（Linux）
3. %paste 复制粘贴板里的内容至终端（代码）
4. %timeit function(para1, para2, ...) 查看某函数的运行时间 
5. %pdb on 相当于在命令行中调试，若程序出错，可以打印变量的值。比如 p a(打印变量a的值)，p b(打印变量b的值)，最后q命令退出。不想用自动开调试，在ipython终端运行此命令：%pdb off
6. _(一个下划线)表示操作（命令）的上一个历史，__(两个下划线)表示上两个操作的历史
7. _34得到第34行输入代码的运行结果
8. _i34得到第34行输入代码
10. ![常用的魔术命令](https://github.com/pick-up-a-drop-of-water/Python_Notes/blob/master/pictures_stored/Ipython常用的魔术命令.png)

