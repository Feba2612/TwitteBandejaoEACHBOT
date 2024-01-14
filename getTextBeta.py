

import sys
from datetime import datetime
def remover_nova_linha_do_array(arr):
    novo_arr = [s.replace("\n", "").replace(":", "").strip() for s in arr]
    return novo_arr



def imprimir_cardapio_bandejao():
    with open('cardapioSemana.txt', 'r', encoding="UTF-8") as text:
        texto = text.readlines()

    index_almoco = -1
    index_janta = 0
    espacos = 0

    textoOriginal = texto
    texto = remover_nova_linha_do_array(texto)


    index_dia = 0
    HOJE = datetime.today()
    dia_semana = HOJE.isoweekday() 
    dia_mes = HOJE.strftime('%d/%m')
    dia_mes = str("08/01")


    segunda = ["Segunta-Feira ","Segunda-Feira " + dia_mes]
    terca = ["Terça-Feira ", "Terça-Feira " + dia_mes]
    quarta = ["Quarta-Feira ", "Quarta-Feira " + dia_mes]
    quinta = ["Quinta-Feira ", "Quinta-Feira " + dia_mes]
    sexta = ["Sexta-Feira", "Sexta-Feira "+ dia_mes]
    nao = ["nao", "nao"]
    diaSemanaT = [nao, segunda, terca, quarta, quinta, sexta]
    
    # #teste
    # dia_semana = 1
    # dia_mes = "08/01"

    try: 
        for j in range(0,2):
            for palavra in texto:
                if diaSemanaT[dia_semana][j] == palavra:
                    index_almoco = texto.index(palavra)
        for i in range (index_almoco, index_almoco + 9): 
            with open("cardapioBandejãodia.txt", "a", encoding="UTF-8") as cardapioDiaBandejaao:
                cardapioDiaBandejaao.write(textoOriginal[i])
                         
    except:
        print("Infelizmente, o bandejão encontra-se fechado hoje :( ")
        sys.exit()
       
       
       
       
    with open("cardapioBandejãodia.txt","r+", encoding="UTF-8") as cardapioDiaBandejaao:
        tt = cardapioDiaBandejaao.read()
        cardapioDiaBandejaao.truncate(0)
    return tt
