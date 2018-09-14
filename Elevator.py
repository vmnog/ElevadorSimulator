from pygame import mixer
import time
mixer.init()
mixer.music.load('musicaDeElevador.mp3')
mixer.music.play()


quantidadeElevadores = 1

print('=-'*30)
print('Bem-vindo ao Hotel Maneirão!')
print(f'A sua frente você encontra {quantidadeElevadores} elevador')
print('Você pode ir do térreo até o terceiro andar')
print('Botões: [0] [1] [2] [3]')

andarInicial = 0 # andarInicial é o Térreo
andarAtual = 0 # Pessoa está no térreo
    
while(1):

    listaAndares = ['térreo','primeiro','segundo','terceiro']

    print('-='*30)
    if andarInicial != 0:
        print(f'Você está no {andarAtual}º andar.')
    else:
        print(f'Você está no {listaAndares[andarAtual]}.')
    andarFinal = int(input('Qual andar você quer ir? ')) 


    if(andarFinal >= andarAtual):
        while(andarAtual <= andarFinal):

            
            time.sleep(2)
            print()
            
            if andarAtual != 0:
                print(f'Você está no {listaAndares[andarAtual]} andar.')
            else:
                print(f'Você está no {listaAndares[andarAtual]}.')
            andarAtual += 1
            
    else:
        while(andarAtual >= andarFinal):
            
            time.sleep(2)
            print()
            
            if andarAtual != 0:
                print(f'Você está no {listaAndares[andarAtual]} andar.')
            else:
                print(f'Você está no {listaAndares[andarAtual]}.')
            andarAtual -= 1            



    andarAtual -= 1
    andarInicial = andarFinal
    andarAtual = andarInicial
    print()
    if andarInicial != 0:
        print(f'Você chegou no {listaAndares[andarFinal]} andar, pode sair do elevador.')
    else:
        print(f'Você chegou no {listaAndares[andarFinal]}, pode sair do elevador.')
