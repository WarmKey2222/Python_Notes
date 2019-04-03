import sys

'''
# 多行输入方法一
str_list = []
for line in sys.stdin:  # 需在里面限制输入字符串的个数
    tempStr = line.split()
    if line[0] is '\n':
        break
    if len(line) > 64+1:            # 字符串长度<=64
        break
    str_list.extend(tempStr)
    if len(str_list)+1 > 100:       # 输入字符串个数<=100
        break
    
'''
str_list = []
# 多行输入方法二
while True:
    #line = sys.stdin.readline().strip()    strip（）会把"\n"去掉
    line = sys.stdin.readline()
    tempStr = line.split()
    if line[0] is '\n':
        break
    if len(line) > 64+1:            # 因为包含了"\n",长度比实际多1  # 字符串长度<=64
        break
    str_list.extend(tempStr)
    if len(str_list)+1 > 100:       # 输入字符串个数<=100
        break
