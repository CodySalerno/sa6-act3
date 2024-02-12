from functools import reduce
my_num = 1234
result = reduce(lambda x, y: int(x) + int(y), str(my_num))
print(result)