
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_pos = {}
    pos_str, pos_byte = 1, 0
    for i in strings:
        file.write(i+"\n")
        strings_pos[(pos_str,pos_byte)] = i
        pos_str += 1
        pos_byte = file.tell()
    file.close()
    return strings_pos


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)