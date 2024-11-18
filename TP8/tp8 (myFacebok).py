# My Facebook

# Cada dicionário, correspondente a um _post_ e tem chaves `id`, `conteudo`, `autor`, `dataCriacao` e `comentarios`. 
# Por sua vez, `comentarios` é uma lista de dicionários com chaves `comentario` e `autor`.

# TPC 3

myFacebook = []


# a)
def quantosPost(redeSocial):
    return f'A rede social {redeSocial} tem {len(redeSocial)} posts'

def postsAutor(redeSocial, autor):
    res = []
    for post in redeSocial:
        if autor == post['autor']:
            res.append(post)

    return res

# b)
def autores(redeSocial):
    res = []
    for post in redeSocial:
        res.append(post['autor'])
        res_ordem = sorted(res)
    return  res_ordem

# c)
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    post = {}
    post['id'] = f'p{len(redeSocial)+1}'
    post['conteúdo'] = conteudo
    post['autor'] = autor
    post['data de criação'] = dataCriacao
    post['comentários'] = comentarios_lista

    redeSocial.append(post)
    return 'Post criado com sucesso!'

# d)
def remPost(redeSocial, id):
    for post in redeSocial:
        if id == post['id']:
            redeSocial.remove(post)
    print('Post removido')
    return redeSocial

# e)
def postsPorAutor(redeSocial):
    print('Autor       Id       Conteúdo                                           Data de Criação')
    for post in redeSocial:
        print('--------------------------------------------------------------------------------------------')
        print(f'{post['autor']}         {post['id']}        {post['conteúdo']}                                           {post['data de criação']}')
        print('--------------------------------------------------------------------------------------------')
    return 

# f)
def comentadoPor(redeSocial, autor):
    res = []
    for post in redeSocial:
        for comentario in post['comentários']:
            if comentario['autor'] == autor:
                res.append(post)
    return res

def main():
    print("""  
    1) Inserir post
    2) Remover post
    3) Consultar os posts pelo nome do autor
    4) Feed da rede social
    5) Consultar os autores registados na rede social, por ordem alfabética
    6) Comentários feitos por um autor
    7) Quantidade de posts presentes na rede social
    0) Sair""")


programa = True
while programa:
    redeSocial = myFacebook
    main()
    op = input('Insira a opção que deseja: ').strip()
    while op not in ['0', '1', '2', '3', '4', '5', '6', '7', '0']:
        op = input('Insira a opção que deseja: ').strip()
    if op == '1':
        continuar = True
        while continuar:
            conteudo = input('Partilhe com os seus seguidores o que sente: ').strip().lower()
            autor = input('Insira o nome do autor: ').strip().lower()
            dataCriacao = input('Insira a data do seu post: ').strip().lower()
            opinião = input('Quer adicionar comentários? [S/N] ').strip().upper()
            while opinião not in ['S', 'N']:
                print("Por favor, insira apenas 'S' ou 'N'.")
                opinião = input('Quer adicionar comentários? [S/N] ').strip().upper()
            if opinião == 'S':
                comentarios_lista = []
                comentarios = {}
                comentarios['comentario'] = input('Insira o comentário: ')
                comentarios['autor'] = input('Insira o autor do comentário: ').strip().lower()
                comentarios_lista.append(comentarios)
            
            print(insPost(redeSocial, conteudo, autor, dataCriacao, comentarios))

            op = input("Deseja inserir mais posts? [S/N] ").strip().upper()
            while op not in ['S', 'N']:
                print("Por favor, insira apenas 'S' ou 'N'.")
                op = input("Deseja inserir mais posts? [S/N] ").strip().upper()
    
            continuar = (op == 'S')

    elif op == '2':
        confirmar = input('Tem a certeza que pretende remover um post? [S/N] ').strip().upper()
        while confirmar not in ['S', 'N']:
                print("Por favor, insira apenas 'S' ou 'N'.")
                confirmar = input('Tem a certeza que pretende remover um post? [S/N] ').strip().upper()
        if confirmar == 'S':
            id = input('Insira o id do post que pretende remover: ').strip().lower()
            print(remPost(redeSocial, id))


    elif op == '3':
        autor = input("Insira o nome do autor que procura: ").strip().lower()
        print(postsAutor(redeSocial, autor))

    elif op == '4':
        print(postsPorAutor(redeSocial))

    elif op == '5':
        print(autores(redeSocial))

    elif op == '6':
        autor = input('Insira o autor que pretende: ').strip().lower()
        print(comentadoPor(redeSocial, autor))

    elif op == '7':
        print(quantosPost(redeSocial))

    elif op == '0':
        programa = False

print('Signed out.')