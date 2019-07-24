import random

nonskills = {
 '__class__',
 '__del__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'agile',
 'cure',
 'exp',
 'height',
 'hp',
 'level',
 'name',
 'property',
 'weight'            
}

class Poketmon:
    
    def __init__(self,name):
        self.weight = str(random.randint(20,1000)) + 'kg'
        self.height = str(random.randint(20,250)) + 'm'
        self.name = name
        self.level = 5
        self.hp = self.level * 20
        self.exp = 0
        self.agile = random.uniform(0,0.5)
    
    def __del__(self):
        print(f'{self.name}은(는) 사망했다.')
    
    def crush(self, other):
        dmg = 10
        print(f'가라! {self.name}! 몸통박치기!!')
        if other.hp <= 0:
            print('워워, 이미 죽은상대는 공격할 수 없습니다!!')
        else:
            if random.random() > other.agile:
                other.hp -= dmg
                print('명중했다!')
                print(f'{other.name}의 hp가 {other.hp + dmg} => {other.hp}가 되었다.')
                if other.hp <= 0:
                    print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                    self.exp += other.level * 15
                    print(f'경험치 {other.level*15}를 획득했다.')
                    if self.exp >= self.level * 100:
                        self.exp = self.exp - self.level * 100
                        self.level += 1
                        print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                        print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
                        
    def cure(self):
        print(f'{self.name}을(를)회복시켜줘!')
        print('기력이 되살아난다.')
        print('............')
        print(f'{self.name}이(가) 모든 기력을 회복했다.')
        self.hp = self.level * 20

    def bark(self,other):
        print(f'{self.name}(이)가 {other.name}을(를) 위협했다!')
        
class WaterPoketmon(Poketmon):
    
    def __init__(self,name):
        super().__init__(name)
        self.property = 'water'
    
    def skill(self, other):
        dmg = 25
        print(f'가라! {self.name}! 물대포발사!!')
        if other.hp <= 0:
            print('워워, 이미 죽은상대는 공격할 수 없습니다!!')
        else:
            if random.random() > other.agile:
                if other.property == 'fire':
                    other.hp -= dmg * 2
                    print('치명적 데미지! 상당한 효과가 있었다!!')
                    print(f'{other.name}의 hp가 {other.hp + dmg * 2} => {other.hp}가 되었다.')
                    if other.hp <= 0:
                        print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                        self.exp += other.level * 15
                        print(f'경험치 {other.level*15}를 획득했다.')
                        if self.exp >= self.level * 100:
                            self.exp = self.exp - self.level * 100
                            self.level += 1
                            print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                            print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
                else:
                    other.hp -= dmg
                    print('명중했다!')
                    print(f'{other.name}의 hp가 {other.hp + dmg} => {other.hp}가 되었다.')
                    if other.hp <= 0:
                        print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                        self.exp += other.level * 15
                        print(f'경험치 {other.level*15}를 획득했다.')
                        if self.exp >= self.level * 100:
                            self.exp = self.exp - self.level * 100
                            self.level += 1
                            print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                            print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
            else:
                print(f'이런! {other.name}(이)가 공격을 회피했다.')
                print('아무일도 일어나지 않았다.')
    
    def ult(self, other):
        dmg = 60
        print(f'가라! {self.name}! 포세이돈!!!!')
        if other.hp <= 0:
            print('워워, 이미 죽은상대는 공격할 수 없습니다!!')
        else:
            if other.property == 'fire':
                other.hp -= dmg * 2
                print('치명적 데미지! 상당한 효과가 있었다!!')
                print(f'{other.name}의 hp가 {other.hp + dmg * 2} => {other.hp}가 되었다.')
                if other.hp <= 0:
                    print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                    self.exp += other.level * 15
                    print(f'경험치 {other.level*15}를 획득했다.')
                    if self.exp >= self.level * 100:
                        self.exp = self.exp - self.level * 100
                        self.level += 1
                        print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                        print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
            else:
                other.hp -= dmg
                print('명중했다!')
                print(f'{other.name}의 hp가 {other.hp + dmg} => {other.hp}가 되었다.')
                if other.hp <= 0:
                    print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                    self.exp += other.level * 15
                    print(f'경험치 {other.level*15}를 획득했다.')
                    if self.exp >= self.level * 100:
                        self.exp = self.exp - self.level * 100
                        self.level += 1
                        print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                        print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
        
    def __repr__(self):
        return f'name : {self.name} \nweight : {self.weight} height : {self.height}\nlevel : {self.level} hp : {self.hp}\nexp : {self.exp} agile : {self.agile}\n skills :{set(dir(self)) - nonskills}'
                        


class FirePoketmon(Poketmon):
    
    def __init__(self,name):
        super().__init__(name)
        self.property = 'fire'
    
    def skill(self, other):
        dmg = 25
        print(f'가라! {self.name}! 파이어볼!!')
        if other.hp <= 0:
            print('워워, 이미 죽은상대는 공격할 수 없습니다!!')
        else:
            if random.random() > other.agile:
                if other.property == 'tree':
                    other.hp -= dmg * 2
                    print('치명적 데미지! 상당한 효과가 있었다!!')
                    print(f'{other.name}의 hp가 {other.hp + dmg * 2} => {other.hp}가 되었다.')
                    if other.hp <= 0:
                        print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                        self.exp += other.level * 15
                        print(f'경험치 {other.level*15}를 획득했다.')
                        if self.exp >= self.level * 100:
                            self.exp = self.exp - self.level * 100
                            self.level += 1
                            print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                            print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
                else:
                    other.hp -= dmg
                    print('명중했다!')
                    print(f'{other.name}의 hp가 {other.hp + dmg} => {other.hp}가 되었다.')
                    if other.hp <= 0:
                        print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                        self.exp += other.level * 15
                        print(f'경험치 {other.level*15}를 획득했다.')
                        if self.exp >= self.level * 100:
                            self.exp = self.exp - self.level * 100
                            self.level += 1
                            print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                            print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
            else:
                print(f'이런! {other.name}(이)가 공격을 회피했다.')
                print('아무일도 일어나지 않았다.')
    
    def ult(self, other):
        dmg = 60
        print(f'가라! {self.name}! 볼케이노!!!!')
        if other.hp <= 0:
            print('워워, 이미 죽은상대는 공격할 수 없습니다!!')
        else:
            if other.property == 'tree':
                other.hp -= dmg * 2
                print('치명적 데미지! 상당한 효과가 있었다!!')
                print(f'{other.name}의 hp가 {other.hp + dmg * 2} => {other.hp}가 되었다.')
                if other.hp <= 0:
                    print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                    self.exp += other.level * 15
                    print(f'경험치 {other.level*15}를 획득했다.')
                    if self.exp >= self.level * 100:
                        self.exp = self.exp - self.level * 100
                        self.level += 1
                        print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                        print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
            else:
                other.hp -= dmg
                print('명중했다!')
                print(f'{other.name}의 hp가 {other.hp + dmg} => {other.hp}가 되었다.')
                if other.hp <= 0:
                    print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                    self.exp += other.level * 15
                    print(f'경험치 {other.level*15}를 획득했다.')
                    if self.exp >= self.level * 100:
                        self.exp = self.exp - self.level * 100
                        self.level += 1
                        print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                        print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
    
    def __repr__(self):
        return f'name : {self.name} \nweight : {self.weight} height : {self.height}\nlevel : {self.level} hp : {self.hp}\nexp : {self.exp} agile : {self.agile}\n skills :{set(dir(self)) - nonskills}'
                        
class ElectricPoketmon(Poketmon):
    
    def __init__(self,name):
        super().__init__(name)
        self.property = 'electricity'
    
    def skill(self, other):
        dmg = 25
        print(f'가라! {self.name}! 100만 볼트!!!')
        if other.hp <= 0:
            print('워워, 이미 죽은상대는 공격할 수 없습니다!!')
        else:
            if random.random() > other.agile:
                if other.property == 'water':
                    other.hp -= dmg * 2
                    print('치명적 데미지! 상당한 효과가 있었다!!')
                    print(f'{other.name}의 hp가 {other.hp + dmg * 2} => {other.hp}가 되었다.')
                    if other.hp <= 0:
                        print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                        self.exp += other.level * 15
                        print(f'경험치 {other.level*15}를 획득했다.')
                        if self.exp >= self.level * 100:
                            self.exp = self.exp - self.level * 100
                            self.level += 1
                            print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                            print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
                else:
                    other.hp -= dmg
                    print('명중했다!')
                    print(f'{other.name}의 hp가 {other.hp + dmg} => {other.hp}가 되었다.')
                    if other.hp <= 0:
                        print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                        self.exp += other.level * 15
                        print(f'경험치 {other.level*15}를 획득했다.')
                        if self.exp >= self.level * 100:
                            self.exp = self.exp - self.level * 100
                            self.level += 1
                            print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                            print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
            else:
                print(f'이런! {other.name}(이)가 공격을 회피했다.')
                print('아무일도 일어나지 않았다.')
    
    def ult(self, other):
        dmg = 60
        print(f'가라! {self.name}! 토르의 번개!!!!')
        if other.hp <= 0:
            print('워워, 이미 죽은상대는 공격할 수 없습니다!!')
        else:
            if other.property == 'water':
                other.hp -= dmg * 2
                print('치명적 데미지! 상당한 효과가 있었다!!')
                print(f'{other.name}의 hp가 {other.hp + dmg * 2} => {other.hp}가 되었다.')
                if other.hp <= 0:
                    print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                    self.exp += other.level * 15
                    print(f'경험치 {other.level*15}를 획득했다.')
                    if self.exp >= self.level * 100:
                        self.exp = self.exp - self.level * 100
                        self.level += 1
                        print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                        print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
            else:
                other.hp -= dmg
                print('명중했다!')
                print(f'{other.name}의 hp가 {other.hp + dmg} => {other.hp}가 되었다.')
                if other.hp <= 0:
                    print(f'{other.name}이(가) 전투불능상태에 빠졌다')
                    self.exp += other.level * 15
                    print(f'경험치 {other.level*15}를 획득했다.')
                    if self.exp >= self.level * 100:
                        self.exp = self.exp - self.level * 100
                        self.level += 1
                        print(f'{self.name}의 레벨이 {self.level-1}에서 {self.level}로 올랐다!')
                        print(f'{self.name}의 현재 경험치는 {self.exp}. 레벨업까지 {self.level*100 - self.exp}남았다.')
    
    def __repr__(self):
        return f'name : {self.name} \nweight : {self.weight} height : {self.height}\nlevel : {self.level} hp : {self.hp}\nexp : {self.exp} agile : {self.agile}\n skills :{set(dir(self)) - nonskills}'
                        
                    
def Poketfight(p1,p2):
    act= ['crush','skill','ult','cure','bark']
    while True:
        print(f'\n-----{p1.name}-------')
        act1 = random.choice(act)
        if act1 == act[0]:
            p1.crush(p2)
        elif act1 == act[1]:
            p1.skill(p2)
        elif act1 == act[2]:
            p1.ult(p2)
        elif act1 == act[4]:
            p1.bark(p2)
        else:
            p1.cure()
        print(f'\n-----{p2.name}-------')
        act2 = random.choice(act)
        if act2 == act[0]:
            p2.crush(p1)
        elif act2 == act[1]:
            p2.skill(p1)
        elif act2 == act[2]:
            p2.ult(p1)
        elif act2 == act[4]:
            p2.bark(p1)
        else:
            p2.cure()
        if p1.hp <= 0:
            print(f'{p2.name}(이)가 승리했다!')
            break
        if p2.hp <= 0:
            print(f'{p1.name}(이)가 승리했다!')
            break


pikachu = ElectricPoketmon('piakchu')
Firetail = FirePoketmon('Firetail')
Kobuggi = WaterPoketmon('Kobuggi')

for i in range(10):
    pikachu.cure()
    print('')
    Firetail.cure()
    print('')
    print(f'fight #{i+1}')
    Poketfight(pikachu,Firetail)
    print('')
