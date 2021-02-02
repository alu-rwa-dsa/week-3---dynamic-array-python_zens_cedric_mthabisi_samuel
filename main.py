from array import Array
from array import DynamicArray

# create instance of class Array
x = Array()

# create instance of subclass DynamicArray
y = DynamicArray()

# print method calls
print(x.__len__())
print(x.__getitem__(2))
print(y.append(2))
print(y.delete(0))
print(x.item)
print(y.__contains__(13))
print(y.reverse())
print(y.insert(1, 4))



