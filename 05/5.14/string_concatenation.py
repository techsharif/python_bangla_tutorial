str1 = "hello"
str2 = " world"
full_string = "hello world"
another_string = "hello world"
str3 = str1 + str2
print(str3==full_string)
print(id(str3))
print(id(full_string))
print(id(another_string))

