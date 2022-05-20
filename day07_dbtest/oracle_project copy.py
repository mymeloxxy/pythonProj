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