class MyArray:
    def __init__(self):
        self.length = 0;
        self.data = []

    def get_value(self, index):
        if self.length == 0:
            print("MyArray is empty")
        return self.data[index]

    def push(self, data1):
        self.data.append(data1)
        self.length = self.length+1

    def print_myarray(self):
        strr = ''
        for val in self.data:
            strr += str(val)+'-->'
        print(strr)


mya = MyArray()
mya.push(100)
mya.push(200)
mya.push(300)
print(mya.get_value(0))
print(mya.get_value(2))

mya.print_myarray()