import random
import time

# class

# 공통 스탯 부분
class Stat:
    HP = None
    ATK = None
    DEF = None
    SPD = None

    def attack(self, enemy_hp, enemy_def):
        calcul = (self.ATK * random.randint(1, 4)) - enemy_def # 난수 공격
        if calcul <= 0: # 최소 공격
            calcul = 1
        result = enemy_hp - calcul # 결과
        return result, calcul
    
    def status(self, name): #상태창
        print("-"*40)
        print("%s의 상태" %name)
        print("체력 : %d" %self.HP)
        print("공격력 : %d" %self.ATK)
        print("방어력 : %d" %self.DEF)
        print("민첩 : %d" %self.SPD)
        print("-"*40)


# 플레이어 class
class Human(Stat):
    global Name
    HP = 50
    ATK = 10
    DEF = 10
    SPD = 10

    def training(self, how): #트레이닝 하기
        if how == '1':
            self.HP += 10
            print("체력이 10 올랐다 !")
            time.sleep(1)
        elif how == '2':
            self.ATK += 2
            print("공격력이 2 올랐다 !")
            time.sleep(1)
        elif how == '3':
            self.DEF += 2
            print("방어력이 2 올랐다 !")
            time.sleep(1)
        elif how == '4':
            self.SPD += 2
            print("민첩이 2 올랐다 !")
            time.sleep(1)


# 몬스터 고블린
class Goblin(Stat):
    #스탯 난수 생성
    HP = random.randrange(30, 50)
    ATK = random.randrange(7, 13)
    DEF = random.randrange(5, 10)
    SPD = random.randrange(8, 12)


# def
# 메인 선택
def choose():
    trainingTime = 1 # 트레이닝은 한번만
    while True:
        que = input("\n무엇을 하시겠습니까?\n1.모험\n2.상태\n3.트레이닝\n")
    
        if que == "1": # 1번 모험
            print("")
            time.sleep(0.5)
            print("모험을 떠납니다.\n")
            time.sleep(0.5)
            break

        elif que == "2": # 2번 상태
            print("")
            time.sleep(0.5)
            player.status() # 상태창 불러오기
            time.sleep(2)
            continue

        elif que == "3": # 3번 트레이닝
            print("")
            time.sleep(0.5)
            while True:
                if trainingTime == 0: # 트레이닝을 이미 했다면
                    print("트레이닝을 이미 완료 하였습니다.")
                    time.sleep(1)
                    break
                else: # 처음 트레이닝을 한다면
                    que_train = input("어떤 트레이닝을 하시겠습니까?\n1.체력\n2.공격력\n3.방어력\n4.민첩\n당신의 선택은? : ")
                    while True:
                        if que_train == '1' or '2' or '3' or '4':
                            print("")
                            time.sleep(1)
                            break
                        else:
                            print("다시 입력해주십시오.\n")
                            time.sleep(1)
                    player.training(que_train) # 트레이닝 하기
                    trainingTime = 0
                    break

# 몬스터 나타났을 때
def vsMonster(monsterClass, monsterName):
    monster = monsterClass() # 몬스터 클래스 부여하기
    monsterName = monsterName # 몬스터의 이름 (문자열)

    print("%s이(가) 나타났다 !"%monsterName)

    while True:
        time.sleep(1)
        
        monster.status(monsterName) #몬스터 상태 보여주기
        player.status(Name) #플레이어 상태 보여주기
        player_que = input("%s(은)는 무엇을 할까?\n1.공격\n2.도망가기\n"%Name)

        if player_que == "1": #공격의 경우
            print("")
            if player.SPD >= monster.SPD: #플레이어의 민첩이 몬스터의 민첩보다 높을 때
                monster.HP, player_dmg = player.attack(monster.HP, monster.DEF)
                print("%s에게 %d만큼의 대미지를 주었다 !\n"%(monsterName,player_dmg)) #플레이어의 공격
                time.sleep(1)

                if monster.HP <= 0: # 몬스터의 HP가 0보다 낮다면
                    print("%s(와)과의 싸움에서 승리했다 !\n"%monsterName)
                    time.sleep(1)
                    break

                print("%s의 공격!\n"%monsterName) #몬스터의 공격
                time.sleep(1)
                player.HP, monster_dmg = monster.attack(player.HP, player.DEF)
                print("%s에게 %d만큼의 대미지를 입었다 !\n"%(monsterName, monster_dmg))
                
                if player.HP <= 0: # 플레이어의 HP가 0보다 낮다면
                    print("%s는 쓰러졌다 !\n" %Name)
                    time.sleep(1)
                    break
                else:
                    time.sleep(1)
                    continue

            else: # 몬스터의 민첩이 플레이어의 민첩보다 높을 때
                print("%s의 공격!\n"%monsterName) # 몬스터의 공격
                time.sleep(1)
                player.HP, monster_dmg = monster.attack(player.HP, player.DEF)
                print("%s에게 %d만큼의 대미지를 입었다 !\n"%(monsterName, monster_dmg))
                time.sleep(1)

                if player.HP >= 0: # 플레이어의 HP가 0보다 높다면
                    monster.HP, player_dmg = player.attack(monster.HP, monster.DEF)
                    print("%s에게 %d만큼의 대미지를 주었다 !\n"%(monsterName, player_dmg)) # 플레이어의 공격
                    
                    if monster.HP <= 0: # 몬스터의 HP가 0보다 낮다면
                        print("%s(와)과의 싸움에서 승리했다 !\n"%monsterName)
                        time.sleep(1)
                        break 
                    else: # 몬스터의 HP가 0보다 높다면
                        continue
                        
                else:
                    print("%s(은)는 쓰러졌다 !\n" %Name)
                    time.sleep(1)
                    break

        if player_que == "2": # 도망가기
            
            if player.SPD >= monster.SPD: # 플레이어가 빠르다면
                print("무사히 도망쳤다 !\n")
                time.sleep(1)
                break

            else: # 몬스터가 빠르다면
                print("도망치지 못하였다 !\n")
                time.sleep(1)
                continue
    
    
# main
Name = input("당신의 이름을 입력해주세요. : ")
print("%s(이)가 모험을 시작했다!"%Name)
player = Human()
choose()
vsMonster(Goblin, "고블린")

print("플레이 해주셔서 감사합니다.")