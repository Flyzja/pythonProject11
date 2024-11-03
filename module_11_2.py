from inspect import isgenerator, isgeneratorfunction, ismethodwrapper, istraceback
import inspect

help(inspect)


def introspection_info(obj):
    result = {}
    result['type'] = type(obj)
    result['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr, 'Атрибут не найден'))]
    result['methods'] = [method for method in dir(type(obj)) if callable(getattr(obj, method))]
    result['module'] = inspect.getmodule(introspection_info)
    result['method'] = [m for m in inspect.getmembers(obj, predicate=inspect.isfunction)]
    return result


number_info = introspection_info(42)
print(number_info)

str_info = introspection_info('42')
print(str_info)

dict_info = introspection_info({'имя': 'Иван', 'возраст':  '45', 'профессия': 'механизатор'})
print(dict_info)

list_info = introspection_info(['Иван', 45, 32.08, (True, None), False])
print(list_info)



print(dir(number_info))
print(isinstance('obj', int))
print(hasattr(str_info, '42'))
print(hasattr(number_info, 'x'))

print(vars(introspection_info)) #возвращает словарь из атрибута dict
print(callable(introspection_info)) #является ли объект вызываемым
print(inspect.getmembers((introspection_info)))


print(isgenerator('obj'))  #является ли генератором
print(isgeneratorfunction(dict_info)) #является ли данное значение функцией генератора
print(ismethodwrapper(introspection_info)) #является ли оберткой
print(istraceback(introspection_info)) #обратная связь
number_info = introspection_info("Солнце")
print(isinstance("Солнце", str))
print(isinstance("Солнце", int))
