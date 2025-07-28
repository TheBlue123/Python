linhas = 0
colunas = 0
def criar_hotel(linhas, colunas):
    hotel = []
    for i in range(linhas):
        andar = []
        for j in range(colunas):
            quarto = {'status': 'livre', 'hospede': None}
            andar.append(quarto)
        hotel.append(andar)
    return hotel
def exibir(hotel):
    for andar in hotel:
        linha = ''
        for quarto in andar:
            if quarto['status'] == 'livre':
                linha += '[ L ] '
            else:
                linha += '[ O ] '
        print(linha)
def adicionar(hotel):
    procurar_andar = int(input("\nDigite o andar: "))
    procurar_quarto = int(input("\nDigite o numero do quarto: "))
    
    quarto = hotel[procurar_andar-1][procurar_quarto-1]
    if quarto['status'] == 'livre':
        quarto['status'] = 'ocupado'
        print("\nO quarto foi ocupado! ")
    else:
        print("\nO quarto ja esta ocupado! ")
def remover(hotel):
    procurar_andar = int(input("\nDigite o andar: "))
    procurar_quarto = int(input("\nDigite o numero do quarto: "))
    
    quarto = hotel[procurar_andar-1][procurar_quarto-1]
    if quarto['status'] == 'ocupado':
        quarto['status'] = 'livre'
        print("\nO quarto foi desocupado! ")
    else:
        print("\nO quarto ja esta desocupado! ")
def porcentagem(hotel):
    quartos_ocupados = 0
    total_quartos = 0
    for andar in hotel:
        for quarto in andar:
            total_quartos += 1
            if quarto['status'] == 'ocupado':
                quartos_ocupados += 1
    media = (quartos_ocupados / total_quartos) * 100
    
    print(f"\nA porcentagem de taxa de ocupacao e {media}%")
        
    
while True:
    print("--- Hotel TQI - Gestão de Quartos ---")
    print("[1] - Tamanho do Hotel")
    print("[2] - Exibir Ocupação")
    print("[3] - Fazer Check-in")
    print("[4] - Fazer Check-out")
    print("[5] - Ver Taxa de Ocupação")
    print("[6] - Sair")
    print("-----------------------------------")
    
    opcao = int(input("\nDigite uma numero para a opcao desejada: "))
    
    if opcao == 1:
        linhas = int(input("\nDigite a quantidade de andares (linhas): "))
        colunas = int(input("\nDigite a quantidade de quartos por andar (colunas): "))
        hotel = criar_hotel(linhas, colunas)
    elif opcao == 2: 
        if hotel is not None:
            exibir(hotel)
        else:
            print("Crie o hotel primeiro! ")
    elif opcao == 3:
        adicionar(hotel)
    elif opcao == 4:
        remover(hotel)
    elif opcao == 5:
        porcentagem(hotel)
    elif opcao == 6:
        print("Saindo...")
        break
    else:
        print("\nDigite uma opcão valida!")
        