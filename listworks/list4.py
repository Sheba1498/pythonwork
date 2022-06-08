#most frequent element
# lst=[10,11,11,12,13,14,14,14]
# dup_lst=[]
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         if lst[i]==lst[j]:
#             dup_lst.append(lst[i])
# print(f"1st recursive element is {dup_lst[0]} and 2nd recursive element {dup_lst[2]}")

# lst=[2,3,4,6,9]
# sum=15
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(f"pairs{lst[i],lst[j]}")
#             break

lst=[2,3,4,6,9,5]
lst.sort()
element=7
low=0
upp=len(lst)-1
while(low < upp):
    cur_sum=lst[low]+lst[upp]
    if cur_sum==element:
        print(f"pair {lst[low]},{lst[upp]}")
        low+=1
    elif cur_sum>element:
        upp-=1
    elif cur_sum<element:
        low+=1



