def single_root_words(root_word,*other_words):
    same_words = []
    print("переданы слова:",other_words)
    n = len(other_words)
    print("всего слов:",n,"ищем среди них совпадения")
    print()
    for i in range(0,n):
        root_str = root_word.lower()
        other_str = (other_words[i]).lower()
        print(other_str)
        print(root_str)
        if root_str in other_str or other_str in root_str:
            same_words.append(other_words[i])
            print('совпадение!')
            print()
        else:
            print('совпадения нет')
            print()
    print("результат:")

    return same_words




result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)
