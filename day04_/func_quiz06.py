# quiz 06>
# 앞에 타자 게임을 활용 while True사용
# - 1. 문제추가 2. 타자게임 3. 등수리스트 4. 종료하기
# - 문제추가 후 데이터는 파일로 저장
# - 문제추가는 단어를 입력받아서 중복되지 않도록 않게 추가, 종료 전까지 계속 추가 작업 진행
# -print(random.sample(range(1,46),6))
# - 타자게임은 시간을 체크하고, 걸린시간을 사용자명과 함께 저장 (딕셔너리로 저장(dic) = 등수데이터)
# - 등수리스트는 걸리시간이 적은 순서대로 정렬해서 출력( _.sort-> print)
# - 종료하기는 등수데이터를 저장하고 진행
# - 프로그램이 시작될 때 문제와 등수정보를 읽어 옴

# word = ["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
# rank = {'aaa':10.111}

import func_basic1 as fb1

word = fb1.load_save_data('word.json','r')
rank = fb1.load_save_data('rank.json','r')

while True:
    menu = input('''
1.문제추가 2.타자게임 3.등수리스트 4.종료하기
메뉴선택 >>> ''')
    if menu == '1':
        fb1.quiz_input(word)
        fb1.load_save_data('word.json','w',word)
    elif menu == '2':
        fb1.typing_game(word,rank)
    elif menu == '3':
        fb1.rank_list(rank)
    elif menu == '4':
        print('프로그램을 종료합니다.')
        fb1.load_save_data('rank.json','w',rank)
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')