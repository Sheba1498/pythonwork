class Parent:
    def properties(self):
        self.props={"mobile":"Nokia","bike":"Passion"}
        return self.props

class Child(Parent):
    def properties(self):
        props=super().properties()
        props["car"]="Swift"
        return props

ch=Child()
print(ch.properties())
list.append()