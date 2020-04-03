# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 02:47:55 2020

@author: byron
"""


#imporatndo random pro sistema dos dadinhos
import random
import time
from colorama import Fore, Style


#variáveis relevantes para o programa
dado_01 = 0 
dado_02 = 0
fichas = 0 
aposta = 0
soma_dados = dado_01 + dado_02
craps_insper = True 





#a partir daqui eu começo a fazer as funções dos tipos de jogada. 
#as funções estão simplificadas e n produzem alterações no saldo e nem sempre fala quanto
#ganhou ou perdeu, pensei que seria mais tranquilo fazer isso fora da função. 
#
#
#
#
#
#aqui é função da jogada do tipo pass line bet, essa primeira corresponde a 
#fase desse tipo de aposta, abrindo margem pra mudar para o modo point.
def pass_line_bet_comeout(dado_01, dado_02):
    soma = dado_01 + dado_02
    resultado = 0
    if soma == 7 or soma == 11:
        resultado = "A soma dos dados foi de {0} pontos. Você venceu esta rodada!".format(soma)
    elif soma == 2 or soma == 3 or soma == 12: 
        resultado = "A somda dos dados foi de {0} pontos. Você perdeu esta rodada por tirar um dos números CRAPS.".format(soma)
    else: 
        resultado = "Você migrou para a fase POINT!"
    return resultado





#como quando muda de modo o jogador pode escolher outro tipo de aposta tive que 
#fazer essa segunda parte da pass line bet pro caso do jogador quiser continuar 
#com esse tipo de aposta na fase point.
def pass_line_bet_point(soma_dados):
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    soma = dado_1 + dado_2
    resultado = 0 
    rodada = True
    while rodada == True:
        if soma == 7 :
            resultado = "A soma deu 7, você perdeu esta rodada!"
            rodada = False
        elif soma == soma_dados:
            resultado = "A soma dos dados é igual ao POINT! Você venceu esta rodada!"
            rodada = False
        else:
            dado_1 = random.randint(1,6)
            dado_2 = random.randint(1,6)
            soma = dado_1 + dado_2
    return resultado






#função que define a jogada field
def field(dado_01, dado_02):
    soma = dado_01 + dado_02 
    resultado = 0 
    if soma >=5 and soma <= 8:
        resultado = "A soma dos dados deu {0}, portanto você perdeu a rodada!".format(soma)
    elif soma == 2:
        resultado = "A soma dos dados deu {0}, portanto você ganhou esta rodada recebendo o valor da sua aposta mais um bonus com o dobro do valor da sua aposta!".format(soma)
    elif soma == 12: 
        resultado = "A soma dos dados deu {0}, portanto você ganhou esta rodada recebendo o valor da sua aposta mais um bonus com o triplo do valor da sua aposta!".format(soma)
    else:
        resultado = "A soma dos dados deu {0}, portanto você ganhou esta rodada recebendo o valor da sua aposta mais um bonus no mesmo valor da sua aposta!".format(soma)
    return resultado 





#função que define a jogada any craps
def any_craps(dado_01, dado_02):
    soma = dado_01 + dado_02
    if soma == 2 or soma == 3 or soma  == 12:
        resultado = "A soma dos dados deu {0}, portanto você venceu esta rodada!".format(soma)
    else: 
        resultado = "A soma dos dados deu {0}, portanto você perdeu a rodada!".format(soma)
    return resultado 




#função que define a jogada twelve
def twelve(dado_01, dado_02):
    soma = dado_01 + dado_02 
    if soma == 12: 
        resultado = "A soma dos dados deu {0}, portanto você venceu esta rodada!".format(soma)
    else: 
        resultado = "A soma dos dados deu {0}, portanto você perdeu a rodada!".format(soma)
    return resultado





#a partir daqui começamos a lidar com a mecânica do jogo
    

print(Style.RESET_ALL)
print(Fore.CYAN +"Olá, seja muito bem vindo ao CRAPS IMSPER!")
print('')
time.sleep(1)
fichas = int(input(Fore.CYAN + "Digite aqui o número de fichas que desja comprar: "))














        


        
        

   




    
    
    
    