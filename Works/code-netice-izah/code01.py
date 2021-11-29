class A:
    def one(self):
        return self.two()
    def two(self):
        return 'A'

class B(A):
    def two(self):
        return 'B'

obj=A()
obj2=B()

print(obj.two(), obj2.two())

#### bele basa dusdumki polifornizm budur mehz neticeni alir inherit edir 
# ama oz deyisiyliyni qatir iwin icine 
