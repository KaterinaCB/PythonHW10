# Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, максимум и среднее арифметическое последовательности целых чисел.
# Экземпляры классов инициализируются без аргументов. Метод add_number должен добавлять в статистику число, 
# которое будет учтено при вычислении финального результата методом result. Для экземпляров MinStat и MaxStat result должен возвращать целое число, 
# для AverageStat — число типа float (это число будет сравниваться с правильным ответом до седьмой значащей цифры).
# Если в последовательности отсутствуют числа и статистические величины вычислить невозможно, метод result должен возвращать None.

# class MinStat:
#     def __init__(self):
#         self.v = []
#  
#     def add_number(self, n):
#         self.v.append(n)
#  
#     def result(self):
#         if self.v == []:
#             return None
#         else:
#             return min(self.v)
 
 
# class MaxStat:
#     def __init__(self):
#         self.v = []
 
#     def add_number(self, n):
#         self.v.append(n)
 
#     def result(self):
#         if self.v == []:
#             return None
#         else:
#             return max(self.v)
 
 
# class AverageStat:
#     def __init__(self):
#         self.v = []
 
#     def add_number(self, n):
#         self.v.append(n)
 
#     def result(self):
#         if self.v == []:
#             return None
#         else:
#             n = len(self.v)
#             s = sum(self.v)
#             return s / n

# values = [1, 2, 4, 5]

# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


# Реализуйте класс Table, который хранит целые числа в двумерной таблице. 
# При инициализации Table(rows, cols) экземпляру передаются число строк и столбцов в таблице. Строки и столбцы нумеруются с нуля.
# table.get_value(row, col) — прочитать значение из ячейки в строке row, столбце col. Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.
# table.set_value(row, col, value) — записать число в ячейку строки row, столбца col. Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.
# table.n_rows() — вернуть число строк в таблице
# table.n_cols() — вернуть число столбцов в таблице
# table.delete_row(row) — удалить строку с номером row
# table.delete_col(col) — удалить колонку с номером col
# table.add_row(row) — добавить в таблицу новую строку с индексом row.
# Номера строк >= row, должны увеличиться на единицу. Новая строка состоит из нулей.
# table.add_col(col) — добавить в таблицу новую колонку с индексом col.
# Номера колонок >= col, должны увеличиться на единицу. Новая колонка состоит из нулей.

class Table(object):
 
    def __init__(self, rows, cols):
        self.field = [[0 for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols
 
    def get_value(self, row, col):
        if row in range(self.rows) and col in range(self.cols):
            return self.field[row][col]
        return
 
    def set_value(self, row, col, value):
        self.field[row][col] = value
 
    def n_rows(self):
        return self.rows
 
    def n_cols(self):
        return self.cols

tab = Table(3, 5)
tab.set_value(0, 1, 10)
tab.set_value(1, 2, 20)
tab.set_value(2, 3, 30)
for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()

tab.add_row(1)

for i in range(tab.n_rows()):
    for j in range(tab.n_cols()):
        print(tab.get_value(i, j), end=' ')
    print()
print()