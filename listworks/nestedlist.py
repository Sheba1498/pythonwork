lst=[
    [10,11],
    [12,28],
    [14,40],
    [15,30]
]
# for sub_list in lst:
#     for num in sub_list:
#         if (num>16):
#             print(num)
# print(max(lst))
# print(lst)

# flatten_list=[]
# for sub_list in lst:
#     for num in sub_list:
#         flatten_list.append(num)
# print(flatten_list)
# print(max(flatten_list))
# print(min(flatten_list))
# print(flatten_list.sort())

# flatten_list=[num for sub_list in lst for num in sub_list]
# print(flatten_list)
# flatten_list.sort()
# print(flatten_list)

#list comprehension
# num_odd=[num for num in flatten_list if num%2!=0]
# print(num_odd)
#
#
#
# num_evn=[num for num in flatten_list if num%2==0]
# print(sum(num_evn))


flatten_list=[num for sub_list in lst for num in sub_list]
mapped_list=[ num+1 if num>25 else num-1 for num in flatten_list]
print(mapped_list)


