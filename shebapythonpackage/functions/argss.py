# def sum_fun(*args):
#     return sum(args)
# print(sum_fun(14,16,18,19,10,30))
#
# def max_fun(*args):
#     return max(args)
# print(max_fun(45,80,678,321,90))
#
# def min_fun(*args):
#     return min(args)
# print(min_fun(67,89,23,21,8,54,43))


def add_nums(**kwargs):
    print(sum([v for k,v in kwargs.items()]))


add_nums(n1=10,n2=30,n3=70)