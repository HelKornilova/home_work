#Задание 1

def count_letter(list_, i):
    new_list = []
    for word in list_:
        if i in word:
            new_list.append(word)
    print(len(new_list))

count_letter(['трава', 'рост', 'дом', 'комп', 'трава', 'мост'], 'р')
