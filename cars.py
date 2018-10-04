# 组织列表
# 1.使用方法sort()对列表进行永久性排序 按照字母表顺序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# 与字母表相反顺序排序
cars.sort(reverse=True)
print(cars)

# 2. 使用函数sorted()对列表进行临时排序 按照字母表顺序排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))
print("\n Here si the original list again:")
print(cars)

# 3.倒着打印列表  reverse() 永久性地修改列表元素地排列顺序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 4. 确定列表地长度 len()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))







