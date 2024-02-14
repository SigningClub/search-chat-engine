import click


@click.command()
@click.option("--subject", default="DNF", help="Subject of the book")
@click.option(
    "--targetaudience", default="DNF", help="Target audience of the book"
)
@click.option("--theme", default="DNF", help="The theme of the book")
def add_to_matrix(subject, targetaudience, theme):
    temas = []
    publicos_alvos = []
    nivel = []
    livro = []
    temas.append(theme)
    publicos_alvos.append(targetaudience)
    nivel.append(subject)
    matriz_suport = [temas[0], publicos_alvos[0], nivel[0]]
    livro.append(matriz_suport)
    print("Você adicionou esse livro:", livro[0])
    return livro


livro = add_to_matrix()
# click.echo(theme)
my_list = [1, 2, 3, 4]
item_to_add = 5

# result = add_to_list(my_list, item_to_add)

# if result:
#    print(f"{item_to_add} added to the list: {my_list}")
# else:
#    print(f"{item_to_add} already exists in the list: {my_list}")
# temas = []
publicos_alvos = []
nivel = []
livro = []
i = 0
# print(theme, target - audience, subject)
# while True:
#    user_input = input("Tema: ")
#    temas.append(user_input)
#    user_input = input("Público Alvo: ")
#    publicos_alvos.append(user_input)
#    user_input = input("Nível: ")
#    nivel.append(user_input)
#    matriz_suport = [temas[i], publicos_alvos[i], nivel[i]]
#    livro.append(matriz_suport)
#    print("Você adicionou esse livro:", livro[i])
#    user_input = input("Inserir outro livro?: ")
#    if user_input.lower() == "n":
#        break
#    if user_input.lower() == "s":
#        i += 1
