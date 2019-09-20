# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
for letter in word.lower():
    if letter in 'аеёиоуыэюя':
        count += 1
print(count)



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
list = (sentence.split())
for list_index in list:
    print(list_index[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
print(int(len(sentence.replace(' ',''))/len(sentence.split())))

