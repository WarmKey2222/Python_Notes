"""
题目描述：
--  对输入字符串检查是否存在非法字符，输出合法字符串（去重）和非法字符串（不去重）
--  对合法字符串循环左移10次，在进行排序输出。（举例：比如字符串"abc"，循环左移一次的结果为"bca"）
输入描述：
(1) 字符串中的字符集合为 '0'-'9'，'a'-'z'，'A'-'Z'，其余为非法字符串（空字符串作为定界符），
    有非法字符的字符串被视为非法输入；
(2) 作为输入的字符串个数不超过100，每个字符串长度不超过64；
(3) 作为输入的连续空字符串（空格/制表符/回车/换行符）作为一个空格处理（作为定界符，字符串起始字符不能为空）；
(4) 输入每行只有一个字符串
(5) 输入以空行结束
输出描述：
(1) 输出合法字符串并去重
(2) 输出所有非法字符串
(3) 对结果1的去重合法字符串循环左移10次
(4) 对结果3合法字符串字符串排序，按ASCII表字符从小到大顺序排序
注意事项：
--  每输入一个字符后用空格跟下一个字符串隔离，作为输出的所有字符串之间只能有一个空格（作为定界符）；
示例1:
-- 输入
abc
def
==
acd123
44234tjg
aga'-=
ad--s
abd
123
abcdef
1234567890123456789012345678901234567890123
45678901234567890123
EDFG
SDFG
ABC
DEF
cccc
a*b=1
dd
87&&^
asdfas
234abc35
765rgfh4sd
1231
123
==
EDFG

-- 输出
abc def acd123 44234tjg abd 123 abcdef 1234
5678901234567890123456789012345678901234567
8901234567890123 EDFG SDFG ABC DEF cccc dd
asdfas 234abc35 765rgfh4sd 1231
== aga'-= as--s a*b=1 87&&^ ==
bca efd 23acd1 234tjg44 bda 231 efabcd 1234
5678901234567890123456789012345678901234567
8901231234567890 FGED FGSD BCA EFD cccc dd
asasdf 4abc3523 765rgfh4sd 3112
1234567890123456789012345678901234567890123
45678901231234567890 231 234tjg44 23acd1 31
12 4abc3523 765rgfh4sd BCA EFD FGED FGSD as
asdf bca bda cccc dd efabcd efd
"""
########################################################################################################################
########################################################################################################################
'''
NOTE:
# 注意输入时strip()、split()用法
# extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# ord('a') 返回字符a的ASCII码
# index = [m.start() for m in re.finditer(' ',x)] 返回输入字符串中空格所在索引位置
# 字符串去重时，由于需要删除列表新加入的元素，而remove()只能移除列表中第一个匹配的元素，因此需要找到需去重的字符串索引
# 用pop(index)，从后往前的弹出。由于在此期间存储字符串的列表长度在动态改变，而for循环不能动态改变数组长度，因此用while

# split(str="",num=string.count(str)) 函数
# str_test = 'This\t\t is    a\t\t\t test for   split()'
# 输入：str_test.split()           # 默认分割(删除)所有的空字符，包括空格、换行(\n)、制表符(\t)等
# 输出：['This', 'is', 'a', 'test', 'for', 'split()']
# 输入：str_test.split('s')        # 分割所有的字符s
# 输出：['Thi', '\t\t i', '    a\t\t\t te', 't for   ', 'plit()']
# 输入：str_test.split('s',2)      # 分割前2个字符s
# 输出：['Thi', '\t\t i', '    a\t\t\t test for   split()']
'''
########################################################################################################################
########################################################################################################################
import sys


# 初始化输入
def input_init():
    string_list = []
    while True:
        line = sys.stdin.readline().rstrip('\n')        # 逐行读入，并去除行末的换行符
        if 0 == len(line):                              # 输入以空行结束,break语句较强应放在continue语句前，不然会陷入死循环
            break
        if len(line) > 64:                              # 每个字符串长度不超过64
            continue
        if len(string_list) > 100-1:                    # 输入字符串个数不超过100
            continue
        if (line.startswith(' ')) & (0 != len(line)):   # 输入字符串不能以空格开始
            continue
        temp_str = line.split()                         # split()，默认分割(删除)所有的空字符，包括空格、换行(\n)、制表符(\t)等
        string_list.append(' '.join(temp_str))          # 输入的连续空字符串（空格/制表符/回车/换行符）作为一个空格处理
    return string_list


# 保存合法字符串
def get_legal_string(string_list: list):
    number_ls = list("0123456789")
    letter_ls = list("abcdefghijklmnopqrstuvwxyz")
    up_letter_ls = []
    for letter in letter_ls:
        up_letter_ls.append(letter.upper())

    flag = int(0)
    legal_str = []

    for index in range(0, len(string_list)):
        temp_str = string_list[index]
        for ix in range(0, len(temp_str)):
            x = temp_str[ix]
            if (x in number_ls) | (x in letter_ls) | (x in up_letter_ls):
                # 合法字符串
                flag = 1
            else:
                flag = 0
                break
        if flag:
            legal_str.append(temp_str)
    return legal_str


# 去除列表中重复的字符串
def remove_repeat_string(string_list: list):
    remove_repeated_str = string_list.copy()
    ix = 0
    while True:
        temp_str = remove_repeated_str[ix]
        count = remove_repeated_str.count(temp_str)             # 统计重复字符串个数
        if ix == len(remove_repeated_str)-1:
            break
        if count == 1:
            ix = ix + 1
            continue
        while count > 1:                                        # for循环不能动态改变数组长度，因此用while
            count = count - 1
            j = 1
            while True:
                need_remove = remove_repeated_str[-j]           # 反序遍历
                if temp_str == need_remove:
                    #remove_repeated_str.remove(need_remove)    # 因为remove()只能移除列表中第一个匹配的元素
                    pop_index = len(remove_repeated_str) - j
                    remove_repeated_str.pop(pop_index)          # 删除指定索引位置元素(反序)
                    break
                else:
                    j = j + 1
    return remove_repeated_str


# 保存非法字符串
def get_non_legal_string(raw_string_list: list, legal_string: list):
    non_legal_str = []
    for i in raw_string_list:
        if i in legal_string:
            continue
        non_legal_str.append(i)  # 非法字符串
    return non_legal_str


# 左移10次字符 10%len(str)
def shift_string(string_list: list):
    shift_string = []
    for shift_str in string_list:
        start = 10 % len(shift_str)
        shift_temp = ""
        shift_temp += shift_str[start:]
        shift_temp += shift_str[:start]
        shift_string.append(shift_temp)
    return shift_string


# 输出字符串结果
def output_string(string_list: list):
    output = ""
    for str_ in string_list:
        output += str_ + " "
    print(output)


def main():
    # 原始输入
    str_list = input_init()
    # 保存合法字符串
    legal_str = get_legal_string(str_list)
    # 保存非法字符串
    non_legal_str = get_non_legal_string(raw_string_list=str_list, legal_string=legal_str)
    # 保存合法字符串_去重
    remove_repeated_string = remove_repeat_string(legal_str)
    # 1.输出去重合法字符串
    output_string(remove_repeated_string)
    # 2.输出未去重的非法字符串
    output_string(non_legal_str)
    # 3.输出去重合法字符串左移10次后的结果
    shift_legal_str = shift_string(remove_repeated_string)
    output_string(shift_legal_str)
    # 4.输出对合法字符串字符串左移后排序，按ASCII表字符从小到大顺序排序
    shift_legal_str = sorted(shift_legal_str)
    output_string(shift_legal_str)


if __name__ == '__main__':
    main()
