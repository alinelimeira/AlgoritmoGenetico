import random
import itertools 
from random import sample
import time
start = time.time()
#importando as funcoes
from functions import addRankingAndSort, ajustePopulacional, algoritmoGenetico, fitness, cruzamento


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
#escolha aleatoria de 10 indivifuos, 
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
tamanhoAmostraInicial = dictLen
pais_1geracao = []
### cruzamento das amostras inciais, taxa de cruzamento 
limiteCruzamento = True
while limiteCruzamento:
    if  len(listaAmostraInicial) > 0.3*tamanhoAmostraInicial: 
        pai1 = random.choice(listaAmostraInicial)
        listaAmostraInicial.remove(pai1)
        pai2 = random.choice(listaAmostraInicial)
        listaAmostraInicial.remove(pai2)
        pais_1geracao.append(cruzamento(pai1[0],pai2[0],probMutacao,DicpontosCartesianos))
        #print(pai1,"pai1", pai2,"pai2")
    else:
        limiteCruzamento = False

#Fazendo o ajuste populacional nos novos pais, entao aqui na verdade eu elimino baseado no fitness
for cont_interno in range(0,len(pais_1geracao)):
    pais_1geracao[cont_interno] = addRankingAndSort(pais_1geracao[cont_interno])
novo_valor_pais = ajustePopulacional(pais_1geracao,tamanhoPopulacao)



# JA ESTA RODANDO A PARTIR DA 1 GERAÇÃO 
for cont_geracoes in range(criteriodeParada):
    resultado_geracoes = algoritmoGenetico(len(novo_valor_pais),novo_valor_pais,probMutacao,DicpontosCartesianos,tamanhoPopulacao)
    resultado = algoritmoGenetico(len(resultado_geracoes),resultado_geracoes,probMutacao,DicpontosCartesianos,tamanhoPopulacao)
print(f"O Menor caminho é: {resultado[0][0]}")

#QAUANDO EU CHAMO O ALGORITMO GENETICO ELE TEM QUE ME RESULTAR UMA LISTA TAL QUAL A LISTADEAMOSTRAINICIAL
end = time.time()
print(end - start)