from ctypes import *
import math

from typing import TypeVar
T = TypeVar('T')  # used to represent an arbitrary type

class MyList:
    __slots__ = ('_n', '_capacity', '_array')

    # class-level variables for stats
    _resizes: int = 0  # total number of resizes
    _copies:  int = 0  # number of array-to-array copies during resizing

    @classmethod
    def resetStats(cls) -> None:
        MyList._resizes = 0
        MyList._copies = 0

    @classmethod
    def getStatsDict(cls) -> dict:
        return {"resizes" : MyList._resizes, \
                "copies"  : MyList._copies}

    def __init__(self):
        self._n        = 0  # number of actual elements currently in the list
        self._capacity = 1  # default MyList capacity

        self._array    = self._make_array(self._capacity)

    def _make_array(self, capacity: int):# -> #'ctypes array':
        ''' private method to reserve space for a low-level array of the
            given capacity
        Parameters:
            capacity: integer size of the array
        Returns:
            a ctypes low-level array
        '''
        ArrayType = (capacity * py_object)  # defined in ctypes
        return ArrayType() # create and return an array of py_object of size capacity

    def __len__(self) -> int:
        ''' returns number of actual elements in the array
        Returns:
            integer count of number of elements in the array
        '''
        return self._n
        

    def __getitem__(self, index: int) -> T:
        ''' returns the item in the array at the given index
        Parameters:
            index: integer index between 0 and self.len() - 1
        Returns:
            item of type T at given index
        Raises:
            IndexError exception if index is invalid
        '''
        pass

        if index > self._n-1:
            raise IndexError("Index out of bounds")
        
        if index < 0:
            raise ValueError('Only supporting positive indexing')
        
        if not isinstance(index, int):
            raise TypeError('Index must be integer')
        
        return self._array[index]

    def __setitem__(self, index: int, item: T) -> None:
        ''' sets the entry in the array at the given index to the given item
        Parameters:
            index: integer index between 0 and self.len() - 1
            item:  type-T element (must match type of entries already in list)
        Returns:
            None
        Raises:
            IndexError exception of index is invalid
            TypeError exception if type of item does not match types in array
        '''

        if not isinstance(index, int):
            raise TypeError('Index must be int')
        
        if index > self._n-1:
            raise IndexError("Index out of bounds")
        
        if index < 0:
            raise ValueError('Only supporting positive indexing')

        self._array[index] = item
        pass

    def append(self, item: T) -> None:
        ''' appends the given item to the array, increasing the capacity of
            the array as necessary
        Parameters:
            item: type-T element to append to the array
        Return:
            None
        Raises:
            TypeError exception if type of item does not match types in array
        '''



        if self._n > 0 and not isinstance(item, type(self._array[0])):
        # Type check against the first element if the list is not empty
            msg = f'Data type {type(item)} does not match data type of current elements in the array. Current data type: {type(self._array[0])}'
            raise ValueError(msg)

        if self._n == self._capacity:
            #print("adding more space to the array")
            self._resize(10 * self._capacity)
            #self._resize(2 * self._capacity)
            #self._resize(math.ceil(1.5 * self._capacity))
            #self._resize(math.ceil(1.25 * self._capacity))
            #self._resize(math.ceil(1024 + self._capacity))
            #self._resize(math.ceil(2048 + self._capacity))
            self._resize(math.ceil(4096 + self._capacity))
            MyList._resizes += 1
            

        self._array[self._n] = item
        self._n += 1

    def _resize(self, capacity: int) -> None:
        ''' private method to resize the array to a specific capacity,
            copying elements from the old array into the new
        Parameters:
            capacity: integer size of the new array
        Returns:
            nothing

        '''
        new_array = self._make_array(math.ceil(capacity))

        for i in range(self._n):
            new_array[i] = self._array[i]
            MyList._copies +=1

        self._array = new_array

        self._capacity = capacity


        

    def __str__(self) -> str:
        ''' a string representation of this MyList
        Returns:
            a printable string format of the MyList contents
        '''

        _str = '['

        for i in range(self._n):
            _str += str(self._array[i]) + ', '
        
        _str = _str[:-1]
        return _str + ']'


def main():

    l1 = MyList()
    l1.append(1)
    l1.append(2)

    for i in range(18,300,2):
        l1.append(i%18)

    print(l1)


if __name__ == '__main__':
    main()