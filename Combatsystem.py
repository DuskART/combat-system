import random
import time

class Fighter():
        
        
    def __init__(self, name, pace, endurance, power, chin, const, attack, defence, ment):
        self.name = name
        self.age = 19
        # atributes
        self.pace = pace
        self.endurance = endurance
        self.power = power
        self.chin = chin
        self.const = const
        self.attack = attack
        self.defence = defence
        self.ment = ment
        # money,experience etc
        self.experience = 0
        self.money = 10000
        self.rank = random.randint(1000, 1400)
        self.overal = (((pace + endurance + power + chin + const + attack + defence + ment) / 8) * 5) + 10
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.ko = 0
        self.record = [self.wins, self.loses, self.draws]
        # modes
    def defensivemodeON(self):
        pass
    def defensivemodeOFF(self):
        pass

    def ofensivevemodeON(self):
        pass
    def ofensivevemodeOFF(self):
        pass

    def suicidemodeON(self):
        pass
    def suicidemodeOFF(self):
        pass



def iniciativa(f1, f2):
    luck1 = random.randint(0, 5)
    luck2 = random.randint(0, 5)
    if ((f1.pace - (f1.pace/10)**2) + luck1) > ((f2.pace - (f2.pace/10)**2) + luck2):
        if f1.const > 0:
            print(f"{f1.name} útočí..")
            f1.pace -= 1 / f1.endurance
            return 1
    elif ((f2.pace - (f2.pace/10)**2) + luck2) > ((f1.pace - (f1.pace/10)**2) + luck1):
        if f2.const > 0:
            print(f"{f2.name} útočí..")
            f2.pace -= 1 / f2.endurance
            return 2
    else:
        print("nikdo")
        return 0

#
#                        pace,end,pow,chn,con,att,def,ment
#                         op       o           OP  Op  

#                        pace,end,pow,chn,con,att,def,ment
player1 = Fighter("Duska", 10, 10, 10, 10, 10, 10, 10, 10)

#                        pace,end,pow,chn,con,att,def,ment
cpu = Fighter    ("cpu",   10, 10, 10, 10, 10, 10, 10, 10)

#                               pace,end,pow,chn,con,att,def,ment
wilder = Fighter    ("Wilder",    10, 13, 18, 14, 14, 13, 11, 15)

#                               pace,end,pow,chn,con,att,def,ment
fury = Fighter    ("Tyson Fury",  10, 10, 11, 14, 14, 14, 16, 15)

#                               pace,end,pow,chn,con,att,def,ment
aj = Fighter    ("AJ",            10, 13, 16, 12, 14, 14, 11, 13)

#                               pace,end,pow,chn,con,att,def,ment
ali = Fighter    ("Ali",          10, 14, 12, 15, 12, 11, 17, 13)



#                               pace,end,pow,chn,con,att,def,ment
breazeale = Fighter("Breazeale",   9, 11, 13, 11, 14, 12, 13, 13)







playeracts = 0
cpuacts = 0
p_score = 0
cpu_score = 0

def fight(f1, f2):
    playeracts = 0   
    cpuacts = 0
    s_pacef1 = f1.pace
    s_constf1 = f1.const
    s_pacef2 = f2.pace
    s_constf2 = f2.const

    p_score = 0
    cpu_score = 0

    print(f"_____{f1.name}  vs  {f2.name}_____")
    time.sleep(0.1)
    for round in range(12):
        b1 = 0
        b2 = 0
        ko = 0
        tko = 0
        print(f"_____{round + 1}. round______")
        for situation in range(10):
            i = iniciativa(f1, f2)
            # akce 1
            if i == 1:
                playeracts += 1
                b1 += 0.33
                # trefa1
                luckA = random.randint(0, 2)
                luckD = random.randint(2, 5) 
                if (f1.attack) + luckA > (10 * (f2.defence/12)) + luckD:
                    print(f"{f1.name} pěkná trefa..")
                    b1 += 2
                    f2.const = f2.const - (f1.power/22)*1.33
                    # knockdown1
                    luckPow = random.randint(0, 1)
                    luckChin = random.randint(1, 6)
                    if f1.power + luckPow > f2.chin + luckChin:
                        print(f"{f1.name} ho posílá k zemi....")
                        time.sleep(0.1)
                        f2.const = f2.const - (f1.power/22)*3
                        b1 += 10
                        # knockout1
                        luckPowKO = random.randint(0, 1)
                        luckChinKO = random.randint(4, 6)
                        if f1.power + luckPowKO > f2.chin + luckChinKO:
                            print(f"Hrozná rána, {f2.name} je úplně mimo....")
                            time.sleep(0.3)
                            ko = 1
                            break
                            
                        
            # akce 2    
            elif i == 2:
                cpuacts += 1
                b2 += 0.33
                # trefa2
                luckA = random.randint(0, 2)
                luckD = random.randint(2, 5)
                if (f2.attack) + luckA > (10 * (f1.defence/12)) + luckD:
                    print(f"{f2.name} pěkná trefa..")
                    b2 += 2
                    f1.const = f1.const - (f2.power/22)*1.33
                    # knockdown2
                    luckPow = random.randint(0, 1)
                    luckChin = random.randint(1, 6)
                    if f2.power + luckPow > f1.chin + luckChin:
                        print(f"{f2.name} ho posílá k zemi....")
                        time.sleep(0.1)
                        f1.const = f1.const - (f2.power/22)*3
                        b2 += 10
                        # knockout2
                        luckPowKO = random.randint(0, 1)
                        luckChinKO = random.randint(4, 6)
                        if f2.power + luckPowKO > f1.chin + luckChinKO:
                            print(f"Hrozná rána, {f1.name} je úplně mimo....")
                            time.sleep(0.3)
                            ko = 2
                            break





        # checker po konci kola
        if f1.const < 0:
            print(f"{f2.name} vítězí na TKO v {round + 1}.kole.. ")
            f2.wins += 1
            f2.ko += 1
            f1.loses += 1
            tko = 2
            break
        elif f2.const < 0:
            print(f"{f1.name} vítězí na TKO v {round + 1}.kole.. ")
            f1.wins += 1 
            f1.ko += 1
            f2.loses += 1
            tko = 1
            break
        if ko == 1:
            print(f"{f1.name} vítězí na KO v {round + 1}.kole.. ")
            f1.wins += 1
            f1.ko += 1
            f2.loses += 1
            break
        elif ko == 2:
            print(f"{f2.name} vítězí na KO v {round + 1}.kole.. ")
            f2.wins += 1
            f2.ko += 1
            f1.loses += 1
            break

# score system

        if b1 > b2:
            p_score += 10
            cpu_score += 9
        if b2 > b1:
            cpu_score += 10
            p_score += 9
        if b1 == b2:
            p_score += 10
            cpu_score += 10
# save pro pristi fight
    print("______________________")
    f1.pace = s_pacef1 
    f1.const = s_constf1
    f2.pace = s_pacef2 
    f2.const = s_constf2

    if tko == 1 or tko == 2:
        print("konec")  
    elif ko == 1 or ko == 2:
        print("snad bude v pořádku....")
    elif p_score > cpu_score:
        print(f"{f1.name} vítězí na body v poměru {p_score} ku {cpu_score}")
        f1.wins += 1
        f2.loses += 1
    elif cpu_score > p_score:
        print(f"{f2.name} vítězí na body v poměru {cpu_score} ku {p_score}")
        f2.wins += 1
        f1.loses += 1
    elif p_score == cpu_score:
        print(f"Zápas končí jako remíza v poměru {p_score} ku {cpu_score} na body")
        f1.draws += 1
        f2.draws += 1

# výpis na konci fightu
    print("___________________")
    print(f"player akcí: {playeracts}")
    print(f"cpu akcí: {cpuacts}")
    print("___________________")
    print(f"player score: {p_score}")
    print(f"cpu score: {cpu_score}")



fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)
fight(player1, cpu)

fight(wilder, fury)
fight(fury, aj)
fight(aj, wilder)

# fight(fury, aj)
# fight(breazeale, fury)
# fight(player1, wilder)
# fight(player1, fury)







# print(f"player pace: {player1.pace}")
# print(f"cpu pace: {cpu.pace}")
print("___________________")
print(f"player constitution: {player1.const}")
print(f"cpu constitution: {cpu.const}")
print("___________________")

print(f"wins: {player1.wins}")
print(f"loses: {player1.loses}")
print(f"draws: {player1.draws}")
print(f"kos: {player1.ko}")

