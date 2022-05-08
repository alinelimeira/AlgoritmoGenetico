import random
import itertools 
from random import sample
import operator

### FUNÇÕES

######Calcular o FITNESS/APTIDAO (DISTANCIA) 1/distTotal DA POPULAÇÃO INICIAL, POR MEIO DA ROLETA ###############
#passar a populacao incial para o fitness
def fitness (tamanhoPermuta, rotas, DicpontosCartesianos): 
    fitnessPopulacao = {}
    populacao = []
    for count in range(0,tamanhoPermuta):
        populacao.append('R'+"".join(rotas[count])+'R')
    
    for count2,r in enumerate(populacao):
        distancia = 0
        for index in range(len(r)-1): 
            distancia += abs(DicpontosCartesianos[r[index+1]][0] - DicpontosCartesianos[r[index]][0]) + abs(DicpontosCartesianos[r[index+1]][1] - DicpontosCartesianos[r[index]][1])
        fitnessPopulacao[" ".join(r[1:-1])] = distancia
    print(len(fitnessPopulacao))
    
    return fitnessPopulacao, int(tamanhoPermuta)

### adicionando ranking dos individuos por meio do fitness
def addRanking(dictIndividuos):
    paisFitness = []   
    ############ORDENAÇAO E METODO DA ROLETA PARA SELECIONAR OS PAIS ###############
    sortedDictFit = sorted(dictIndividuos.items(), key=operator.itemgetter(1))
    #pegar cada indivíduo e fazer 1/distanciatotaldelemsm e dps escolher de dois em dois e formar os pais 
    for cont,itemlist in enumerate(sortedDictFit):
        paisFitness.append( 1 / itemlist[1]) 
    ###ADICIONANDO A LISTA DOS PAIS O VALOR DO RANKING DOS MESMOS
    #adicionando teste

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
    populacaodisponivel =  permutacaoPopulacao
    randomPickup = random.choice(populacaodisponivel)
    if randomPickup not in populacaoAmostra:
        populacaoAmostra.append(randomPickup)
    else:
        contador -= 1
        pass
    contador += 1

print(populacaoAmostra)
distanciasAmostraInicial = fitness(len(populacaoAmostra), populacaoAmostra, DicpontosCartesianos)
dictFitness = distanciasAmostraInicial[0]
dictLen = distanciasAmostraInicial[1]

addRanking(dictFitness)







################## MUTAÇÃO DOS FILHOS #####################















