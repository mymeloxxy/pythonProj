# quiz 03> 커피메뉴 관리프로그램
# 데이터 저장은 딕셔너리로.. {'메뉴명':가격,'coffee':2000}
# 프로그램에서 사용할 메뉴
# 1. 메뉴입력 2. 메뉴수정 3. 메뉴목록 4. 메뉴삭제 5. 프로그램 종료
# - 메뉴입력 : 메뉴명과 가격을 입력받아서 저장(딕셔너리에-같은이름은 덮어씀(키는 중복이 안됨))
# - 메뉴수정 : 메뉴명을 확인하고 있는 메뉴에 가격을 입력받아 수정
# - 메뉴목록 : 저장된 메뉴명과 가격을 출력(천단위구분기호표기), 메뉴명 순서대로 출력
# - 메뉴삭제 : 메뉴명을 확인하고 있는 메뉴에서 삭제
# - 프로그램 종료 : 프로그램을 종료하는 메세지를 출력하고 종료(while True-무한반복 가 들어가야됨)
# - 메뉴1-5까지만 입력받고 다른 값이 들어오면 관련 에러 메세지를 출력한다.
# - 가격은 숫자로 입력해야됨

def menu_input():
    print('현재메뉴 :',list(menu.keys()))
    name = input('추가할 메뉴명을 입력하세요 >>>')
    price = 'a'
    while not price.isdecimal():
        price = input('추가할 메뉴의 가격을 입력하세요 >>>')
    menu[name]=int(price)

def menu_update():
    print('현재메뉴 :',list(menu.keys()))
    name = ''
    while not name in menu.keys():
        name = input('수정할 메뉴명을 입력하세요 >>>')
    price = 'a'
    while not price.isdecimal():
        price = input('수정할 메뉴의 가격을 입력하세요 >>>')
    menu[name]=int(price)

def menu_list():
    print('----- menu -----')
    for item in sorted(menu.items(),key=lambda data:data[1],reverse=True):
        print(f'{item[0]} : {item[1]:,}')

def menu_delete():
    print('현재메뉴 :',list(menu.keys()))
    name = ''
    while not name in menu.keys():
        name = input('삭제할 메뉴명을 입력하세요 >>>')
    del menu[name]

# 분리할때는 import사용/import뒤 파일명/as=별칭 붙이기

import func_basic as fb
menu = {'아이스아메리카노':3000,'라떼':4000,'코코아':3500}
while True:
    choice = input('''
----------------------------------------------------------
1. 메뉴입력 2. 메뉴수정 3. 메뉴목록 4 메뉴삭제 5. 프로그램종료
----------------------------------------------------------
메뉴선택 >>> ''')
    if choice == '1':
        fb.menu_input(menu)
    elif choice == '2':
        fb.menu_update(menu)
    elif choice == '3':
        fb.menu_list(menu)
    elif choice == '4':
        fb.menu_delete(menu)
    elif choice == '5':
        print('프로그램을 종료합니다.')
        break
    else:
        print('메뉴를 잘못 선택 하였습니다.')