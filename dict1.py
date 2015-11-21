list1={
    'name':'tom',
    'age':18,
    'sex':'male'
}

print '#' * 70
print 'all items : ',list1.items()

print '#' * 70
print 'all keys : ',list1.keys()

print '#' * 70
print 'all values : ',list1.values()

print '#' * 70
for i  in list1.iterkeys():
    print 'keys(one key per-line) : ',i

print "#" * 70
for j in list1.itervalues():
    print 'values(one value per-line) : ',j

print "#" * 70
list2=range(0,20,3)
print list2
'''
print "#" * 70
list3 = list1.pop('name')
print list1
'''
print "#" * 70
list1.popitem()
print list1



