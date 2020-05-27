# import functools
# import operator


def ft_reduce(fc, list):
    if len(list) > 0:
        res = list[0]
        for x in list[1:]:
            res = fc(res, x)
        return res
    else:
        raise TypeError("ft_reduce() of empty sequence with no initial value")

#
# li = [1, 2]
#
# print(functools.reduce(operator.truediv, li))
# print(ft_reduce(operator.truediv, li))
