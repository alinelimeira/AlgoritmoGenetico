import random
import itertools 
from random import sample
#importando as funcoes
from functions import addRankingAndSort, fitness


############## Leitura da matriz ##############
arquivo = open ("matriz.txt", "r")
tam_linha,tam_coluna = arquivo.readline().split() 
tam_linha,tam_coluna = int(tam_linha),int(tam_coluna)

linhas = arquivo.read().splitlines()
matriz = [] 
vertices = []
DicpontosCartesianos = {}

for i in range(len(linhas)):          
    matriz.append(linhas[i].split())  

arquivo.close()

for i in range(tam_linha):
    for j in range(tam_coluna):
        letra = matriz[i][j]
        if matriz[i][j] == 'R':
            DicpontosCartesianos[letra] = (i, j)
        elif matriz[i][j] != '0':
            DicpontosCartesianos[letra] = [i,j]  
            vertices.append(letra)
            
vertices= sorted(vertices)
#print("Aqui são os vertices", vertices, "dicpontos",DicpontosCartesianos)
#print(matriz)

########## Parametros do A.G ######################

criteriodeParada = 50 #(quantidade de gerações)
tamanhoPopulacao = 10
txReproducao= 70
probMutacao = 0.5

#Populacao inicial a partir de 10  tamanhoPopulacao

populacaodisponivel = []
populacaoAmostra = []

permutacaoPopulacao =  list(itertools.permutations(vertices)) #PERMUTAÇAO TOTAL
#EXCLUIR O ULTIMO ELEMENTO QUE JA FOI PEGADO
contador = 0
while contador < tamanhoPopulacao:
    randomPickup = random.choice(permutacaoPopulacao)
    if randomPickup not in populacaoAmostra:
        populacaoAmostra.append(randomPickup)
    else:
        contador -= 1
        pass
    contador += 1

distanciasAmostraInicial = fitness(len(populacaoAmostra), populacaoAmostra, DicpontosCartesianos)
dictFitness = distanciasAmostraInicial[0]
dictLen = distanciasAmostraInicial[1]

listaAmostraInicial = addRankingAndSort(dictFitness)

################## MUTAÇÃO DOS FILHOS #####################