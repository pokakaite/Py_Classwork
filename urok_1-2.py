smth = 1
smth1 = "asd"
smth2 = True
smth3 = 4.0

print(type(smth), type(smth1), type(smth2), type(smth3)) # <class 'int'> <class 'str'> <class 'bool'> <class 'float'>

print(smth, smth1, smth2, smth3, sep='')
print(smth, smth1, smth2, smth3, sep=' ')

print(smth, end='') #1asd
print(smth1, end='\n')
print(smth2, end='\t')
print(smth2, end='\n') #True

print(0o123) #восьмиричная система
print(0x123) #шестнадцатиричная система
print(0o123 + 0x123) #374

var = .14
var1 = 1.14

print(var1 - var)
print("{} - {}".format(var, var1))
print(f"{var} - {var1}")  #лучше использовать этот вариант
print(True + True * False)