#Júlia Conconi, Júlia Fortunato e Lanna Kamily

estoque_atual = { #para criar um estoque, montamos um tipo de array, onde colocamos o nome, colocamos o sinal de igual, abrimos chaves e começamos 
    #a declarar o nome do objeto dentro de aspas, os dois pontos servem como iguais, e depois adicionamos o valor. Em phyton sempre colocamos virgula no final!!
    #nesse exemplo também estamos usando chaves, pq estamos criando um dicionario que guarda pares de chaves  e valores.
    "caneta" :150,
    "lapis": 60,
    "pastas" : 70,
    "folhas de sulfite" : 100,
    "lapis colorido":140,
    "cadernos": 95,
    "colas": 115,
    "mochilas": 80,

}

movimentacoes_dia = [ # Aqui estamos fazendo a movimentação das coisas, e estamos colocando as "tuplas", que no caso seriam 
    #produtos, o tipo de movimentação, e a quantidade final que saiu ou entrou. Nesse caso colocamos [] porque estamos criando uma lista e vamos verificar essa lista, fazer uma consulta.
    # SEMPRE VIRGULA!
("caneta", "saída", 25),
("lapis", "entrada", 10),
("pastas", "entrada", 50),
("pastas", "saída", 20),
("folhas de sulfite", "entrada", 20),
("folhas de sulfite", "saída", 30),
("lapis colorido", "saída", 50),
("lapis colorido", "entrada", 10),
("cadernos", "saída", 50),
("colas", "entrada", 22),
("colas","saída",30),
("mochilas", "entrada", 80),
("mochilas", "saída", 60),
("caneta", "saída", 30),
("pastas", "saída", 50),
]

for produtos, tipo, quantidade in movimentacoes_dia: # aqui nos vamos consultar o produto, o tipo da movimentação, e a quantidade, dentro das movimentações. Por isso que colocamos o IN, que significa "em tal lugar". 
    #Nesse caso não colocamos {} so os pontos e as variaveis (produto, tipo, quantidade) são criadas dentro do for
    if produtos not in estoque_atual: #Aqui estamos basicamente dizendo que se o produto não existe em estoque_atual então, ele deve ser adicionado a estoque_atual, na sessão de produtos, no primeiro lugar da fila
        estoque_atual[produtos] = 0

    if tipo == "entrada": # Aqui formamos uma condição, onde se o tipo for entrada, então dentro de produtos do estoque atual
        #vamos somar e igualar a quantidade
        estoque_atual[produtos] += quantidade

    elif tipo == "saída": # Depois formamos uma condição, onde se for do tipo saída, dentro de estoque atual, e de produtos, vamos subitrair e igualar
        estoque_atual[produtos] -= quantidade


produtos_reposicao = [] #Aqui criamos uma lista vazia para colocar os produtos que precisam de reposição

for produtos, quantidade in estoque_atual.items(): #Aqui estamos verificando o produto e a sua quantidade final para saber se precisa ou não de reposição.
    #utilizamos o .items para pegar mais de um topico da lista, aqui no caso pegamos produtos e quantidade
    if quantidade <= 50: #Se a quantidade for menos que 50, vamos fazer alguma coisa
        produtos_reposicao.append(produtos) # E aqui, se for menos que 50 é adicionado em produtos para reposição. Colocamos o .append para adicionar no final da linha
        #(produtos), é utilizado para pegar o nome do produto na parte de produtos.

print("Estoque atualizado:")
for produto, quantidade in estoque_atual.items(): #colocamos um for que vai rodar os produtos e a quantidade no estoque
    print(f"- {produto}: {quantidade} unidades") # depois vamos exibir o produto e sua quantidade

print("\nProdutos que precisam de reposição (<= 50 unidades):")
if produtos_reposicao:
    for produto in produtos_reposicao: # depois vamos rodar um for que vai mostrar os produtos que também estão na lista de produtos para reposição
        print(f"- {produto}")# E aqui vamos exibir isso
else:
    print("Nenhum produto precisa de reposição!")

