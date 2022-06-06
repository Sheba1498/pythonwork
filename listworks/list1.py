# expenses=[10000,12000,14000,16000,18000,20000]
# for amount in expenses:
#     print(amount)

# for i in range(0,len(expenses)):
#     print(expenses[i])

# len(expenses)->fun returns length of obj

numbers=[10,11,13,14,17,18,19]
# for num in numbers:
#     if num<15:
#         print(num-1)
#     elif num>15:
#         print(num+1)
#     else:
#         print(num)

#print count of nos where nos in range of including 14-18
# numbers=[10,11,13,14,17,18,19]
# count=0
# for num in numbers:
#     if num<=18 and num>=14:
#         count+=1
# print(count)

#neg count and po count and zero count
numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
# p_count=0
# n_count=0
# z_count=0
# for num in numbers:
#     if num>0:
#         p_count+=1
#     elif num<0:
#         n_count+=1
#     elif num==0:
#         z_count+=1
# print(f"+ve count{p_count},-ve count{n_count},zero count{z_count}")
#total sum

sum=0
for num in numbers:
    sum=sum+num
    num+=1
print(sum)









