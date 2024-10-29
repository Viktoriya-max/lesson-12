#Распаковка позиционных параметров
    #1.Функция с параметрами по умолчанию:

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

#Функция с разным количеством аргументов:

print_params()
print_params({1})
print_params(3, 5)
print_params([1, 3],'b',False)

print_params(b = 25)
print_params(c = [1, 2, 3])

    #2.Распаковка параметров:

values_list = [False, [3, 4, 2], 'ХаХа'] #Распаковка списка
print_params(*values_list)

values_dict = {'a' : (True, 1), 'b' : 54, 'c' : 'НеНе'} #Распаковка словаря
print_params(**values_dict)

    #Распаковка + отдельные параметры:
values_list_2 = [1.45, 'help']
print_params(*values_list_2, 42)



