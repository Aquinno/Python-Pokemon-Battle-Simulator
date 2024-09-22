import random #Para rolar os dados
import time #Para o sleep

#Variáveis globais(Mesmo que não seja a melhor opção, por enquanto é como faço confortavelmente)
p = 'Pikachu'
s = 'Squirtle'
c = 'Charmander'
l = 1
q = 1
ac = 1
cu = 1
vida_monstro = 40
vida_jogador = 40

#Funções das ações                
def ataque():
    global vida_monstro, vida_jogador, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    y = random.randint(1,20)
    vida_monstro = (vida_monstro - y)
    print("{} causou {} de dano!".format(b,y))
    if y == 20:
        print("Dano crítico!")
    elif y == 1:
        print("Erro crítico!")
    print("Vez do Torchic!")
    time.sleep(1)
    z = random.randint(1,20)
    vida_jogador = (vida_jogador - z)
    print("Torchic causou {} de dano!".format(z))
    if z == 20:
        print("Dano Crítico!")
    elif z == 20:
        print("Erro Crítico!")
    print(" ")
    print(" ")

def curar():
    global vida_monstro, vida_jogador, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    w = random.randint(1,10)
    vida_jogador = vida_jogador + w
    print("{} curou {} de vida!".format(b,w))
    print("Vez do Torchic!")
    time.sleep(1)
    z = random.randint(1,20)
    vida_jogador = (vida_jogador - z)
    print("Torchic causou {} de dano!".format(z))
    if z == 20:
        print("Dano Crítico!")
    elif z == 20:
        print("Erro Crítico!")
    print(" ")
    print(" ")
    
def fugir():
    global vida_monstro, vida_jogador, p, s, c, l, q, ac, cu
    f = random.randint(1,20)
    print("Você tirou {} no D20!".format(f))
    if f >= 15:
        print("Você fugiu!")
    else:
        print("Não conseguiu escapar! Precisa de 15 no dado.")
        print("Vez do Torchic!")
        time.sleep(1)
        z = random.randint(1,20)
        vida_jogador = (vida_jogador - z)
        print("Torchic causou {} de dano!".format(z))
        if z == 20:
            print("Dano Crítico!")
        elif z == 20:
            print("Erro Crítico!")
        print(" ")
        print(" ")

def choque():
    global vida_monstro, vida_jogador, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    y = random.randint(1,35)
    vida_monstro = (vida_monstro - y)
    print("{} causou {} de dano com Choque do Trovão!".format(b,y))
    if y == 35:
        print("Dano crítico!")
    elif y == 1:
        print("Erro crítico!")
    print("Vez do Torchic!")
    time.sleep(1)
    z = random.randint(1,20)
    vida_jogador = (vida_jogador - z)
    print("Torchic causou {} de dano!".format(z))
    if z == 20:
        print("Dano Crítico!")
    elif z == 1:
        print("Erro Crítico!")
    print(" ")
    print(" ")  
  
def fogo():
    global vida_monstro, vida_jogador, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    y = random.randint(1,10)
    vida_monstro = (vida_monstro - y)
    print("{} causou {} de dano com Bola de Fogo!".format(b,y))
    if y == 10:
        print("Dano crítico! Mas não muito efetivo.")
    elif y == 1:
        print("Erro crítico!")
    print("Vez do Torchic!")
    time.sleep(1)
    z = random.randint(1,20)
    vida_jogador = (vida_jogador - z)
    print("Torchic causou {} de dano!".format(z))
    if z == 20:
        print("Dano Crítico!")
    elif z == 1:
        print("Erro Crítico!")
    print(" ")
    print(" ") 
        
def agua():
    global vida_monstro, vida_jogador, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    y = random.randint(1,45)
    vida_monstro = (vida_monstro - y)
    print("{} causou {} de dano com Jato De Água!".format(b,y))
    if y == 45:
        print("Dano crítico! Muito efetivo!")
    elif y == 1:
        print("Erro crítico!")
    print("Vez do Torchic!")
    time.sleep(1)
    z = random.randint(1,20)
    vida_jogador = (vida_jogador - z)
    print("Torchic causou {} de dano!".format(z))
    if z == 20:
        print("Dano Crítico!")
    elif z == 1:
        print("Erro Crítico!")    
    print(" ")
    print(" ") 

#Funções dos Pokemons
def charmander():
    global vida_monstro, vida_jogador, p, s, c, l, q, ac, cu
    while vida_monstro > 0 or vida_jogador > 0:
        while q == 1:
            print("{}: {}".format(b,("="*vida_jogador)))
            print("Torchic: {}".format("="*vida_monstro))
            q = int(input("Escolha:\n(1)Atacar\n(2)Curar\n(3)Fugir\n:"))
            if q == 1:
                ac = int(input("(1)Golpear\n(2)Bola de Fogo\n"))
                if ac == 1:
                    ataque()
                    if vida_monstro <= 0 or vida_jogador <= 0:
                        break   
                elif ac == 2:
                    fogo()
                    if vida_monstro <= 0 or vida_jogador <= 0:
                        break 
                else:
                    ac = 1
                    print("Escolha uma opção válida")
                    continue  
            elif q == 2:
                curar()
                break     
            elif q == 3:
                fugir()
                break   
            else:
                print("Escolha uma opção válida!")
                q = 1
                continue
        if vida_monstro <= 0 or vida_jogador <= 0:
            break     

def pikachu():
    global vida_monstro, vida_jogador, p, s, c, l, q, ac, cu
    while vida_monstro > 0 or vida_jogador > 0:
        while q == 1:
            print("{}: {}".format(b,("="*vida_jogador)))
            print("Torchic: {}".format("="*vida_monstro))
            q = int(input("Escolha:\n(1)Atacar\n(2)Curar\n(3)Fugir\n:"))
            if q == 1:
                ac = int(input("(1)Golpear\n(2)Choque do Trovão!\n"))
                if ac == 1:
                    ataque()
                    if vida_monstro <= 0 or vida_jogador <= 0:
                        break   
                elif ac == 2:
                    choque()
                    if vida_monstro <= 0 or vida_jogador <= 0:
                        break 
                else:
                    ac = 1
                    print("Escolha uma opção válida")
                    continue  
            elif q == 2:
                curar()
                q = 1
                if vida_monstro <= 0 or vida_jogador <= 0:
                    break   
            elif q == 3:
                fugir()
                q = 1
                if vida_monstro <= 0 or vida_jogador <= 0:
                    break   
            else:
                print("Escolha uma opção válida!")
                q = 1
                continue
        if vida_monstro <= 0 or vida_jogador <= 0:
            break   
            
def squirtle():
    global vida_monstro, vida_jogador, p, s, c, l, q, ac, cu
    while vida_monstro > 0 or vida_jogador > 0:
        while q == 1:
            print("{}: {}".format(b,("="*vida_jogador)))
            print("Torchic: {}".format("="*vida_monstro))
            q = int(input("Escolha:\n(1)Atacar\n(2)Curar\n(3)Fugir\n:"))
            if q == 1:
                ac = int(input("(1)Golpear\n(2)Jato de Água\n"))
                if ac == 1:
                    ataque()
                    if vida_monstro < 0 or vida_jogador < 0:
                        break   
                elif ac == 2:
                    agua()
                    if vida_monstro < 0 or vida_jogador < 0:
                        break 
                else:
                    ac = 1
                    print("Escolha uma opção válida")
                    continue  
            elif q == 2:
                curar()
                break     
            elif q == 3:
                fugir()
                break   
            else:
                print("Escolha uma opção válida!")
                q = 1
                continue
        if vida_monstro <= 0 or vida_jogador <= 0:
            break                       

#Selecionar o Pokemon            
print(" ")
print(" ")
print("{}Batalha Pokemon!{}".format(('-=-'*5),('-=-'*5)))
print("Você começa!")
while l == 1: 
    l = int(input("Escolha seu Pokemon!\n(1)Pikachu\n(2)Squirtle\n(3)Charmander\nInsira aqui:"))
    if l == 1:
        b = p
        pikachu()
    elif l == 2:
        b = s
        squirtle()
    elif l == 3:
        b = c
        charmander()
    else:
        l = 1
        print("Escolha uma opção válida!")
        continue
    if vida_monstro <= 0 or vida_jogador <= 0:
        break       

#Printar o ganhador
if vida_jogador > vida_monstro:
    print(f"{('-=-')*10}{b} ganhou!{('-=-')*10}")
elif vida_jogador < vida_monstro:
    print(f"{('-=-')*10}{b} perdeu!{('-=-')*10}")  
else:     
    print(f"Empate!")  

#Estética pós-jogo
print(" ")
print(" ")
print("Fim de jogo!")
print(" ")  
