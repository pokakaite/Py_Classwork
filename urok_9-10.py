st = "as"
print(st.encode("UTF-8")) ## просмотр кода. с цифрами не работает
print(st.encode("UTF-16"))

st = b'\xff\xfea\x00s\x00'
print(st.decode("UTF-16"))

st = r"Hello \n world"
print(st)

st = r"{str1}Hello \n world"
print(st)

st = f"Hello \n world"
print(st)

file = open(r"new\new.py", "r")
print(file)

st = '''"Hello world!"
"You are 'the' best" '''
print(id(st))
print(type(st))
print(st)

st = "re"

print(id(st))


st = '''Hello worLd!
\t You are 'the' best'''
# print(st[0:10])
# print(st[10:0:-1])
# print(st + st)
#
# print(len(st))
# l = ["sdf", "asf"]
# print(len(l))
#
# st = st.lower()
# print(st)
# print(st.capitalize()) # делает первую букву большой
# print(st.upper()) # делает все буквы большими
# print(st.title()) # делает первую букву каждого слова большой
# print(st.swapcase()) # меняет большие буквы на маленькие и наоборот

print(st.count("l")) # считает буквы
print(st.count("l", 0, 10)) # считает буквы в диапазоне

print(st.find("worLd", 0, 15)) # находит символ, с которого начинается слово (в диапазоне)
print(st.rfind("l", 0, 55))

print(st.startswith('H'))
print(st.endswith('"'))

print(st.isalnum())
print(st.isspace())

str1 = " \n \t"
print(str1.isspace())

print(st.center(150, " "))

print(st.expandtabs(tabsize=10)) # задаем размер для пробела

print(st.ljust(100, "*")) # заполняет символами

myStr = "    Python is cool   "
print(myStr.lstrip()) # убирает пробелы слева
print(myStr.rstrip()) # убирает пробелы справа
print(myStr.strip()) # убирает пробелы по бокам
myStr = "   @ Python is cool @   "
print(myStr.lstrip('@'))
print(myStr.rstrip('@'))
print(myStr.strip('@'))






