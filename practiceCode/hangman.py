"""def at(a,b):
    if a<=4:
        print("@"*a,"^"*b)
        at(b,a*b)
    else:
        return
at(1,2)"""
"""
def number(a):
    if a>=3000 and a<=5000:
        return True
print(number())
"""
'''class soccer_player:
    def __init__(self,name,age,sex,weight,position):
        self.name=name
        self.age=age
        self.sex=sex
        self.weight=weight
        self.position=position
    def jump(self):
        print("멍")
    def sleep(self):
        self.age+=1
    def shoot(self):
        print('뻥')
    def change(self,new_position):
        self.position=new_position
        print(self.position)
player=soccer_player('호날두',20,'male',80,'st')
player.change('mf')

class soccer_team:
    def __init__(self,name,coach):
        self.name=name
        self.coach=coach
        self.player_list=[]
    def add_player(self,player):
        self.player_list.append(player)
    def print_info(self):
        print(self.name)
        for i in self.player_list:
            print(i.shoot())
team=soccer_team('리버풀','지단')
team.add_player(player)
team.print_info()
dogs=dog('도지',3,'male',5)
dogs.jump()
dogs.sleep
'''
'''
class basketball_player:
    def __init__(self,name,age,height,weight,position):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.position=position
    def shoot(self):
        print('철썩')
        print(self.name,'가 슛을 쐈습니다')
class basketball_team:
    def __init__(self,name,coach):
        self.name=name
        self.coach=coach
        self.player_list=[]
    def add_player(self,player):
        self.player_list.append(player)
    def print_info(self):
        print(self.name)
        for i in self.player_list:
            print(i.name)
player=basketball_player('코비',25,198,95,'SG')
player.shoot()
team=basketball_team('레이커스','리버스')
team.add_player(player)
team.print_info()
'''
'''
class car:
    def __init__(self,number,size,color):
        self.number=number
        self.size=size
        self.color=color
    def print_info(self):
        print(self.number,self.size,self.color)
    def Bamm(self):
        print('빵')

class taxi(car):
    def __init__(self,number,size,color,charge,local):
        super().__init__(number,size,color)
        self.charge=charge
        self.local=local
    def print_info(self):
        super().print_info()
        print(self.charge,self.local)
taxi1=taxi(1234,5,'orange',5000,'서울')
taxi1.Bamm()
taxi1.print_info()

class elec(car):
    def __init__(self,number,size,color,battery_duration):
        super().__init__(number,size,color)
        self.battery_duration=battery_duration
    def print_info(self):
        super().print_info()
        print(self.battery_duration)
    def Bamm(self):
        print('찌릿찌릿')
elec_car=elec(1111,5,'white',100)
elec_car.Bamm()
'''
'''
class dog:
    def __init__(self,size,color,food):
        self.size=size
        self.color=color
        self.food=food
    def print_info(self):
        print(self.size,self.color,self.food)
    def bark(self):
        print('멍')

class wolf(dog):
    def __init__(self,size,color,food,pack):
        super().__init__(size,color,food)
        self.pack=pack
    def print_info(self):
        super().print_info()
        print(self.pack)
    def bark(self):
        print('howling')

dog1=dog('small','brown','사료')
wolf1=wolf('big','black','고기',10)
dog1.bark()
wolf1.bark()
wolf1.size='giant'
'''
'''
from marine import marine

from GameManager import game_manager
marine1=marine()
GM=game_manager(marine1)
GM.game_start()
'''
'''
class person:
    def __init__(self,height,weight,sex,age,name):
        self.height=height
        self.weight=weight
        self.sex=sex
        self.age=age
        self.name=name
    def print_info(self):
        print(self.height,self.weight,self.sex,self.age,self.name)
    def eat(self):
        self.weight=self.weight+1
    def sleep(self):
        self.age=self.age+1

class student(person):
    def __init__(self,height,weight,sex,age,name,major,grade,score):
        super().__init__(height,weight,sex,age,name)
        self.major=major
        self.grade=grade
        self.score=score

    def study(self):
        self.score=self.score+1

    def eat(self):
        self.weight=self.weight+1
        self.height=self.height+1

    def print_info(self):
        super().print_info()
        print(self.major,self.grade,self.score)

person1=person(170,60,'male',30,'bob')
student1=student(165,50,'female',17,'Jin','Science',11,97)
person1.eat()
student1.eat()
person1.print_info()
student1.print_info()
'''

class hangman:
    def __init__(self,answer):
        self.answer=answer
        self.list1=[]
        for i in range(len(self.answer)):
            self.list1.append('F')
        self.try1=len(self.answer)+2

    def PrintCurrent(self):
        for i in range(len(self.list1)):
            if self.list1[i]=='F':
                print('= ',end="")
            if self.list1[i]=='T':
                print(self.answer[i] ,end=' ')
        print(self.try1)


    def AnswerCheck(self,p):
        tryCheck=False
        for i in range(len(self.answer)):
            if self.answer[i]==p:
                self.list1[i]='T'
                tryCheck=True
        if tryCheck==False:
            self.try1=self.try1-1

    def gameOver(self):
        if self.try1==0:
            return True
        else:
            return False

    def winCheck(self):
        for i in range(len(self.list1)):
            if self.list1[i]=="F":
                return False

        return True






h1=hangman("apple")


while((h1.gameOver() or h1.winCheck())==False):
    a=input("알파벳을 입력:")
    h1.AnswerCheck(a)
    h1.PrintCurrent()
