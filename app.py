import os

# lista que armazena dicionários com os dados referentes aos restaurantes cadastrados no sistema
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]


def exibir_nome_do_programa():
    print("""
      🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢
      """)

def exibir_opcoes():
    print('1.Cadastrar restaurante')
    print('2.Listar restaurantes')
    print('3.Alternar estado do restaurante')
    print('4.Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizar app')

# função que retoma o menu de opções
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

# função para o caso de erro
def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

# função criada para evitar repetições dos elementos nela contidos ao longo do código
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

# função para cadastrar restaurantes
'''
1) Recebe os inputs:
- Nome do restaurante
- Categoria
2) Armazena os dados fornecidos em um dicionário
3) Envia o dicionário para a lista restaurantes
'''
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)

    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

# função com loop de repetição para printar na tela os dados fornecidos, à medida que vão sendo adicionados
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')
    #                           ajuste de espaço
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')

    # inicializando a variável booleana
    restaurante_encontrado = False
    for restaurante in restaurantes:
          # condição que verifica um elemento específico pertencente à lista
          if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
        print(f'.{restaurante}')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

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
    '''
        
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
