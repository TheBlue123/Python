def create_posts(list_posts, next_id):
    post_tittle = input("Digite o título do post: ")
    author_name = input("Digite o nome do autor: ")
    estrutura_post = {
    "id_post": next_id,
    "titulo": post_tittle,
    "autor": author_name,
    "comentarios": []
 }
    list_posts.append(estrutura_post)
    next_id += 1
    return next_id

def listar(list_posts):
    for posts in list_posts:
        print("O id do poste é: ",posts['id_post']) 
        print("O título do post é: ",posts['titulo'])
blog_posts = []
next_id = 1
while True:
    print("--- Mini Blog TQI ---")
    print("[1] - Criar Novo Post")
    print("[2] - Listar Todos os Posts")
    print("[3] - Adicionar Comentário a um Post")
    print("[4] - Ver Post Completo")
    print("[5] - Sair")
    print("---------------------")
    opcao = int(input("Digite uma opcao: "))

    if opcao == 1:
        create_posts(blog_posts, next_id)
    elif opcao == 2:
        listar(blog_posts)
        
    