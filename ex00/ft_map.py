def ft_map(fc, list):
    for x in list:
        yield fc(x)


# def x2(n):
#     return n*2
#
#
# li = (1, 2, 3, 4, 5)
#
# print(map(x2, li))
# print(ft_map(x2, li))
#
# print(list(map(x2, li)))
# print(list(ft_map(x2, li)))
