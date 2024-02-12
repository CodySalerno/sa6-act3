my_strings = ["abd", "abc", "asdfasdfasd", "as"]
print(sorted(my_strings, key=lambda x: (len(x), x)))