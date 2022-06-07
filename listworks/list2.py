# element=12

# flag=0
# for num in lst:
#     if element==num:
#         flag=1
#         break
# if flag==1:
#     print("element found")
# else:
#     print("not found")

lst=[10,12,14,17,14,20,24,14]
evnlist=[]
for num in lst:
    if num%2==0:
        evnlist.append(num)
print(evnlist)
evnlist.sort(reverse=True)
print(evnlist)
evnlist.pop(3)
print(evnlist)
evnlist.insert(2,16)
print(evnlist)
print(lst.count(14))
