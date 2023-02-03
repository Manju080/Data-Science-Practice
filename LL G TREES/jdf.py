class Computer:
    wheels = 50
    def config(self):
        print("hello ")
    @classmethod
    def getschool(cls):
        return cls.wheels
    @staticmethod
    def info():
        print("hello darling")
    

com1 = Computer()

Computer.config(com1)

Computer.info()
print(Computer.getschool())