"""Define an array class"""


class Array:
    def __init__(self):
        my_list = [2, 5, 7, 11, 13]
        self.item = my_list

    # get length of array
    def __len__(self):
        return len(self.item)

    # get get item of array
    def __getitem__(self, index):
        return self.item[index]

        if type(index) is not int:
            raise TypeError("This is not an integer")

        if index > len(item) - 1:
            raise IndexError("Not in range of index")

    def __setitem__(self, key, value):
        pass


"""define subclass"""


class DynamicArray(Array):
    # define append method to add to list
    def append(self, item):
        for _ in self.item:
            if self.item:
                self.item.append(item)
                return self.item

    # delete from array
    def delete(self, last_item):
        for _ in self.item:
            if self.item:
                self.item.pop(last_item)
                return self.item

        if last_item is None:
            raise TypeError("Please insert an item")

    # return boolean to test for item in list
    def __contains__(self, item):
        if item in self.item:
            return True
        else:
            return False

    # define reverse method to reverse item in list
    def reverse(self):
        """reverse the array"""
        if self.item is not None and self.__len__() >= 0:  # class len function we created
            i = 0
            new_array = []
            size = self.__len__() - 1
            while size >= i:
                new_array.append(self.item[size - i])
                i += 1
            return new_array

    def insert(self, index, data):
        """ Inserts data at a specific index
        BEST: O(1)
        WORST: O(n)
        """
        if index == 0:
            self.item.insert(data)
            return
        at_index = self.__getitem__(index - 1)
        if at_index is None:
            raise IndexError
        if self.item is None:
            self.append(data)
            return