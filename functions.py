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
            distancia += (abs(DicpontosCartesianos[r[index+1]][0] - DicpontosCartesianos[r[index]][0]) + abs(DicpontosCartesianos[r[index+1]][1] - DicpontosCartesianos[r[index]][1]))
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
    return novaPopulacao[0]


    

################## MUTAÇÃO DOS FILHOS #####################
def mutacao(filho, probMutacao):
    #minha taxa é apenas um float aleatorio
    taxa = random.uniform(0.0, 1.0)
    if taxa < probMutacao:
        index1 = random.randint(0, len(filho)-1)
        index2 = random.randint(0, len(filho)-1)
        filho[index1], filho[index2] = filho[index2], filho[index1]
    return filho


################# AJUSTE POPULACIONAL ######################
def ajustePopulacional(populacao, tamanhoPopulacao):
    while len(populacao) > tamanhoPopulacao:
        tam = len(populacao)
        individuo1 = random.randint(0, tam-1)
        individuo2 = random.randint(0, tam-1)
        if individuo1 != individuo2:
            if populacao[individuo1][individuo1][2] < populacao[individuo2][individuo2][2]:
                populacao.remove(populacao[individuo2])
            else:
                populacao.remove(populacao[individuo1])
    
    return populacao


############# ALGORITMO GENETICO ##########################
def algoritmoGenetico(tamanhoListas,resultado_geracoes,probMutacao,DicpontosCartesianos,tamanhoPopulacao):
    #primeiramente eu tenho que tratar minha lista de listas para somente 1 lista por vez
    for cont_listas in range(0,tamanhoListas):
        tamanho_amostra_geracoes = len(resultado_geracoes[cont_listas])
        lista_amostra_geracoes = resultado_geracoes[cont_listas]
        pais_geracao = []
        valor_daquela_geracao = []
        ### cruzamento das amostras inciais, taxa de cruzamento 
        limiteCruzamento = True
        if  (len(lista_amostra_geracoes) > 0.3*tamanho_amostra_geracoes) and limiteCruzamento: 
            pai1 = random.choice(lista_amostra_geracoes)
            pai2 = random.choice(lista_amostra_geracoes)
            if pai1 in pais_geracao:
                lista_amostra_geracoes.remove(pai1)
            else:
                pass
            if pai2 in pais_geracao:
                lista_amostra_geracoes.remove(pai2)
            else:
                pass
            pais_geracao.append(cruzamento(pai1[0],pai2[0],probMutacao,DicpontosCartesianos))
            #print(pai1,"pai1", pai2,"pai2")
        else:
            limiteCruzamento = False

        #Fazendo o ajuste populacional nos novos pais, entao aqui na verdade eu elimino baseado no fitness
        for cont_interno in range(0,len(pais_geracao)):
            pais_geracao[cont_interno] = addRankingAndSort(pais_geracao[cont_interno])
        valor_daquela_geracao = ajustePopulacional(pais_geracao,tamanhoPopulacao)


    return valor_daquela_geracao