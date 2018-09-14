import time

quantidadeElevadores = 1

print('=-'*30)
print('Bem-vindo ao Hotel Maneirão!')
print(f'A sua frente você encontra {quantidadeElevadores} elevador')
print('=-'*30)


andarInicial = 0 # andarInicial é o Térreo
andarAtual = 0 # Pessoa está no térreo
    
while(1):

    listaAndares = ['térreo','primeiro','segundo','terceiro']

    print('-='*30)
    print(f'Você está no {listaAndares[andarAtual]}')
    andarFinal = int(input('Qual andar você quer ir? ')) 
    
    while(andarAtual <= andarFinal):
        time.sleep(2)
        print()
        print(f'Você está no {listaAndares[andarAtual]} andar ')
        andarAtual += 1    

    andarAtual -= 1
    andarInicial = andarFinal
    print()
    print(f'Você chegou no {andarFinal}º andar, pode sair do elevador.')
