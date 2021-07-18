import random
import time

AUTOFILLING = True


class matrix():

    def __init__(self, lines, columns):

        self.columns = columns
        self.lines = lines

        self.matrix = [[0] * self.columns for i in range(lines)]

        self.fill()
        self.show()
        time.sleep(1)

    def input(self):
        for i in range(self.lines):
            for j in range(self.columns):
                print('A[', i, '][', j, '] = ', sep='', end='')
                self.matrix[i][j] = int(input())

    def show(self):
        print()
        print("+", (self.columns) * "-------+", sep='')
        for i in range(self.lines):
            for j in range(self.columns):
                print("|", '{:^6.0f}'.format(self.matrix[i][j]), end='')
            print("|\n", end='')
        print("+", (self.columns) * "-------+", sep='')

    def transpon(self):
        if self.columns == self.lines:
            for i in range(self.lines):
                for j in range(i + 1, self.columns):
                    tmp = self.matrix[i][j]
                    self.matrix[i][j] = self.matrix[j][i]
                    self.matrix[j][i] = tmp
        else:
            print("\n[!] You cant transpon non-sqare matrix")

    def fill_random(self, start=- 100, end=100):
        for i in range(self.lines):
            for j in range(self.columns):
                self.matrix[i][j] = random.randrange(start, end)
        print("matrix filled random numbers")

    def fill(self):
        if AUTOFILLING:
            self.fill_random()
        else:
            self.input()


def q_1():
    A = matrix(5,5)

    for i in range(5):
        for j in range(5):
            if i > j:
                A.matrix[i][j] = 0
            elif i != j:
                A.matrix[i][j] = 3
    A.show()


def q_2():
    A = matrix(3,5)

    sum = 0
    for i in range(3):
        for j in range(5):
            if A.matrix[i][j] > 0:
                sum = sum + A.matrix[i][j]

    print('sum is ', sum)


def q_3():
    A = matrix(3,3)

    pos_count = 0
    for i in range(3):
        for j in range(3):
            if A.matrix[i][j] > 0:
                pos_count += 1

    print('Positive numbers is ', pos_count)


def q_4():
    A = matrix(3,5)

    prod = 1
    for i in range(3):
        for j in range(5):
            if A.matrix[i][j] > 0:
                prod *= A.matrix[i][j]

    print('producton of positive numbers is ', prod)


def q_5():
    A = matrix(4,3)

    count_degreess_one = 0
    for i in range(4):
        for j in range(3):
            if A.matrix[i][j] > 1:
                count_degreess_one += 1

    print('count degrees one is ', count_degreess_one)


def q_6():
    A = matrix(5,5)

    prod = 1
    for i in range(5):
        prod *= A.matrix[i][i]

    print('Production element of main diagonal is ', prod)


def q_7():
    A = matrix(4,4)

    count = 0
    for i in range(4):
        for j in range(4):
            if A.matrix[i][j] < 0:
                count += 1

    print('Count of element below zero is ', count)


def q_8():
    B = matrix(5,5)
    C = []

    for i in range(5):
        C.append(B.matrix[i][i])

    print('C is ', C)


def q_9():
    A = matrix(5,5)

    count = 0
    for i in range(1, 5):
        for j in range(i):
            if A.matrix[i][j] > 0:
                count += 1

    print('Count of positive elements below main dialonal is', count)


def q_10():
    A = matrix(3,3)

    sum = 0
    for i in range(3):
        for j in range(3):
            if A.matrix[i][j] < 0:
                sum += A.matrix[i][j]

    print('Sum of negative elements is ', sum)


def q_11():
    A = matrix(5,5)

    min = A.matrix[0][0]
    for i in range(0, 5, 2):
        for j in range(5):
            if A.matrix[i][j] < min:
                min = A.matrix[i][j]

    print('Min element is ', min)


def q_12():
    A = matrix(5,5)

    B = []

    for j in range(5):
        max = A.matrix[0][j]
        for i in range(1, 5):
            if A.matrix[i][j] > max:
                max = A.matrix[i][j]
        B.append(max)

    print('B is ', B)


def q_13():
    A = matrix(5,5)

    prod = 1
    count = 0
    for i in range(1, 5, 2):
        if A.matrix[i][4 - i] > 0 and (A.matrix[i][4 - i] % 2) == 0:
            prod *= A.matrix[i][4 - i]
            count += 1

    if count:
        print('Production of the right ones elements is ', prod)
    else:
        print('There is no the right ones elemtnts')


def q_14():
    A = matrix(7,7)

    max = A.matrix[0][0]

    for i in range(7):
        for j in range(6 - i):
            if A.matrix[i][j] > max:
                max = A.matrix[i][j]

    print('max element above side diagonal is ', max)


def q_15():
    A = matrix(7,7)

    max = A.matrix[1][6]

    for i in range(1, 7):
        for j in range(7 - i, 7):
            if A.matrix[i][j] > max:
                max_i = i
                max_j = j
                max = A.matrix[i][j]

    for i in range(7):
        A.matrix[i][max_j], A.matrix[max_i][i] = A.matrix[max_i][i], A.matrix[i][max_j]

    A.show()

    print('max element below side diagonal is ', max)


def q_16():
    A = matrix(5,5)

    print("How you want to sort?")
    print('[1] descending order')
    print('[2] ascending order')
    try:
        choose = int(input('My choose is - '))
    except ValueError:
        print('¯\_(ツ)_/¯ ')
        return 0

    if choose == 1:
        for i in range(5):
            for k in range(5):
                for j in range(4):
                    if A.matrix[i][j] > A.matrix[i][j + 1]:
                        A.matrix[i][j], A.matrix[i][j + 1] = A.matrix[i][j + 1], A.matrix[i][j]
    elif choose == 2:
        for i in range(5):
            for k in range(5):
                for j in range(4):
                    if A.matrix[i][j] < A.matrix[i][j + 1]:
                        A.matrix[i][j], A.matrix[i][j + 1] = A.matrix[i][j + 1], A.matrix[i][j]
    else:
        print('¯\_(ツ)_/¯ ')
        return 0

    A.show()


def q_17():
    A = matrix(6,6)

    B = []

    for i in range(5):
        for j in range(5):
            tmp = A.matrix[i][j]
            A.matrix[i][j] = ''
            for k in range(5):
                if tmp in A.matrix[k]:
                    B.append(tmp)
    try:
        max = B[0]
    except IndexError:
        print("There is no reapiting values")
        return 0

    for i in range(len(B)):
        if B[i] > max:
            max = B[i]

    print('Max is ', max)


def q_18():
    A = matrix(8,8)

    for i in range(8):
        min = A.matrix[i][0]
        for j in range(1, 8):
            if A.matrix[i][j] < min:
                min = A.matrix[i][j]
        print('minimum element in string', i + 1, 'is', min)


def q_19():
    A = matrix(7,7)

    max = A.matrix[0][0]

    for i in range(7):
        if A.matrix[i][i] > max:
            max_i = i
            max_j = i
            max = A.matrix[i][i]

    for i in range(7):
        if A.matrix[i][6 - i] > max:
            max_i = i
            max_j = 6 - i
            max = A.matrix[i][6 - i]

    A.matrix[max_i][max_j] = A.matrix[3][3]
    A.matrix[3][3] = max

    A.show()


def q_20():
    A = matrix(8,8)

    for i in range(8):
        max = A.matrix[i][0]
        for j in range(1, 8):
            if A.matrix[i][j] > max:
                max = A.matrix[i][j]
        print('maximum element in string', i + 1, 'is', max)


def q_21():
    A = matrix(4,4)

    count = 0
    for i in range(3):
        for j in range(i + 1, 4):
            if A.matrix[i][j] == 0:
                count += 1

    print("Count of element equal zero is ", count)


def q_22():
    A = matrix(4,4)

    sum_of_negative = 0
    count_of_negative = 0

    for i in range(4):
        for j in range(4):
            if A.matrix[i][j] < 0:
                sum_of_negative += A.matrix[i][j]
                count_of_negative += 1

    if count_of_negative != 0:
        print('Arithmetic mean is ', sum_of_negative / count_of_negative)
    else:
        print('There is no negative velues')


def q_23():
    A = matrix(4,3)

    B = A.matrix

    print('B is', B)


def q_24():
    A = matrix(3,3)

    count = 0
    for i in range(3):
        for j in range(3):
            if A.matrix[i][j] == 0:
                count += 1

    print('Count of element equal zero is ', count)


def q_25():
    A = matrix(5,5)

    for i in range(5):
        A.matrix[i][i] = 0

    A.show()


def Intro():
    print("""
    ПРАКТИКА ПО ИТ.

    1)Дана матрица А(5,5). Все элементы ниже главной диагонали обнулить, выше - заменить на "3".

    2)Найти сумму положительных элементов матрицы А(3,5).

    3)В матрице А(3,3) найти количество нулевых элементов.

    4)В матрице А(3,5) найти произведение положительных элементов.

    5)В матрице А(4,3) необходимо определить количество элементов, больших еденицы.

    6)Найти произведение элементов главной диагонали матрицы А(5,5).

    7)Найти количество отрицательных элементов матрицы А(4,4).


    8)Переписать элементы главной диагонали матрицы В(5,5) в одномерный массив С(5).

    9)Найти количество положительных элементов,расположенных под главной диагональю матрицы А(5,5).

    10)Найти сумму отрицательных элементов матрицы А(3,3).

    11)Дан массив А(5,5).Найти минимальный элемент среди элементов, расположенных в нечетных строках массива.

    12)Дан массив А(5,5).Построить массив В(5) по следующему правилу: 
    B(J) присвоить максимальный элемент J- столбца массива А.

    13)Дан массив А(5,5). Найти произвдение и количество четных положительных
    элементов побочной диагонали соответствующих строк

    14)Дан массив А(7,7). Найти максимальный элемент среди элементов, расположенных выше побочной диагонали.

    15)Дан массив А(7,7). Найти максимальный элемент расположенный ниже побочной диагонали. 
    Поменять местами элементы строки и столбца, на пересечении которых находится максимальный элемент.

    16)Дан массив А(5,5). Упорядочить элементы массива построчно.

    17)Дан массив А(6,6). Найти максимум среди элементов повторившихся более одного раза.

    18)Дан массив А(8,8). Найти максимальный элемент среди элементов строк.

    19)Дан Массив А(7,7). Найти наибольший элемент среди стоящих на главной и побочной диагоналях и поменять
    его местами с элементом, стоящим на пересечении этих диагоналей.

    20)Дан массив А(8,8). Найти минимальный элемент среди элементов строк.

    21)Найти количество нулевых элементов матрицы А(4,4), расположенных над главной диагональю.

    22)Найти среднее арифметическое отрицательных элементов матрицы А(4,4)

    23)Дан массив А(4,3). Переписать все ее элементы в вектор В.

    24)В матрице А(3,3) найти количество нулевых элементов.

    25)Дан массив А(5,5). Заменить нулями все ее элементы, расположенные на главной диагонали.
    """)


def main():
    global AUTOFILLING
    Intro()
    while True:
        choose = int(input("What you want? "))
        if choose == 0:
            break
        if choose == 1:
            q_1()
        if choose == 2:
            q_2()
        if choose == 3:
            q_3()
        if choose == 4:
            q_4()
        if choose == 5:
            q_5()
        if choose == 6:
            q_6()
        if choose == 7:
            q_7()
        if choose == 8:
            q_8()
        if choose == 9:
            q_9()
        if choose == 10:
            q_10()
        if choose == 11:
            q_11()
        if choose == 12:
            q_12()
        if choose == 13:
            q_13()
        if choose == 14:
            q_14()
        if choose == 15:
            q_15()
        if choose == 16:
            q_16()
        if choose == 17:
            q_17()
        if choose == 18:
            q_18()
        if choose == 19:
            q_19()
        if choose == 20:
            q_20()
        if choose == 21:
            q_21()
        if choose == 22:
            q_22()
        if choose == 23:
            q_23()
        if choose == 24:
            q_24()
        if choose == 25:
            q_25()
        if choose == 100:
            AUTOFILLING = not AUTOFILLING
            print(AUTOFILLING)


if __name__ == '__main__':
    main()

