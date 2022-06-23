
#overriding
class Parent:
    def phone(self):
        print("Nokia")

    def bike(self):
        print("passion")


class Child(Parent):
    def phone(self):
        print("Iphone 12")
    def bike(self):
        print("Bullet")


ch=Child()
ch.phone()
ch.bike()

