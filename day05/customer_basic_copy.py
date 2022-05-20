# 콘솔형 고객 정보 관리 시스템 구축

# list[]함수는 순서가 있어서 index사용함[0]->첫번째, [1]->2번째 1~5번호주는 슬라이싱이 가능하고 추출이 가능하다,중복가능
# 튜플()은 리스트함수랑 기능 같지만 다른 점 하나->중간수정이 안됨 통채로 제거해야됨
# 딕셔너리{k;v}{k,v},,,는 순서x,인덱스x,슬라이싱x,데이터로 구분,똑같은 데이터들어가면 오류발생,{k;v}key값은 중복되면 안되고,value값은 중복되도 됨
        #  [0] [1],,,
# 셋{v}value값만 들어감

# 1. 기능  
# 고객 정보 입력(I), 현재/이전/다음 고객 정보 조회(C/P/N), key값으로 데이터 가져와서 고객 정보 수정(U), key값으로 데이터 가져와서 고객 정보 삭제(D), 고객 정보 종료(Q)

# - 괄호 안 영문자를 입력하면 각 기능이 구현되게 만든다
# - 종료(Q)를 입력하기 전까지 기능 선택 메시지가 계속 뜨도록 만든다
# - 각 기능은 함수로 관리한다
# - 입력된 각 정보는 인덱스 값에 따라 페이지를 가진다 [a,s,d,f,g]
# [-1]=값x,[0]=a,[1]=s/값을 [1]까지 입력했으면 current=page1
#   -> 첫 정보 입력 시 인덱스는 0이므로, 입력 전 기본 page 값은 -1로 설정한다

# 2. 입력(I)
# - dictionary로 각 키의 값을 받고 빈 리스트에 채워나간다
# - 성별(gender) : M, m, F, f로만 입력 가능
#   -> 소문자로 입력하는 경우 대문자로 자동 변환
#   -> gender 값이 M 또는 F가 아닐 경우 다시 입력
# - 이메일(email) : 입력값 내 '@'가 반드시 있어야 함/이메일을 key값으로 사용
#   -> 정규표현식 사용
#   -> re를 import 하여 이메일 입력값 내 '@' 존재 여부 파악
#   -> 없는 경우 '@'를 포함하라는 문구와 함께 재입력 하도록 함
#   -> 중복된 이메일 입력 방지/구분하는 key값으로 사용
# - 출생년도(birthyear) : 4자리로 입력 해야
#   -> len 값으로 입력 값의 길이를 구함
#   -> 4자리가 아닐 경우 재입력 하도록 함
# - 출생년도까지 입력이 완료되었을 경우
#   -> 키 값 입력이 완료된 customer 딕셔너리를 custlist 리스트에 추가(append)한다
#   -> 고객 정보가 새로 입력 되었으므로 page 값에 1을 더한다

# 3. 조회(C, P, N)
# - 인덱스는 0부터 시작하나 페이지는 통상 1부터 시작하므로 페이지 출력시 page+1 값을 반환한다
# - 이전 페이지 조회(P)의 경우, 첫 번 째 페이지인 상태에서 이전 페이지로 이동이 불가하므로 현재 페이지인 첫 번 째 페이지를 반환
# - 다음 페이지 조회(N)의 경우, 마지막 페이지인 상태에서 다음 페이지로 이동이 불가하므로 현재 페이지인 마지막 페이지를 반환

# 4. 삭제(D)
# - unique한 키를 기준으로 삭제정보를 선택한다 -> 여기서는 이메일로 가정
# - 삭제 성공 여부 변수(delok)
#   -> 입력한 이메일이 등록된 정보 내에 있을 경우 삭제
#   -> 삭제가 성공하면 delok=1 (default 값 0)
#   -> 등록된 정보 내에 없는 이메일일 경우(delok=0) 등록되지 않았다고 출력

# 5. 수정(U)
# - unique한 키를 기준으로 수정 정보를 선택한다 -> 여기서는 이메일로 가정
# - 입력한 이메일과 일치하는 고객 정보의 인덱스를 idx에 입력
#   -> idx의 default 값은 -1
#   -> 일치 여부 확인 후에도 idx가 -1일 경우 등록되지 않았다고 출력
# - 이메일 외에 이름, 성별, 출생년도 중 수정할 정보 선택
# - 수정할 정보 선택 후 수정할 내용 입력
# - 수정하고 픈 변수가 없는 경우 exit 입력 시 수정 창 종료

# 6. 종료(Q)
# - 맨 처음 while 반복문을 나간다 -> break


# import re
# custlist=[]
# page=-1
# custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong123@gmail.com', 'birthyear': '2000'},
#           {'name': '박철수', 'gender': 'M', 'email': 'park01@gmail.com', 'birthyear': '2002'},
#           {'name': '김나리', 'gender': 'F', 'email': 'kim123@gmail.com', 'birthyear': '1999'}] 
# 미리 세건으로 맞춰놔서 page = 2
# page = 2 
# while True:
# input~밑의 내용 = 키보드로 입력받은 값을 str로 바꿔줌
# str.upper = 대문자로 바꿔줌/str.upper의 내용을 choice에 input
#     choice=input('''
# 다음 중에서 하실 일을 골라주세요 :
# I - 입력 C - 현재  P - 이전  N - 다음  U - 수정  D - 삭제  Q - 종료
# >>>''').upper()  

#     if choice=="I":  
#         customer={'name': '', 'gender': '', 'email': '', 'birthyear': ''}
#         customer['name']=input('이름 >>> ')
#         # 이름을 입력받아 바로 넣음
#         while True:
#         # 제대로 들어올 때 까지 반복
#             customer['gender']=input('성별(M,F) >>> ').upper()
#             if customer['gender'] in ('M','F'):
#             # if로 젠더안에 남자인지 여자인지
#                 break
#         # 이메일
#         while True:
#             while True:
#                 # 이메일값 받고 시작
#                 customer['email']=input('email >>> ')
#                 if customer['email'].find('@') != -1:
#                 # 값이 있으면 0<=/값 없으면 -1
#                     break
#                 else:
#                     print('이메일을 정확하게 입력하세요')
#             check = 0
#             # 중복여부 확인
#             # i는 custlist에서 가져온 데이터 ,custmoer는 금방 입력한 데이터/check값이 0이면 입력처리하면 됨,그러나 1이나2,3,,,이면 중복되는 이메일 있다고 프린트
#             for i in custlist:
#                 if i['email'] == customer['email']:
#                     check = 1
#                     break
#             if check == 0:
#                 break
#             print('중복되는 이메일이 있습니다.')
#         while True:
#             customer['birthyear'] = input('생년월일(4자리) >>> ')
#             if len(customer['birthyear']) == 4 and customer['birthyear'].isdecimal():
#                 # isdecimal()-숫자인지
#                 break

#         custlist.append(customer)
#         # 전체 리스트에 추가
#         page = len(custlist)-1
#         # 무조건 마지막 페이지로 바꿔놓기로 해놧음
#         print(custlist)
            
        
#     elif choice=="C": 
#         if page < 0:
#             print('입력된 정보가 없습니다.')
#         else:
#             print(f'현재 페이지는 {page+1}페이지 입니다.')
#             print(custlist[page])
#     elif choice == 'P':
#         if page <= 0:
#             print('첫번째 페이지 입니다.')
#         else:
#             page -= 1
#             print(custlist[page])
#         print(f'현재 페이지는 {page+1}페이지 입니다.')
#     elif choice == 'N':
#         if page >= len(custlist)-1:
#             print('마지막 페이지 입니다.')
#         else:
#             page += 1
#             print(custlist[page])
#         print(f'현재 페이지는 {page+1}페이지 입니다.')
#     elif choice=='D':
#         print(custlist)
#         choice1 = input('삭제하려는 이메일 주소를 입력하세요 >>> ')
#         delok = 0
#         # 지워졌는지 안지워졌는지 상태값/처음 = 0/만약 1이라면 지워졌다는 뜻
#         for i in range(len(custlist)):
#             if custlist[i]['email'] == choice1:
#             # 지우고자한 걸 찾음
#                 print(f'{custlist[i]["name"] }님의 정보가 삭제되었습니다.')
#                 del custlist[i]
#                 delok = 1
#                 break
#         if delok == 0:
#         # 똑같은 이메일을 못찾았다
#             print('등록되지 않은 고객 정보입니다.')
#         print(custlist)
#     elif choice=="U": 
#         while True:
#             choice1 = input('수정하려는 이메일 주소를 입력하세요 >>> ')
#             idx = -1
#             # 몇번째를 수정할것인가, 초기값은 -1임
#             for i in range(len(custlist)):
#                 if custlist[i]['email']==choice1:
#                     idx = i
#                     # 찾으면 idx에 위치값을 저장
#                     break
#             if idx == -1:
#                 print('등록되지 않는 정보입니다.')
#                 break

#             choice2 = input('''
# --------------------------------------------
#  다음 중 수정할 항목을 선택하세요(종료:exit)
#   - name,gender,birthyear 중 입력
# --------------------------------------------  
# 항목 >>> ''')
#             if choice2 in ('name','gender','birthyear'):
#                 custlist[idx][choice2] = input(f'수정할 {choice2}를 입력하세요 >>>')
#                 print(custlist[idx])
#                 break
#             elif choice2 == 'exit':
#                 break
#             else:
#                 print('존재하지 않는 정보입니다.')
#                 break

#     elif choice=="Q":
#         print('프로그램을 종료합니다.')
#         break