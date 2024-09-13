def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res > 1:
            if all((res % i != 0) for i in range(2, int(res ** 0.5) + 1)):
                return "Простое"
            else:
                return "Составное"
    return wrapper
@is_prime
def sum_three(a, b, c):
    summa = a + b + c
    print(summa)
    return summa

result = sum_three(2, 3, 6)

print(result)