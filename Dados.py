avaliacoes = {'Lucas':
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
                  {'O Ultimato BourneAndroides Sonham com Ovelhas Elétricas?': 3.5,
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

#função euclidiana

from math import sqrt

def euclidiana(usuario_1, usuario_2):
    livros_comum = {} #verifica se há avaliacoes do mesmo filme entre os dois usuários

    for item in avaliacoes[usuario_1]: #busca os livros que o usuário leu
        if item in avaliacoes[usuario_2]: livros_comum[item] = 1 #verifica se os livros tbm estão no user 2

    if len(livros_comum == 0): return 0 #tamanho da lista == 0 (não tem livros em comum)

    soma = sum([pow(avaliacoes[usuario_1][item] - avaliacoes[usuario_2][item], 2) #funcao euclidiana

        for item in avaliacoes[usuario_1] if item in avaliacoes[usuario_2]]) #pega todos os itens dentro dos dois usuários

    return 1/(1 + sqrt(soma)) #retorna o valor em porcentagem