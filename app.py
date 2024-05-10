import os

def exibir_nome_do_programa():
    print("""
      🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢
      """)

def exibir_opcoes():
    print('1.Cadastrar restaurante')
    print('2.Listar restaurante')
    print('3.Ativar restaurante')
    print('4.Sair restaurante\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o app ')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    '''
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    else:
        finalizar_app() 
    '''
    # situações que envolvem múltiplos padrões complexos
    match opcao_escolhida:
        case 1:
            print('Adicionar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativar restaurante')
        case 4:
            print('Finalizar app')
        # padrão coringa equivalente ao else
        case _:
            print('Opção inválida!')



def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
