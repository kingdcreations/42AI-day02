def ft_filter(fc, list):
    for x in list:
        if (fc is None or fc(x)):
            yield x
#
#
# def x2(n):
#     if (n > 3):
#         return True
#     return False
#
#
# li = (1, 2, 3, 4, 5)
#
# print(list(filter(x2, li)))
# print(list(ft_filter(x2, li)))
#
# print(list(filter(None, li)))
# print(list(ft_filter(None, li)))
#
# print((filter(x2, li)))
# print((ft_filter(x2, li)))
