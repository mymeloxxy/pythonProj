#  과일가게 재고관리 프로그램
# 기능은 알아서
# -재고입력
# -입력된 것 판매
# -재고상황 리스트
# -삭제
# 1.  상품명입력
# 2. 판매_재고상황 리스트
# 3. 단가
# 4. 입고일자


import re
fruitlist=[] 
fruitlist=[{'product': '사과', 'number': '20개', 'price': '1000원', 'date': '20220510', 'sugqr':'4'}, {'product': '바나나', 'number': '15개', 'price': '500원', 'date': '20220508', 'sugqr':'2'}, {'product': '토마토', 'number': '25개', 'price': '1500원', 'date': '20220506', 'sugqr':'3'}]
product = "temp"
dic = {}

while True:
    choice = input('''
---------------------------------------------
1. 상품명 2. 상품수 3. 단가 4. 입고일자 5. 삭제
---------------------------------------------
선택 >>> ''')
    if choice == '1':
        while product != "":
            name = input("팔린 물품을 입력하시오 (종료: Enter):")
            if name == "":
                break
            count = int(input("팔린 수량을 입력하세요:"))
            print(" ") 
        #     if name in dic:
        #         dic[name] += count
        #     else:
        #         dic[name] = count

        #         print(" ")        
        #         print("*"*40)
        #         print("총 판매 품목 수 :",len(dic.keys()))
        #         print("총 판매 수량 :",sum(dic.values()))
        #         print("*"*40,end="\n판매 순위\n")

        # temp = {}
        # List = []

        # for k,v in dic.items():
        #     temp[v] = k
        #     List.append(v)
            
        # List.sort()
        # List.reverse()

        # for i in range(len(List)):
        #     print("%d위:\t%s %d개"%(i+1,temp[List[i]],dic[temp[List[i]]]))
            
    elif choice == '2':
        print(fruitlist)
        while True:
            choice1 = input('판매한 과일을 입력하세요 : ')
            idx = -1
            for i in range(len(fruitlist)):
                if fruitlist[i]['fruit'] == choice1:
                    idx = i
                    break
            if idx == -1:
                print('등록되어있지 않은 과일입니다.')
                break
            choice2 = input('판매한 수량을 입력하세요 : ').upper()
            sale = fruitlist[idx]['stock']-int(choice2)
            print(f'{choice1}을 {choice2}개를 판매하여 {sale}개가 남았습니다.')

            if choice2 == 'q':
                break
            fruitlist[idx]['stock'] = sale
            print(fruitlist)

    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    

