def multiplicar_unaescala(mat):
    m3 =[]
    
    for i in range(len(mat)):
        m3.append([])
        for j in range(len(mat[0])):
            m3[i].append(0)
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for x in range(len(mat)):
                if mat[i][x] == 1 and mat[x][j] == 1:
                    m3[i][j]=1
    
    for i in range(len(m3)):
        for j in range(len(m3[0])):
            print(m3[i][j])

    return m3
   

def Peru():
    matriz=[[0,1,1,1,1,0,1,1,1],
            [1,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0],
            [1,0,0,0,0,1,0,0,1],
            [1,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,1,0,0],]
    
    a = multiplicar_unaescala(matriz)
     
print('Hi')
Peru()