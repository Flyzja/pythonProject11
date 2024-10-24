import pandas as pd     # Импортируем библиотеку Pandas.
import numpy as np
import matplotlib.pyplot as plt

series_example = pd.Series([3, -8, 6, 1])     # Создаём объект Series, содержащий числа.
print('СОЗДАЛИ ОБЪЕКТ Series: ')
print(series_example)                          # Выводим объект на экран.

seasons = {'время года': ['зима', 'весна', 'лето'],
        'месяцы': [('декабрь', 'январь', 'февраль'), ('март', 'апрель', 'май'), ('июнь', 'июль', 'август')],
        'праздники': [('31', '1-8', '22, 23'), ('8, 9', '-', '1-4, 8-11'), ('12-15', '-', '-')]} # Создаём словарь с нужной информацией о временах года.

df = pd.DataFrame(seasons)  # Превращаем словарь в DataFrame, используя стандартный метод библиотеки.
print('ПРЕВРАЩАЕМ В СЛОВАРЬ  DataFrame: ')
print(df)

new_season = {'время года': 'осень', 'месяцы': ('сентябрь', 'октябрь', 'ноябрь'), 'праздники': ('-', '-', '2-4')}
df1 = pd.DataFrame([new_season])
new_list1 = pd.concat([df, df1])  # добавляем информацию
print('ДОБАВИЛИ: ')
print(new_list1)

new_list1.to_csv('file 5.txt', sep='\t', encoding='utf-8') # записываем в файл


new_list1 = pd.read_fwf('file 5.txt', delimiter='\n')   # читаем из файла
print('ЧИТАЕМ ИЗ ФАЙЛА: ')
print(new_list1)

new_list1 = pd.read_table('file 5.txt')       # читаем из файла
print('ЧИТАЕМ ИЗ ФАЙЛА: ')
print(new_list1)

a = np.array([1, 2, 3, 4, 5]) # массив из списка
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # двумерный массив из списка списков
c = np.arange(0, 10, 2)    # массив из диапазона значений
d = np.linspace(0, 1, 5) # массив из равномерно распределённых значений
e = np.random.rand(3, 3) #  массив из случайных значений
f = np.zeros((2, 3)) # массив из нулей
g = np.ones((3, 3))   # массив из единиц

print(a, b, c, d, e, f, g)

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
print("Array : " + str(array))
n = array.size
N = 4
M = n//N
reshaped1 = array.reshape((N, M))
print("Первый измененный Массив : ")
print(reshaped1)
reshaped2 = np.reshape(array, (2, 8))
print("Второй измененный Массив : ")
print(reshaped2)

array = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print("3-D массив : ")
print(array)

reshaped = array.reshape((9))
print("измененный массив 1-D : ")
print(reshaped)

first_array = np.array([1, 3, 5, 7])
second_array = np.array([2, 4, 6, 8])

#  + ператор
result1 = first_array + second_array
print("+ оператор:", result1)

# add() функция
result2 = np.add(first_array, second_array)
print("add() функция:", result2)

first_array = np.array([3, 9, 27, 81])
second_array = np.array([2, 4, 8, 16])

#  - оператор
result1 = first_array - second_array
print(" - оператор:", result1)

#  subtract() функция
result2 = np.subtract(first_array, second_array)
print("subtract() функция:", result2)

first_array = np.array([1, 3, 5, 7])
second_array = np.array([2, 4, 6, 8])

#  * оператор
result1 = first_array * second_array
print("* оператор:", result1)

#  multiply() function
result2 = np.multiply(first_array, second_array)
print("multiply() функция:", result2)

first_array = np.array([1, 2, 3])
second_array = np.array([4, 5, 6])

#  / оператор
result1 = first_array / second_array
print("/ оператор:", result1)

# divide() функция
result2 = np.divide(first_array, second_array)
print("divide() функция:", result2)

# инициализация данных
x = [40, 30, 20, 10]
y = [25, 28, 20, 15]

# построение графика данных
plt.plot(x, y)

# Добавление заголовка к сюжету
plt.title("Символ строки")

# Добавление метки по оси y
plt.ylabel('Ось Y')

# Добавление метки по оси x
plt.xlabel('Ось X')

plt.plot(x, y, color='violet', marker='o', markersize=10)

plt.show()


x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]

plt.bar(x, y, label='Величина прибыли', alpha=0.3) #Параметр label позволяет задать название величины для легенды
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.plot(x, y, color='black')
plt.show()


vals = [72, 17, 38, 21, 35]
labels = ["кражи", "грабежи", "мошенничества", "разбои", "вымогательства"]

plt.pie(vals, labels=labels, autopct='%1.1f%%')
plt.title("соотношение видов хищения")
plt.show()

