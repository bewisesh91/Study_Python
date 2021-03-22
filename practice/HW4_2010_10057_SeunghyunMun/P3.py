"""
Implement a function that takes a dictionary as an argument
and returns the number of values that appear two or more times.

* Condition: All values are hashable.


>>>P3({'red': 1, 'green': 1, 'blue': 2})
1

>>>P3({'r': 'a', 'g': 'b', 'b': 'c'})
0

>>>P3(dict())
0

>>>P3({'a':True, 'b': True, 'c':2, 'd':2})
2
"""

def P3(dct):
    new_list = []
    for key, value in dct.items() :
        new_list.append(value)
    new_list2 = []
    for i in new_list :
        if new_list.count(i) > 1 :
            new_list2.append(i)
    return len(set(new_list2))
