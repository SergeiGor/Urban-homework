
def print_params(a = 1, b = 'строка', c = True):

    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print('Ура! Функция принемает любые параметры.')
print()

values_list = [10,'двадцать',True]
print('список:',values_list)

print_params(*values_list)
print()

values_dict = {'a':11,'b':'стр','c':False}
print('словарь:',values_dict)

print_params(**values_dict)
print()

values_list_2 = ['первый',22]
print_params(*values_list_2, 42)