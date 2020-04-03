# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 02:47:55 2020

@author: byron
"""


#imporatndo random pro sistema dos dadinhos
#imporatndo random pro sistema dos dadinhos
import random
import time
from colorama import Fore, Style


#variáveis relevantes para o programa
dado_01 = 0 
dado_02 = 0
fichas = 0 
aposta = 0
tipos_de_aposta = ["PASS LINE BET" , "FIELD", "ANY CRAPS", "TWELVE"]
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
        resultado = "A soma dos dados foi um número entre (7 ou 11). Você venceu esta rodada!"
    elif soma == 2 or soma == 3 or soma == 12: 
        resultado = "A somda dos dados foi um número entre (2,3,12). Você perdeu esta rodada por tirar um dos números CRAPS."
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
        resultado = "A soma dos dados foi um número de 5 à 8, portanto você perdeu a rodada!"
    elif soma == 2:
        resultado = "A soma dos dados deu 2 portanto você ganhou esta rodada recebendo o valor da sua aposta mais um bônus com o dobro do valor da sua aposta!"
    elif soma == 12: 
        resultado = "A soma dos dados deu 12, portanto você ganhou esta rodada recebendo o valor da sua aposta mais um bônus com o triplo do valor da sua aposta!"
    else:
        resultado = "A soma dos dados deu um número entre (3,4,9,10,11), portanto você ganhou esta rodada recebendo o valor da sua aposta mais um bônus no mesmo valor da sua aposta!"
    return resultado 





#função que define a jogada any craps
def any_craps(dado_01, dado_02):
    soma = dado_01 + dado_02
    if soma == 2 or soma == 3 or soma  == 12:
        resultado = "A soma dos dados deu um número entre (2,3,12), portanto você venceu esta rodada e ganhou 7 vezes o valor da sua aposta!"
    else: 
        resultado = "A soma dos dados deu um número entre (4,5,6,7,8,9,10,11), portanto você perdeu a rodada!"
    return resultado 




#função que define a jogada twelve
def twelve(dado_01, dado_02):
    soma = dado_01 + dado_02 
    if soma == 12: 
        resultado = "A soma dos dados deu 12, portanto você venceu esta rodada!"
    else: 
        resultado = "A soma dos dados deu um número entre 2 e 11, portanto você perdeu a rodada!"
    return resultado





#a partir daqui começamos a lidar com a mecânica do jogo
    

print(Style.RESET_ALL)
print(Fore.CYAN +"Olá, seja muito bem vindo ao CRAPS INSPER!")
print('')
time.sleep(1)
fichas = int(input(Fore.CYAN + "Digite aqui o número de fichas que desja comprar: ")) 



#Impede engraçadinhos de comprar um número negativo de fichas
while fichas < 0: 
    print('')
    time.sleep(1)
    print(Fore.RED + "Valor inválido! Por favor tente novamente.")
    print('')
    time.sleep(1)
    fichas = int(input(Fore.CYAN + "Digite aqui o número de fichas que desja comprar: ")) 

    
    




print('')
time.sleep(1)
print(Fore.BLUE + "Seu saldo de ficha atual é de {0}.".format(fichas))






#aqui começamos a lidar com o loop  do jogo

while craps_insper == True: 
      nova_rodada = input(Fore.CYAN + "Deseja iniciar  uma nova rodada? (s/n): ")
      while nova_rodada != "s" and nova_rodada != "n": 
          print()
          time.sleep(1)
          print(Fore.CYAN + "Resposta inválida, por favor tente novamente!")
          print('')
          time.sleep(1)
          nova_rodada = input(Fore.CYAN + "Deseja iniciar  uma nova rodada? (s/n): ")


#se a resposta for não encerra o jogo e mostra o saldo final
      if nova_rodada == "n":
          craps_insper = False
          print('')
          time.sleep(1)
          print(Fore.RED + "Seu saldo final é de  {0} fichas.".format(fichas))
    
    
#se a resposta o jogdador quiser joga iniciar uma nova rodada    
      else: 
          if fichas == 0:
              print('')
              time.sleep(1)
              print(Fore.RED + "Desculpe mas você não possui saldo suficiente para uma nova rodada.O jogo será encerrado!")
              break #como o jogador não tem saldo suficiente, esse if faz com que o jogo acabe
              
              
          else: 
              print('')
              time.sleep(1)
              aposta = int(input(Fore.CYAN + "Escolha um valor para apostar: "))
              while aposta > fichas: 
                  print('') 
                  time.sleep(1)
                  print(Fore.RED + "Valor da aposta maior que o saldo! Por favor escolha um novo valor!")
                  print('')
                  time.sleep(1)
                  aposta = int(input("Escolha um valor para apostar: "))
                  
              #aqui começa a escolha das as apostas e  a mecânica de aposta    
              print('')
              time.sleep(1)
              print(Fore.CYAN + "Você está na fase COMEOUT; escolha seu tipo de aposta:")
              print('')
              time.sleep(1)
              print(Fore.MAGENTA + tipos_de_aposta)
              
              
              print('')
              time.sleep(1)
              escolha = input(Fore.CYAN + "Digite uma das opções acima em maiúsculo: ")
              
              #impede o jogador de digitar opções inexistentes
              while escolha != tipos_de_aposta[0] and escolha != tipos_de_aposta[1] and escolha != tipos_de_aposta[2] and escolha != tipos_de_aposta[3]:
                  print('')
                  time.sleep(1)
                  print(Fore.RED + "Opção inválida, digite novamente!")
                  print('')
                  time.sleep(1)
                  escolha = input(Fore.CYAN + "Digite uma das opções acima em maiúsculo: ")
             
                
                  
              #desenvolvendo aposta Pass Line Bet    
              if escolha == "PASS LINE BET":
                  dado_01 = random.randint(1,6)
                  dado_02 = random.randint(1,6)
                  print('')
                  time.sleep(1)
                  rodada = (pass_line_bet_comeout(dado_01,dado_02))








        


        
        

   




    
    
    
    