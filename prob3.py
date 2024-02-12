from functools import reduce
def my_func(my_list, my_lambda):
    return reduce(my_lambda, my_list)
test_list = [1,3,5,2,7,4]
test_lambda = lambda x, y: x if x > y else y
print(my_func(test_list, test_lambda))