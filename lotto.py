import random

#필요한 리스트 선언

list_number = [] #추첨되는 정규 번호 
list_bonus = [] #추첨되는 보너스 번호

#정규 번호 추첨식
for i in range(1, 7) :
    match_val = random.randrange(1, 46)
    while match_val in list_number :
        match_val = random.randrange(1, 46)
    list_number.append(match_val)
#보너스 번호 추첨식
for i in range(1) :
    match_val = random.randrange(1, 46)
    while match_val in list_bonus :
        match_val = random.randrange(1, 46)
    list_bonus.append(match_val)
#보너스 번호 중복 제거
while list_bonus[0] in list_number : #만약 list_number의 숫자가 list_bonus에 있으면
    del list_bonus[0] #list_bonus를 지워준다.
    list_bonus.append(match_val) #list_bonus 재추첨 (반복)

print("로또번호는", list_number, "이고, 보너스 번호는", list_bonus)



list_mynum = []


count = 0
while count < 6 :
    v_input = int(input(f'{count+1}번째 숫자 입력 >>'))

    if count == 0 :
        list_mynum.append(v_input)
        count += 1
    else :
        if v_input in list_mynum :
            print(f'{v_input}은 이미 존재합니다.')
        else :
            list_mynum.append(v_input)
            count += 1

print(list_mynum)

SetNum = set(list_number) #list_number 를 set 타입으로
Setmynum = set(list_mynum) #list_mynum 을 set 타입으로
SetBonus = set(list_bonus) #list_bonus 를 set 타입으로  
SetAnd = SetNum & Setmynum #추첨번호와 내 번호를 비교하여 교집합을 구함
SetBD = Setmynum & SetBonus #내 번호와 보너스 번호의 교집합을 구함


if SetNum == Setmynum : #추첨번호와 내 번호가 모두 같으면 1등
    print('1등')
elif len(SetAnd) == 5 and len(SetBD) == 1 : #추첨번호와 내 번호의 교집합의 갯수가 5개이고, 보너스 번호가 맞으면 2등
    print('2등')
elif len(SetAnd) == 5 : #추첨번호와 내 번호의 교집합이 5개이면 3등
    print('3등')
elif len(SetAnd) == 4 : #추첨번호와 내 번호의 교집합이 4개면 4등
    print('4등')
elif len(SetAnd) == 3 : #추첨번호와 내 번호의 교집합이 3개면 5등
    print('5등')
else :                  #나머지 경우 꽝
    print('꽝입니다')