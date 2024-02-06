def add_to_list(my_list, item):
    if item not in my_list:
        my_list.append(item)
        print(f"{item_to_add} added to the list: {my_list}")
        return True
    else:
        print(f"{item_to_add} already exists in the list: {my_list}")
        return False


my_list = [1, 2, 3, 4]
item_to_add = 5

result = add_to_list(my_list, item_to_add)

if result:
    print(f"{item_to_add} added to the list: {my_list}")
else:
    print(f"{item_to_add} already exists in the list: {my_list}")
temas = []
publicos_alvos = []
nivel = []
livro = []
i = 0
while True:
    user_input = input("Tema: ")
    temas.append(user_input)
    user_input = input("Público Alvo: ")
    publicos_alvos.append(user_input)
    user_input = input("Nível: ")
    nivel.append(user_input)
    matriz_suport = [temas[i], publicos_alvos[i], nivel[i]]
    livro.append(matriz_suport)
    print("Você adicionou esse livro:", livro[i])
    user_input = input("Inserir outro livro?: ")
    if user_input.lower() == "n":
        break
    if user_input.lower() == "s":
        i += 1
