import operator
import random
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
    
    
    return fitnessPopulacao, int(tamanhoPermuta)

### adicionando ranking dos individuos por meio do fitness
def addRankingAndSort(dictIndividuos):
    ############ORDENAÇAO E METODO DA ROLETA PARA SELECIONAR OS PAIS ###############
    sortedDictFit = sorted(dictIndividuos.items(), key=operator.itemgetter(1))
    #pegar cada indivíduo e fazer 1/distanciatotaldelemsm e dps escolher de dois em dois e formar os pais 
    for cont,itemlist in enumerate(sortedDictFit):
        sortedDictFit[cont] += (1/itemlist[1],)
    ###ADICIONANDO A LISTA DOS PAIS O VALOR DO RANKING DOS MESMOS
    #adicionando teste
    return sortedDictFit


def cruzamento(paiCandidato1, paiCandidato2, probMutacao, DicpontosCartesianos):
    listaPai1=paiCandidato1.split()
    listaPai2=paiCandidato2.split()
    tamanhoPais = len(listaPai1)+len(listaPai2)
    novaPopulacao = []
    pontoCorteMid = tamanhoPais//2

    for i in range(0, tamanhoPais):
        filho1 = listaPai1[0:pontoCorteMid]+listaPai2[pontoCorteMid:len(listaPai2)]
        filho2 = listaPai2[0:pontoCorteMid]+listaPai1[pontoCorteMid:len(listaPai1)]
        filho1 = mutacao(filho1, probMutacao)
        filho2 = mutacao(filho2, probMutacao)
        novaPopulacao.append(filho1)
        novaPopulacao.append(filho2)
    novaPopulacao = fitness(len(novaPopulacao),novaPopulacao,DicpontosCartesianos)
    return novaPopulacao


    

################## MUTAÇÃO DOS FILHOS #####################
def mutacao(filho, probMutacao):
    #minha taxa é apenas um float aleatorio
    taxa = random.uniform(0.0, 1.0)
    if taxa < probMutacao:
        index1 = random.randint(0, len(filho)-1)
        index2 = random.randint(0, len(filho)-1)
        filho[index1], filho[index2] = filho[index2], filho[index1]
    
    return filho