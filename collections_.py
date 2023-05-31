"""
import json

list1 = [1, 2.2, '3', (1, 2, 4), 5, 1, 3]
print(list1[3])

unique = set(list1)

print(type(unique))
print(unique)

list2 = list(set(list1))
print(type(list2))
print(list2)

my_tuple = (1, 2, 3, 4, 6)

my_list = []
my_list2 = list()
my_string = 'Any string value'

my_list3 = list(my_string)
print(type(my_list3))
print(my_list)

s = [sym for sym in range(5)]
print(type(s))
print(s)

dictionary = {'one': my_tuple, 'two': 2}
print(dictionary['one'])

lst =[0, 1, 2, 3, 4, 5]
lst2 = []

print(lst)
print(lst2)



lst = [1, 2, 3]
lst2 = lst.copy()
#s = {1:1}

print(lst)
print(lst2)

lst3 = [[1, 2], [3, 4], [5, 6]]
lst4 = lst3.copy()
print(lst4)

#set
x = {1, 2, 3}
y = set()
print(y)

string = 'jdshbfuehiwuehc'
x = set(string)
print(x)
a = {}
print(type(a))
a['one'] = 1

lst = [1, 2, 3, 4, 5, 5]
lst2 = [5, 4, 3, 2, 1]
print(set(lst) == set(lst2)) #порівняння списків
print(len(set(lst)))

lst = [1, 2, 3, 4, 5, 5]
print(11 in lst)

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 6}
s3 = s1.copy()
print(s1.isdisjoint(s2))
print(s1 == s2)
print(s1 == s3)
print(s1.union(s2))
print(s2.difference(s1))
#s1.remove(5)
#print(s1)
#s1.discard(2)
s2 = frozenset(s1)
#s2.delete(1)
print(s2)
"""
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

dc = {'one': 1, 'two': 2, 'three': 3}
print(dc.items())
# збільшення ключів на 1
for key, value in dc.items():
    dc[key] = value + 1
print(dc)

keys = ['one', 'two', 'three']
values = [1, 2, 3]

x = list(zip(keys, values))
x = dict(zip(keys, values))
#print(x['one'])
print(x)
x['four'] = 4
print(x)
print(x.get('five')) #без помилки
#print(x['five']) #з помилкою для контроля данних
x.copy()
import copy
copy.deepcopy(x)

keys = ['one', 'two', 'three']
values = [1, 2, 3]

x = list(zip(keys, values))
x = dict(zip(keys, values))
print(x)
y = x.pop('three')
print(x)
print(y)

dictionary = dict(zip(keys, values))
another_dict = {'four': 4, 'five': 5}
dictionary.update(another_dict)
print(dictionary)

for i in range(10):
    print(i)
words = ['one', 'two', 'three']
for x in words:
    print(x)

for obj in zip(keys, values):
    print(obj)