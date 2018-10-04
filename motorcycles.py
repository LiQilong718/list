# 修改列表元素

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# 在列表中添加元素
# 1.在列表末尾添加元素 append()
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 2.在列表中插入元素 insert()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  # 方法insert()在索引0处添加空间，并将值'ducati'存储到这个地方。
print(motorcycles)

# 3.从列表中删除元素

# 01 使用del语句删除元素 永久删除，之后无法再访问
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# 02 使用方法pop()删除元素  pop 取出  pop()可删除列表末尾的元素，并让你能够接着使用它
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# 03 弹出列表中任何位置处的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycles I owned was a ' + first_owned.title() + '.')

# 04 根据值删除元素 remove() 也可接着使用它的值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+too_expensive.title()+" is too expensive for me.")

