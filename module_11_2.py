from inspect import isgenerator, isgeneratorfunction, ismethodwrapper, istraceback
import inspect
help(inspect)

class Introspection():

    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        pass

number_info = Introspection(42)
print(number_info)
print(dir(number_info))
print(isinstance('obj', int))
print(hasattr(number_info, 'obj'))
print(hasattr(number_info, 'x'))
print(getattr(number_info, 'obj'))
print(setattr(number_info, 'obj', 10))
print(number_info.obj)
print(type(number_info.obj))
print(isgenerator('obj'))  #является ли генератором
print(isgeneratorfunction('obj')) #является ли данное значение функцией генератора
print(ismethodwrapper('obj')) #является ли оберткой
print(istraceback('obj')) #
number_info = Introspection("Солнце")
print(isinstance("Солнце", str))
print(isinstance("Солнце", int))
print(getattr(number_info, 'obj'))
print(hasattr(number_info, 'obj'))
print(setattr(number_info, 'obj', 'эхо'))
print(number_info.obj)