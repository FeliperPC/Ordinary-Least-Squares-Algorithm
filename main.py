import math
from traceback import print_tb
import numpy

def multiplicaVet(v1,v2,pontos):
    newVet=['']*pontos
    for i in range(0,pontos):
        newVet[i]=float(v1[i])*float(v2[i])
    return newVet

def somatorioVet(vet,pontos):
    soma=0
    for i in range(0,pontos):
        soma += vet[i]
    return soma

def imprimeMatriz(m):
    for l in range(0,3):
        for c in range(0,4):
            print(f'[{m[l][c]}]',end ='')
        print()

def gauss(m):
    newM=[['']*4]*3
    #Linha 1 
    for i in range(0,4):
        newM[0][i] = m[0][i]

    #Linha 2 concluida
    newM[1]=m[1][0]-((m[1][0]/m[0][0])*m[0][0]),m[1][1]-((m[1][0]/m[0][0])*m[0][1]),m[1][2]-((m[1][0]/m[0][0])*m[0][2]),m[1][3]-((m[1][0]/m[0][0])*m[0][3])

    #Linha 3 Concluida
    newM[2]=m[2][0]-((m[2][0]/m[0][0])*m[0][0]),m[2][1]-((m[2][0]/m[0][0])*m[0][1]),m[2][2]-((m[2][0]/m[0][0])*m[0][2]),m[2][3]-((m[2][0]/m[0][0])*m[0][3])
    auxVet=[newM[2][0],newM[2][1],newM[2][2],newM[2][3]]

    newM[2]=auxVet[0],auxVet[1]-(auxVet[1]/newM[1][1])*newM[1][1],auxVet[2]-(auxVet[1]/newM[1][1])*newM[1][2],auxVet[3]-(auxVet[1]/newM[1][1])*newM[1][3]
    return (newM)

def resolverSistema(m):
    vetResult=['']*3
    vetResult[2]=m[2][3]/m[2][2] #z
    vetResult[1]=(m[1][3]-(m[1][2]*vetResult[2]))/m[1][1] #y
    vetResult[0]=(m[0][3]-(m[0][1]*vetResult[1])-(m[0][2]*vetResult[2]))/m[0][0]
    return vetResult

condition=False
while condition == False:
    vetLen = int(input("Digite a quantidade de pontos. (limíte 5) : ")) 
    if(vetLen<6 and vetLen>0): 
        condition = True 
    else:
        print("Digite um número de pontos válido !")

g1=[1]*vetLen
g2=['']*vetLen
g3=['']*vetLen

xi=['']*vetLen #vetor vazio dinâmico 
for i in range(0,vetLen):
    xi[i] = input("Digite o valor "+str(i)+"º do vetor xi: ")
    g2[i] = xi[i]
    g3[i]= pow(float(xi[i]),2)

fxi=['']*vetLen 
for i in range(0,vetLen):
    fxi[i] = input("Digite o valor "+str(i)+"º do vetor fxi: ")

print("Vetor xi: "+str(xi))   
print("Vetor fxi: "+str(fxi))
print("Vetor g1: "+str(g1))
print("Vetor g2: "+str(g2))
print("Vetor g3: "+str(g3)+"\n")

matriz=[['']*4]*3

matriz[0]=somatorioVet(multiplicaVet(g1,g1,vetLen),vetLen),somatorioVet(multiplicaVet(g1,g2,vetLen),vetLen),somatorioVet(multiplicaVet(g1,g3,vetLen),vetLen),somatorioVet(multiplicaVet(g1,fxi,vetLen),vetLen)
matriz[1]=somatorioVet(multiplicaVet(g2,g1,vetLen),vetLen),somatorioVet(multiplicaVet(g2,g2,vetLen),vetLen),somatorioVet(multiplicaVet(g2,g3,vetLen),vetLen),somatorioVet(multiplicaVet(g2,fxi,vetLen),vetLen)
matriz[2]=somatorioVet(multiplicaVet(g3,g1,vetLen),vetLen),somatorioVet(multiplicaVet(g3,g2,vetLen),vetLen),somatorioVet(multiplicaVet(g3,g3,vetLen),vetLen),somatorioVet(multiplicaVet(g3,fxi,vetLen),vetLen)

print("Matriz Montada\n")
imprimeMatriz(matriz)
print()
print("Matriz Escalonada\n")
imprimeMatriz(gauss(matriz))
print()
resultado=resolverSistema(gauss(matriz))
print("X: "+str(resultado[0])+"\nY: "+str(resultado[1])+"\nZ: "+str(resultado[2]))