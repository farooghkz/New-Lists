# New-Lists
4 new methods for python lists
### last_index
Just like L.index but counts from end to start.
### sub
Checks if a list is a sub-list of another list or not.returns start index if it is, and None if the smaller list is not a sub list of the bigger one.
### del_sublist
Deletes sub-list of the bigger list, and if the smaller list was not a sub-list of the bigger one, raises ValueError.
### replace
Replaces a value with another value in the list.
## Sample Code
```
from new_list import *

myList = list([1, 2, 4, 6, 1, 2, 3, 56, 1, 13])
print(myList.last_index(1))
print(myList.sub(list([6, 1, 2])))
myList.del_sublist(list([1, 2, 3]))
print(myList)
myList.replace(1, 0)
print(myList)
```
