
import math


class TinyStatistician(object):
    """docstring for TinyStatistician."""

    def __init__(self):
        pass

    def mean(self, arr):
        try:
            if len(arr) == 0:
                return None
            res = 0
            for x in arr:
                res += x
            return float(res / len(arr))
        except TypeError:
            return None

    def median(self, arr):
        try:
            n = len(arr)
            if n == 0:
                return None
            arr.sort()
            if n % 2 == 0:
                return self.mean([arr[int(n/2-1)], arr[int(n/2)]])
            else:
                return float(arr[int((n - 1)/2)])
        except TypeError:
            return None

    def quartiles(self, arr, percentile):
        try:
            n = len(arr)
            if n == 0:
                return None
            if percentile == 25:
                p = 0.25
            elif percentile == 75:
                p = 0.75
            else:
                return None
            arr.sort()
            if n % 2 == 0:
                return self.mean([arr[int(n*p-1)], arr[int(n*p)]])
            else:
                return float(arr[int((n-1)*p)])
        except TypeError:
            return None

    def var(self, arr):
        try:
            if len(arr) == 0:
                return None
            res = 0
            for x in arr:
                res += pow(x - self.mean(arr), 2)
            return float(res / len(arr))
        except TypeError:
            return None

    def std(self, arr):
        try:
            if len(arr) == 0:
                return None
            return math.sqrt(self.var(arr))
        except TypeError:
            return None


tstat = TinyStatistician()
a = [1]

print(tstat.mean(a))
print(tstat.median(a))
print(tstat.quartiles(a, 25))
print(tstat.quartiles(a, 75))
print(tstat.var(a))
print(tstat.std(a))
