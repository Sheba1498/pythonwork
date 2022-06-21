accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]


#q1  print details of 1002
# for ac in accounts:
#     if ac["acno"]==1002:
#         transactions=ac.pop("transactions")
#         print(ac)

# ac_details=[ac for ac in accounts if ac["acno"]==1002]
# print(ac_details)


#print savings type account details
# savings_ac=[ac["acno"] for ac in accounts if ac["ac_type"]=="savings"]
# print(savings_ac)

#q3 sort account based on balance on descending order
# accounts.sort(reverse=True, key=lambda ac:ac["balance"])
# print(accounts)


#q4 prit all phone pay transactions
# for ac in accounts:
#     for tr in ac["transactions"]:
#         if tr["method"]=="phone-pay":
#             print(tr)

# all_transactions=[ac["transactions"] for ac in accounts]
# phonepay=[trans for tlist in all_transactions for trans in tlist if trans["method"]=="phone-pay"]
# print(phonepay)

#amount>500
# for ac in accounts:
#     for tr in ac["transactions"]:
#         if tr["amount"]>500:
#             print(tr)



#q6 crredit transactions of 1002
# for ac in accounts:
#     for tr in ac["transactions"]:
#         if tr["to"]==1002:
#             print(tr)

#q7 aggregate transactions based on payment mode
pms={}
all_transactions=[ac["transactions"] for ac in accounts]
transactions=[trans for tlist in all_transactions for trans in tlist]
for transaction in transactions:
    p_method=transaction["method"]
    amount=transaction["amount"]
    if p_method in pms:
        pms[p_method]+=amount
    else:
        pms[p_method]=amount
print(pms)
print(max(pms.items(),key=lambda item:item[1]))