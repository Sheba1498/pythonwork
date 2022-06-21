def add_numbers(n1,n2):
    return n1+n2
print(add_numbers(14,26))

def sub_numbers(n1,n2):
    return n1-n2
print(sub_numbers(100,90))

def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1
print(smart_sub(14,24))

def num_chk(n1):
    return "even" if n1%2==0 else "odd"
print(num_chk(14))

def validate_gmail(mail):
    return mail.endswith("@gmail.com")
print(validate_gmail("sk14@yahoo.com"))

def factorial(n):
    fact=1
    for i in range(1,(n+1)):
        fact=fact*i
    return fact
print(factorial(4))






