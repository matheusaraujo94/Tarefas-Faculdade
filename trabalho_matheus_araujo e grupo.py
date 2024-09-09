# -*- coding: windows-1252 -*-
import csv
from time import sleep

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
tamanho_alfabeto = len(alfabeto)

def criptografar(texto_limpo):
    texto_criptografado = "******"

    return texto_criptografado

def decriptografar(texto_criptografado):
    texto_limpo = ""
    for letra in texto_criptografado:
        x = alfabeto.find(letra)
        if x == -1:
            texto_limpo += letra
        else:
            c = (x - 3) % tamanho_alfabeto
            letra_decriptografada = alfabeto[c]
            texto_limpo += letra_decriptografada
    return texto_limpo

def imprimirColorido(mensagem):
    print('\033[1;32m' + mensagem + '\033[0m')

def banner():
    logo = "********** GERENCIADOR DE SENHAS **********"
    imprimirColorido(logo)

def menu():
    imprimirColorido('==' * 28)
    print('''
        [ 1 ] Mostrar todas as senhas
        [ 2 ] Incluir Aplicativo
        [ 3 ] Editar Aplicativo
        [ 4 ] Excluir Aplicativo
        [ 0 ] Fechar Gerenciador''')
    imprimirColorido('==' * 28)

def avisar(mensagem):
    print('\033[1;31m' + mensagem + '\033[0m')

def carregar():
    aplicativos = {}
    try:
        with open('senhas.csv', 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                nome, usuario, senha_criptografada, url = linha
                senha = decriptografar(senha_criptografada)
                aplicativos[nome] = {
                    'usuario': usuario,
                    'senha': senha,
                    'url': url
                }
        print('>>>> Database carregado com sucesso...')
        print(f'>>>> {len(aplicativos)} Aplicativos carregados...')
        return aplicativos
    except FileNotFoundError:
        print('Arquivo não encontrado...')
        return aplicativos
    except Exception as erro:
        print('Ocorreu um erro...')
        print(erro)
        return aplicativos

def salvar(senhas):
    try:
        with open('senhas.csv', 'w', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            for aplicativo, detalhes in senhas.items():
                linha = [aplicativo, detalhes['usuario'], criptografar(detalhes['senha']), detalhes['url']]
                escritor_csv.writerow(linha)
        print('Database salvo com sucesso...')
    except Exception as erro:
        print('Ocorreu um erro ao salvar o arquivo...')
        print(erro)

def mostrar(senhas):
    if len(senhas) == 0:
        avisar('Lista vazia...')
    else:
        for aplicativo, detalhes in senhas.items():
            senha_descriptografada = detalhes['senha']
            print('Aplicativo:', aplicativo)
            print('Usuário:', detalhes['usuario'])
            print('Senha:', senha_descriptografada)
            print('URL:', detalhes['url'])
            print('~' * 25)
        print(f'Total: {len(senhas)}')

def incluir_aplicativo(senhas):
    nome = input("Nome do aplicativo: ").strip()
    if nome in senhas:
        avisar("Aplicativo já existe!")
        return
    usuario = input("Nome do usuário: ").strip()
    senha = input("Senha: ").strip()
    url = input("URL: ").strip()
    senhas[nome] = {
        'usuario': usuario,
        'senha': senha,
        'url': url
    }
    salvar(senhas)
    avisar('Aplicativo incluído com sucesso!')

def editar_aplicativo(senhas):
    nome = input('Digite o nome do aplicativo que deseja editar: ').strip()
    if nome in senhas:
        novo_usuario = input("Novo usuário: ").strip()
        nova_senha = input("Nova senha: ").strip()
        nova_url = input("Nova URL: ").strip()
        senhas[nome] = {
            'usuario': novo_usuario,
            'senha': nova_senha,
            'url': nova_url
        }
        salvar(senhas)
        avisar('Aplicativo editado com sucesso!')
    else:
        avisar('Aplicativo não encontrado.')

def excluir_aplicativo(senhas):
    nome = input('Digite o nome do aplicativo que deseja excluir: ').strip()
    if nome in senhas:
        del senhas[nome]
        salvar(senhas)
        avisar('Aplicativo excluído com sucesso!')
    else:
        avisar('Aplicativo não encontrado.')

def executar(opcao, senhas):
    if opcao == '1':
        mostrar(senhas)
    elif opcao == '2':
        incluir_aplicativo(senhas)
    elif opcao == '3':
        editar_aplicativo(senhas)
    elif opcao == '4':
        excluir_aplicativo(senhas)
    elif opcao == '0':
        return False
    return True

if __name__ == "__main__":
    banner()
    senhas = carregar()
    executar_programa = True
    while executar_programa:
        menu()
        opcao = input('Digite uma opção: ').strip()
        executar_programa = executar(opcao, senhas)
        sleep(2)