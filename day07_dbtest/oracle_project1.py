# 1. emp테이블에 job을 입력받아 해당 job인 사원을 출력하세요
# 2. 사원의 이름의 일부를 입력받아서 검색해서 출력(o가 들어가는 사람 등)
# 1번,2번 선택하는 프로그램

import cx_Oracle
while True:
    choice = input('1.직업선택 2. 사원의 이름출력>>>' )
    if choice == '1':
        conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
        cursor = conn.cursor()
        cursor.execute("select * from emp")

        print(cursor)

        for item in cursor:
            print(item[1],item[2])

        conn.close()
    elif choice == '2':
        conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
        cursor = conn.cursor()
        cursor.execute("select * from emp where ename like '%E%'")

        print(cursor)

        for item in cursor:
            print(item[1])

        conn.close()



