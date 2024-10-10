import random #To roll the dice
import time #To use sleep

#Global variables (Even though it's not the best option, for now, it's how I comfortably do it)
p = 'Pikachu'
s = 'Squirtle'
c = 'Charmander'
l = 1
q = 1
ac = 1
cu = 1
monster_hp = 40
player_hp = 40

#Action functions                
def attack():
    global monster_hp, player_hp, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    y = random.randint(1, 20)
    monster_hp -= y
    print("{} caused {} damage!".format(b, y))
    if y == 20:
        print("Critical hit!")
    elif y == 1:
        print("Critical miss!")
    print("Torchic's turn!")
    time.sleep(1)
    z = random.randint(1, 20)
    player_hp -= z
    print("Torchic caused {} damage!".format(z))
    if z == 20:
        print("Critical hit!")
    elif z == 1:
        print("Critical miss!")
    print(" ")
    print(" ")

def heal():
    global monster_hp, player_hp, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    w = random.randint(1, 10)
    player_hp += w
    print("{} healed {} HP!".format(b, w))
    print("Torchic's turn!")
    time.sleep(1)
    z = random.randint(1, 20)
    player_hp -= z
    print("Torchic caused {} damage!".format(z))
    if z == 20:
        print("Critical hit!")
    elif z == 1:
        print("Critical miss!")
    print(" ")
    print(" ")

def run_away():
    global monster_hp, player_hp, p, s, c, l, q, ac, cu
    f = random.randint(1, 20)
    print("You rolled a {} on the D20!".format(f))
    if f >= 15:
        print("You escaped!")
    else:
        print("Failed to escape! You need a 15 or higher.")
        print("Torchic's turn!")
        time.sleep(1)
        z = random.randint(1, 20)
        player_hp -= z
        print("Torchic caused {} damage!".format(z))
        if z == 20:
            print("Critical hit!")
        elif z == 1:
            print("Critical miss!")
        print(" ")
        print(" ")

def thunderbolt():
    global monster_hp, player_hp, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    y = random.randint(1, 35)
    monster_hp -= y
    print("{} caused {} damage with Thunderbolt!".format(b, y))
    if y == 35:
        print("Critical hit!")
    elif y == 1:
        print("Critical miss!")
    print("Torchic's turn!")
    time.sleep(1)
    z = random.randint(1, 20)
    player_hp -= z
    print("Torchic caused {} damage!".format(z))
    if z == 20:
        print("Critical hit!")
    elif z == 1:
        print("Critical miss!")
    print(" ")
    print(" ")  
  
def fireball():
    global monster_hp, player_hp, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    y = random.randint(1, 10)
    monster_hp -= y
    print("{} caused {} damage with Fireball!".format(b, y))
    if y == 10:
        print("Critical hit! But not very effective.")
    elif y == 1:
        print("Critical miss!")
    print("Torchic's turn!")
    time.sleep(1)
    z = random.randint(1, 20)
    player_hp -= z
    print("Torchic caused {} damage!".format(z))
    if z == 20:
        print("Critical hit!")
    elif z == 1:
        print("Critical miss!")
    print(" ")
    print(" ") 
        
def water():
    global monster_hp, player_hp, p, s, c, l, q, ac, cu
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    y = random.randint(1, 45)
    monster_hp -= y
    print("{} caused {} damage with Water Jet!".format(b, y))
    if y == 45:
        print("Critical hit! Super effective!")
    elif y == 1:
        print("Critical miss!")
    print("Torchic's turn!")
    time.sleep(1)
    z = random.randint(1, 20)
    player_hp -= z
    print("Torchic caused {} damage!".format(z))
    if z == 20:
        print("Critical hit!")
    elif z == 1:
        print("Critical miss!")
    print(" ")
    print(" ") 

#Pokemon functions
def charmander():
    global monster_hp, player_hp, p, s, c, l, q, ac, cu
    while monster_hp > 0 or player_hp > 0:
        while q == 1:
            print("{}: {}".format(b,("="*player_hp)))
            print("Torchic: {}".format("="*monster_hp))
            q = int(input("Choose:\n(1)Attack\n(2)Heal\n(3)Run Away\n:"))
            if q == 1:
                ac = int(input("(1)Strike\n(2)Fireball\n"))
                if ac == 1:
                    attack()
                    if monster_hp <= 0 or player_hp <= 0:
                        break   
                elif ac == 2:
                    fireball()
                    if monster_hp <= 0 or player_hp <= 0:
                        break 
                else:
                    ac = 1
                    print("Choose a valid option")
                    continue  
            elif q == 2:
                heal()
                break     
            elif q == 3:
                run_away()
                break   
            else:
                print("Choose a valid option!")
                q = 1
                continue
        if monster_hp <= 0 or player_hp <= 0:
            break     

def pikachu():
    global monster_hp, player_hp, p, s, c, l, q, ac, cu
    while monster_hp > 0 or player_hp > 0:
        while q == 1:
            print("{}: {}".format(b,("="*player_hp)))
            print("Torchic: {}".format("="*monster_hp))
            q = int(input("Choose:\n(1)Attack\n(2)Heal\n(3)Run Away\n:"))
            if q == 1:
                ac = int(input("(1)Strike\n(2)Thunderbolt!\n"))
                if ac == 1:
                    attack()
                    if monster_hp <= 0 or player_hp <= 0:
                        break   
                elif ac == 2:
                    thunderbolt()
                    if monster_hp <= 0 or player_hp <= 0:
                        break 
                else:
                    ac = 1
                    print("Choose a valid option")
                    continue  
            elif q == 2:
                heal()
                q = 1
                if monster_hp <= 0 or player_hp <= 0:
                    break   
            elif q == 3:
                run_away()
                q = 1
                if monster_hp <= 0 or player_hp <= 0:
                    break   
            else:
                print("Choose a valid option!")
                q = 1
                continue
        if monster_hp <= 0 or player_hp <= 0:
            break   
            
def squirtle():
    global monster_hp, player_hp, p, s, c, l, q, ac, cu
    while monster_hp > 0 or player_hp > 0:
        while q == 1:
            print("{}: {}".format(b,("="*player_hp)))
            print("Torchic: {}".format("="*monster_hp))
            q = int(input("Choose:\n(1)Attack\n(2)Heal\n(3)Run Away\n:"))
            if q == 1:
                ac = int(input("(1)Strike\n(2)Water Jet\n"))
                if ac == 1:
                    attack()
                    if monster_hp < 0 or player_hp < 0:
                        break   
                elif ac == 2:
                    water()
                    if monster_hp < 0 or player_hp < 0:
                        break 
                else:
                    ac = 1
                    print("Choose a valid option")
                    continue  
            elif q == 2:
                heal()
                break     
            elif q == 3:
                run_away()
                break   
            else:
                print("Choose a valid option!")
                q = 1
                continue
        if monster_hp <= 0 or player_hp <= 0:
            break                       

#Select Pokemon            
print(" ")
print(" ")
print("{}Pokemon Battle!{}".format(('-=-'*5),('-=-'*5)))
print("You're up first!")
while l == 1: 
    l = int(input("Choose your Pokemon!\n(1)Pikachu\n(2)Squirtle\n(3)Charmander\nEnter here:"))
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
        print("Choose a valid Pokemon!")
        continue

#Victory or Defeat  
if monster_hp < player_hp:
    print(" ")
    print(" ")
    print("Congratulations, you won!")
else:
    print(" ")
    print(" ")
    print("You were defeated!")
