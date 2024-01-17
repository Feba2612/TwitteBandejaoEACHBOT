import sys
from datetime import datetime
def remover_nova_linha_do_array(arr):
    novo_arr = [s.replace("\n", "").replace(":", "").strip() for s in arr]
    return novo_arr



def imprimir_cardapio_bandejao():
    with open("cardapioBandejãodia.txt","r+", encoding="UTF-8") as cardapioDiaBandejaao: 
        cardapioDiaBandejaao.truncate(0)
    
    with open('cardapioSemana.txt', 'r', encoding="UTF-8") as text:
        texto = text.readlines()

    x = 0
    index_almoco = 0
    

    textoOriginal = texto
    texto = remover_nova_linha_do_array(texto)


    
    HOJE = datetime.today()
    dia_semana = HOJE.isoweekday() 
    dia_mes = HOJE.strftime('%d/%m')
    horario = HOJE.strftime("%H")
    horario = int(horario)
    
    # #teste
    # dia_semana = 1
    # dia_mes = "08/01"

    segunda = ["Segunta-Feira ","Segunda-Feira " + dia_mes]
    terca = ["Terça-Feira ", "Terça-Feira " + dia_mes]
    quarta = ["Quarta-Feira ", "Quarta-Feira " + dia_mes]
    quinta = ["Quinta-Feira ", "Quinta-Feira " + dia_mes]
    sexta = ["Sexta-Feira", "Sexta-Feira "+ dia_mes]
    nao = ["nao", "nao"]
    diaSemanaT = [nao, segunda, terca, quarta, quinta, sexta]
    
    

    try: 
        for j in range(0,2):
            for palavra in texto:
                if diaSemanaT[dia_semana][j] == palavra and horario < 12:
                    index_almoco = texto.index(palavra)
                    textoOriginal[index_almoco] = texto[index_almoco] + "\nAlmoço\n"
                elif diaSemanaT[dia_semana][j] == palavra and horario > 12:
                    index_almoco = texto.index(palavra)
                    index_almoco += 11
                    textoOriginal[index_almoco + 1] = textoOriginal[index_almoco + 1] + "\njantar\n"

        for i in range (index_almoco, index_almoco + 8): 
            with open("cardapioBandejãodia.txt", "a", encoding="UTF-8") as cardapioDiaBandejaao:
                cardapioDiaBandejaao.write(textoOriginal[i])
                         
    except:
        tt = "Infelizmente, o bandejão encontra-se fechado hoje :( "
        x = 1
        
    
    if textoOriginal[index_almoco-1] == "**Os Restaurantes Universitários não fornecem copos descartáveis. Tragam suas canecas.**\tFechado\n" and horario > 12:
        tt = "Hoje o bandejão estará fechado no jantar"  #pode dar problema futuramente
        x = 2
        
        
    elif textoOriginal[index_almoco-1] == "**Os Restaurantes Universitários não fornecem copos descartáveis. Tragam suas canecas.**\tFechado\n" and horario <12:
        tt = "Hoje o bandejão estará fechado no jantar"  #pode dar problema futuramente
        print(tt)
        sys.exit()
       
    if x == 0:    
        with open("cardapioBandejãodia.txt","r+", encoding="UTF-8") as cardapioDiaBandejaao:
            tt = cardapioDiaBandejaao.read()
            cardapioDiaBandejaao.truncate(0)
    else:
        with open("cardapioBandejãodia.txt","r+", encoding="UTF-8") as cardapioDiaBandejaao: 
            cardapioDiaBandejaao.truncate(0)
    return tt

