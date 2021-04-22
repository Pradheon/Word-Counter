Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> filepath = input("enter filepath: ")
file = open(filepath, "rt")
value_lines = 0
value_words = 0
value_chars = 0

for lines in file:
    value_lines += 1
    for words in lines.split():
        value_words += 1
        for chars in words:
            value_chars += 1
print (value_lines, '\n', value_words, '\n', value_chars)
enter filepath: 