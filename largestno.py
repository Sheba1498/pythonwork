##largest number
from functools import reduce


num=[9,34,7,8,32,89]
str_lst=[str(n) for n in num]
# print(str_lst)
max_num=reduce(lambda n1,n2:(n1+n2) if (n1+n2)>(n2+n1) else (n2+n1),str_lst)
print(max_num)
