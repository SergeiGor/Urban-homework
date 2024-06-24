def get_multiplied_digits(number=0):
    str_number = str(number)
    first = int(str_number[0])
    # print('первая цифра',first)
    if len(str_number) <=1:
        return first
    nofirst = int(str_number[1:])

    res = get_multiplied_digits(nofirst)

    resul = first * res

    return resul




result = get_multiplied_digits(40203)
print(result)