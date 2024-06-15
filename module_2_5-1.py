def get_matrix():
    matrix = []
    n=int(input("задайте число строк:"))
    m=int(input("задайте число столбцов:"))
    print("матрица",m,"Х",n)
    for i in range(0, n):
        st = []
        matrix.append(st)
        print("заполняем строку",i+1)

        for i in range(0,m):
            value=input("введите значение")
            st.append(value)



    print("результат:",matrix)

get_matrix()