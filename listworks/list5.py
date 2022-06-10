#binary search
# arr=[10,11,12,14,14,15,16]
# element=10
# flag=0
# arr.sort()
# low=0
# upp=len(arr)-1
# while(low<=upp):
#     mid=(low+upp)//2
#     if element==arr[mid]:
#         flag=1
#         break
#     elif element>arr[mid]:
#         low=mid+1
#     elif element<arr[mid]:
#         upp=upp-1
# print("found" if flag>0 else "not found")

#print common elements
# arr1=[20,12,17,16,11,15]
# arr2=[8,19,14,16,18,20]
# p1=0
# p2=0
# arr1.sort()
# arr2.sort()
# while(p1<len(arr1) and p2<len(arr2)):
#     if arr1[p1]==arr2[p2]:
#         print(f"common {arr1[p1]}")
#         p1+=1
#         p2+=1
#     elif arr1[p1]>arr2[p2]:
#         p2+=1
#     elif arr1[p1]<arr2[p2]:
#         p1+=1


