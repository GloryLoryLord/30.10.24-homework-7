my_dict = {'Department34': 1, 'EchoFrost': 2}
print(my_dict)
print(my_dict['Department34'], my_dict.get('Cancord'))
my_dict.update({'Neon': 3, 'Uprising': 4})
print(my_dict)
#del my_dict ['Uprising']
my_dict.pop('Uprising')
print(my_dict)

my_set = {1, 2, 3, 4, 3, 2, 1, True, True, 'str', 'str', 'any str'}
my_set = set(my_set)
print(my_set)
my_set.add( 777)
my_set.add(666)
print(my_set)
my_set.remove(4)
print(my_set)


