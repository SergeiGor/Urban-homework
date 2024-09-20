from inspect import getmodule

def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': obj.__dict__,
        'methods': dir(obj),
        'module': getmodule(obj).__name__
    }
class Mycl:
    def __init__(self, a, b):
        self.a = a
        self.b = b

obj = Mycl(2,3)     # Создание объекта класса с атрибутами

print(introspection_info(obj))
