first_list = [1,2,3,4]
second_list = [2,4,5,6]
in_both = list(filter(lambda x: x in second_list, first_list))
print(in_both)