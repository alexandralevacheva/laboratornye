import numpy as np
class result:
  global xs
  global res

#на вход матрица n1*n первые n*n-значения коэффециэнтов:1-ы1 столбец-1-ая строчка, последняя строчка - значения
#пример
#2x1+3x2-x3=9
#x1-2x2+x3=3
#x1+2x3=2
#kramer([
#        [2, 1, 1],
#        [3, -2, 0],
#        [-1, 1, 2],
#        [9, 3, 2]
#])
def kramer(a):
  vals=a[-1]
  ks=a[:-1]
  det=np.linalg.det(ks)
  if(det!=0):
    ks=[0 for i in range(len(a)-1)]
    for i in range(len(a)-1):
      ks[i]=a[:i]+[vals]+a[i+1:-1]
    ks=[np.linalg.det(i) for i in ks]
    ks=[i/det for i in ks]
    res=result()
    res.xs=ks
    res.res=1
    return res
  if(det==0):
    res=result()
    res.res=0
    return res
# --- перемена местами двух строк системы
def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]
# --- end of перемена местами двух строк системы

# --- деление строки системы на число
def DivideRow(A, B, row, divider):
    A[row] = [a / divider for a in A[row]]
    B[row] /= divider
# --- end of деление строки системы на число

# --- сложение строки системы с другой строкой, умноженной на число
def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight
# --- end of сложение строки системы с другой строкой, умноженной начисло

# --- решение системы методом Гаусса (приведением к треугольному виду)
def Gauss(A, B):
    column = 0
    while (column < len(B)):
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                 current_row = r
        if current_row is None:
            return None
        if current_row != column:
            SwapRows(A, B, current_row, column)
        DivideRow(A, B, column, A[column][column])
        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])
        column += 1
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    return X


a=int(input("Длина матрицы арументов = "))
print("Введите матрицу:")
arr=[[int(j) for j in input().split()] for i in range(a)]
res=[int(i)  for i in input("Введите результаты: ").split()]
print("Gauss = "+ " ".join([str(i) for i in Gauss(arr, res)]))
arr=[[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]
arr+=[res]
print("kramer = "+" ".join([str(i) for i in kramer(arr).xs]))
