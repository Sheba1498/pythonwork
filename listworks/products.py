mobiles=[
    [1000,"samsungA52","4g","AMOLED",27000,"samsung",12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung",20],
    [1002, "redminote10", "4g", "led", 17000, "redmi",50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi",70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung",1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung",34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung",7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung",89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung",0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple",0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus",67]

]
# q1 total number of out_of_stock mobiles
out_stock_pro=[mob for mob in mobiles if mob[-1]==0]
print(len(out_stock_pro))

# q2 total stock
avl_stock=[mob[-1] for mob in mobiles]
print(sum(avl_stock))

# q3 print mobiles available in range 20k to 30k
mobile_price=[mob for mob in mobiles if mob[4] in range(20000,30000)]
print(mobile_price)

# q4 print all 5g phone
mobiles_5g=[mob for mob in mobiles if mob[2]=="5g"]
print(mobiles_5g)

# q5 print samsung mobiles
mobile_samsung=[mob for mob in mobiles if mob[-2]=="samsung"]
print(mobile_samsung)

# q6 print costly mobile
# mobiles.sort(reverse=True,key=lambda mob:mob[4])
# print(mobiles[0])

costly_mobiles=max(mobiles,key=lambda mob:mob[4])
print(costly_mobiles)

# q7 prin low cost mobiles
# mobiles.sort(key=lambda mob:mob[4])
# print(mobiles[0])

low_costly=min(mobiles,key=lambda mob:mob[4])
print(low_costly)

# q8 print all mobiles having stock >10
stock_gt=[mob for mob in mobiles if mob[-1]>10]
print(stock_gt)


# q9 count of mobiles having dispaly amoled
display=[mob for mob in mobiles if mob[3]=="AMOLED"]
print(len(display))

# q10 sort mobiles based on price oredr by desc
mobiles.sort(reverse=True,key=lambda mob:mob[4])
print(mobiles)

# q11 sort mobiles based on avl stock oredr by desc
mobiles.sort(reverse=True,key=lambda mob:mob[-1])
print(mobiles)

# q12 is there any mobile available at rs 10000 ?
mob_ten=[mob[4]==10000 for mob in mobiles]
print("available" if True in mob_ten else "not available" )

# q12 list all mobiles having same price