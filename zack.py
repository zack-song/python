class Geese:
    number = 0
    def __init__(self):
        self.number +=1
        print(Geese.number)

list1 = []
for i in range(4):
    list1.append(Geese())