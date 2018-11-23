avaliacoesUsuario = {'Lucas':
                  {'O Guia do Mochileiro das Galáxias': 4.5,
                   'Orgulho e Preconceito': 1.6,
                   'Os Crimes do Monograma': 2.4},

              'Ester':
                  {'O Guia do Mochileiro das Galáxias': 5.0,
                   'Neuromancer': 4.2,
                   'A Culpa é das Estrelas': 3.0,
                   'Orgulho e Preconceito': 4.8,
                   'Os Crimes do Monograma': 3.0,
                   'Fortaleza Digital': 3.8},

              'Douglas':
                  {'O Guia do Mochileiro das Galáxias': 3.5,
                   'Neuromancer': 4.5,
                   'Orgulho e Preconceito': 2.1,
                   'Os Crimes do Monograma': 3.2},

              'Gabryell':
                  {'A Culpa é das Estrelas': 1.9,
                   'Orgulho e Preconceito': 2.5,
                   'Fortaleza Digital': 4.7},

              'Humberto':
                  {'O Guia do Mochileiro das Galáxias': 2.5,
                   'Orgulho e Preconceito': 4.5},

              'Patrick':
                  {'O Guia do Mochileiro das Galáxias': 1.5,
                   'Neuromancer': 3.3,
                   'A Culpa é das Estrelas': 3.9,
                   'Os Crimes do Monograma': 4.0},

               'Matheus':
                  {'O Guia do Mochileiro das Galáxias': 4.5,
                   'Neuromancer': 4.8,
                   'A Culpa é das Estrelas': 2.0,
                   'Orgulho e Preconceito': 2.2,
                   'Os Crimes do Monograma': 3.5,
                   'Fortaleza Digital': 5.0},
                   
                'Diego':
                  {'Neuromancer': 5.0,
                   'A Culpa é das Estrelas': 4.5,
                   'Orgulho e Preconceito': 2.5,
                   'Os Crimes do Monograma': 3.9},

                'Castro':
                  {'O Guia do Mochileiro das Galáxias': 1.8,
                   'A Culpa é das Estrelas': 4.5,
                   'Orgulho e Preconceito': 4.9,
                   'Fortaleza Digital': 2.7},
              
              }

avaliacoesLivro = {'O Guia do Mochileiro das Galáxias': 
		{'Lucas': 4.5, 
		 'Ester:': 5.0 ,
                 'Douglas': 3.5,
		 'Humberto': 2.5, 
		 'Patrick': 1.5,
                 'Matheus': 4.5,
                 'Castro': 1.8},
	 
	 'Neuromancer': 
		{'Ester': 4.2,
		 'Douglas': 4.5, 
		 'Patrick': 3.3, 
		 'Matheus': 4.8, 
		 'Diego': 5.0 },
				 
	 'A Culpa é das Estrelas': 
		{'Ester:': 3.0,
		 'Gabryell': 1.9, 
		 'Patrick': 3.9,
                 'Matheus': 2.0,
                 'Diego': 4.5,
                 'Castro': 4.5 },
	
	 'Orgulho e Preconceito': 
		{'Lucas': 1.6, 
		 'Ester:': 4.6 ,
		 'Douglas': 2.1,
                 'Gabryell': 2.5,
		 'Humberto': 4.5,
                 'Matheus': 2.2,
		 'Diego': 2.5, 
		 'Castro': 4.9 },
				 
	 'Os Crimes do Monograma': 
		{'Lucas': 2.4, 
		 'Ester:': 3.0,
                 'Douglas': 3.2,
		 'Patrick': 4.0, 
		 'Matheus': 3.5,
                 'Diego': 3.9 },
				 
	 'Fortaleza Digital': 
		{'Ester:': 3.8,
		 'Gabryell': 4.7, 
		 'Matheus': 5.0, 
		 'Casro': 2.7}
}


#função euclidiana

from math import sqrt
import matplotlib.pyplot as plt
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

def getGraficoDispersao(livroUm, livroDois):

    x = [livroUm]
    y = [livroDois]

    plt.plot([1, 2, 3, 4], [4, 7, 8, 12])

    plt.title('Plot De Livros')
    plt.xlabel('Livro Um')
    plt.ylabel('Livro Dois')

    plt.show()
