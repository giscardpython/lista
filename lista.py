# lista
nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joana', 'Maria', 'Mariana']

# exibe a lista
print(nomes_lista)
print(nomes_lista[0]) # exibindo o primeiro nome da lista
print(nomes_lista[2]) # exibindo o terceiro nome da lista
print(nomes_lista[5]) # exibindo o sexto e último nome da lista

# exibir os nomes um embaixo do outro
for nome in nomes_lista:
    print(nome)

for i in range(2):
    print(nomes_lista,i)

for i in range(len(nomes_lista)):
    print(f'{i + 1}o nome da lista: {nomes_lista[i]}')

# ordenação
nomes_lista.sort()
for nome in nomes_lista:
    print(nome)

# lista reversa
nomes_lista.sort(reverse=True)
for nome in nomes_lista:
    print(nome)                
