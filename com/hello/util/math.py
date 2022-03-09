# coding:UTF-8
def add(*numbers): 				# 定义函数
    """
    实现一个任意多个数字的累加操作
    :param numbers: 进行累加操作的数字元组
    :return: 数字累加结果
    """
    sum = 0                                         # 保存数字累加结果
    for num in numbers:                             # 迭代元组
        sum += num                                  # 数字累加
    return sum                                      # 返回累加结果
