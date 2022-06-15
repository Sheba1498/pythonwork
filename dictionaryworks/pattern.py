# pattern="abaccd"
# char_dict={}
# for char in pattern:
#     if char in char_dict:
#         print("first recursive element",char)
#         break
#     else:
#         char_dict[char]=1


pattern="ababcc"
char_dict={}
recursive_list=[]
for char in pattern:
    if char in char_dict:
        recursive_list.append(char)
    else:
        char_dict[char]=1
print(recursive_list[1])




