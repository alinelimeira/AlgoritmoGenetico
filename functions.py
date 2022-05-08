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
def addRankingAndSort(dictIndividuos):
    ############ORDENAÇAO E METODO DA ROLETA PARA SELECIONAR OS PAIS ###############
    sortedDictFit = sorted(dictIndividuos.items(), key=operator.itemgetter(1))
    #pegar cada indivíduo e fazer 1/distanciatotaldelemsm e dps escolher de dois em dois e formar os pais 
    for cont,itemlist in enumerate(sortedDictFit):
        sortedDictFit[cont] += (1/itemlist[1],)
    ###ADICIONANDO A LISTA DOS PAIS O VALOR DO RANKING DOS MESMOS
    #adicionando teste
    return sortedDictFit
