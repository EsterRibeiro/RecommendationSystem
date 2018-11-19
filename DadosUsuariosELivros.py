avaliacoesUsuario = {'Lucas':
                  {'Neuromancer': 2.5,
                   'Frankenstein': 3.5,
                   'Nineteen Eighty-Four': 3.0,
                   'The Hitchhiker''s Guide to the Galaxy': 3.5,
                   'Androides Sonham com Ovelhas Elétricas?': 2.5,
                   'Fahrenheit 451': 3.0},

              'Ester':
                  {'Neuromancer': 3.0,
                   'Frankenstein': 3.5,
                   'Nineteen Eighty-Four': 1.5,
                   'The Hitchhiker''s Guide to the Galaxy': 5.0,
                   'Androides Sonham com Ovelhas Elétricas?': 3.0,
                   'Fahrenheit 451': 3.5},

              'Douglas':
                  {'Neuromancer': 2.5,
                   'Frankenstein': 3.0,
                   'Nineteen Eighty-Four': 3.5,
                   'The Hitchhiker''s Guide to the Galaxy': 4.0},

              'Gabryell':
                  {'Androides Sonham com Ovelhas Elétricas?': 3.5,
                   'Nineteen Eighty-Four': 3.0,
                   'Frankenstein': 4.5,
                   'Neuromancer': 4.0,
                   'Fahrenheit 451': 2.5},

              'Humberto':
                  {'Frankenstein': 3.0,
                   'Nineteen Eighty-Four': 4.0,
                   'Neuromancer': 2.0,
                   'The Hitchhiker''s Guide to the Galaxy': 3.0,
                   'Androides Sonham com Ovelhas Elétricas?': 3.0,
                   'Fahrenheit 451': 2.0},

              'Diego':
                  {'Nineteen Eighty-Four': 3.0,
                   'Frankenstein': 4.0,
                   'Neuromancer': 3.0,
                   'The Hitchhiker''s Guide to the Galaxy': 5.0,
                   'Fahrenheit 451': 3.5},

              'Patrick':
                  {'Nineteen Eighty-Four': 4.5,
                   'The Hitchhiker''s Guide to the Galaxy': 1.0,
                   'Neuromancer': 4.0}
              }

avaliacoesLivro = {'Neuromancer': 
		{'Lucas': 2.5, 
		 'Ester:': 3.0 ,
		 'Gabryell': 4.0, 
		 'Diego': 3.0, 
		 'Patrick': 4.0 },
	 
	 'Frankenstein': 
		{'Lucas': 3.5, 
		 'Ester': 3.5,
		 'Douglas': 3.0, 
		 'Gabryell': 4.5, 
		 'Humberto': 3.0, 
		 'Diego': 4.0 },
				 
	 'Nineteen Eighty-Four': 
		{'Lucas': 3.0, 
		 'Ester:': 1.5,
		 'Douglas': 3.5, 
		 'Gabryell': 3.0,
                 'Humberto': 4.0,
                 'Diego': 3.0,
                 'Patrick': 4.5 },
	
	 'The Hitchhiker''s Guide to the Galaxy': 
		{'Lucas': 3.5, 
		 'Ester:': 5.0 ,
		 'Douglas': 4.0, 
		 'Humberto': 3.0, 
		 'Diego': 5.0, 
		 'Patrick': 1.0 },
				 
	 'Androides Sonham com Ovelhas Elétricas?': 
		{'Lucas': 2.5, 
		 'Ester:': 3.0 ,
		 'Gabryell': 3.5, 
		 'Humberto': 3.0 },
				 
	 'Fahrenheit 451': 
		{'Lucas': 3.0, 
		 'Ester:': 3.5,
		 'Gabryell': 2.5, 
		 'Humberto': 2.0, 
		 'Diego': 3.5}
}


#função euclidiana

from math import sqrt
import matplotlib.pyplot as plt

def euclidiana(base, usuario_1, usuario_2):
    livros_comum = {} #verifica se há avaliacoes do mesmo filme entre os dois usuários

    for item in base[usuario_1]: #busca os livros que o usuário leu
        if item in base[usuario_2]: livros_comum[item] = 1 #verifica se os livros tbm estão no user 2

    if len(livros_comum) == 0: return 0 #tamanho da lista == 0 (não tem livros em comum)

    soma = sum([pow(base[usuario_1][item] - base[usuario_2][item], 2) #funcao euclidiana

        for item in base[usuario_1] if item in base[usuario_2]]) #pega todos os itens dentro dos dois usuários

    return 1/(1 + sqrt(soma)) #retorna o valor e porcentagem

#lista de usuários similares

def getSimilares(base, usuario):
    similaridade = [(euclidiana(usuario, outro), outro) #funcao euclidiana 
                    for outro in base if outro != usuario] #chama a lista de usuarios sem comparar com ele mesmo
    similaridade.sort()
    similaridade.reverse() 
    return similaridade # irá retornar a similaridade em ordem decrescente

#função de recomendação

def getRecomendacoes(base, usuario): #usuario a ser recomendado
    totais = {} #soma da multiplicação da similaridade pela nota do usuário em relação ao livro
    somaSimilaridade= {} #soma da similaridade dos filmes

    for outro in base:
        if outro == usuario: continue #não pode comparar a ele mesmo
        similaridade = euclidiana(base, usuario, outro)

        if similaridade <= 0: continue #deve haver similaridade

        for item in base[outro]: #percorre os itens
            if item not in base[usuario]: #o item não deve estar na lista de filmes que o usuário já assistiu
                totais.setdefault(item, 0) # acumulação da similaridade x a nota dada pelo usuário
                totais[item] += base[outro][item] * similaridade
                somaSimilaridade.setdefault(item, 0)
                somaSimilaridade[item] += similaridade
    rankings = [(total / somaSimilaridade[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
