# pass do nothing
str1 = "a,b,c,d"
str2 = " "
for i in str1:
    if i == ",":
        pass
    else:
        str2 = str2 + i
print(str2)
