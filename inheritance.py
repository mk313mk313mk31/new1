class Mammal:
    def talk(self):
        print("talk")
class Dog(Mammal):
    def brak(self):
        print("brak")
class cat (Mammal):
    pass
dog1 = Dog()
dog1.brak()
dog1.talk()
