# from errno import ENETRESET
# import re
# from matplotlib.pyplot import table

# from regex import D, W

import re


a = 'hello, world!'
# print(re.match('world!',a))
# # match는 첫글자를 비교해서 못찾음
# print(re.search('world!',a))
# # search는 찾을 수 있음
# print(re.search('^world!',a))
# # ^world!-world!로 시작하는 으로 찾으면 못찾음 중간에 있어서
# print(re.search('world!$',a))
# # world!$-world!로 끝나는 으로 찾으면


# str1 = '123 hello 678 HELLO'
# print(re.match('[0-9]',str1))
# # 한 글자에 대한 것
# print(re.match('[0-9]+',str1))
# # 하나 이상
# print(re.match('[0-9]*',str1))
# # 0개이상
# print(re.search('[0-9]*',str1))
# # 중간에서 부터 찾지만 맨 처음 맞딱뜨리는거 찾음

# print(re.match('a*b','b')) 
# # 도 되고
# print(re.match('a*b','ab'))
# # 도 되고 0개이상(없을 수도 있다)
# print(re.match('a*b','aaaaaab'))
# # 도 가능

# print(re.match('a+b','aaaaaab'))
# # a가 하나이상 나와야 되니 여러개 있어도 됨
# print(re.match('a+b','b'))
# # a가 하나이상 나와야 되니 안됨
# print(re.match('abc?d','abd'))
# # c가 없어도 되는데 있으면 1개 있어야 됨

# # 문자열|문자열|문자열 = 문자열or문자열or문자열

# # 문자{개수} (문자열){개수}
# # h{3} = h가 3개, (hello){3} = hello가 3번

# # [0-9]{개수} = 횟수
# # 숫자는 []가 들어감

# # (문자){시작개수,끝개수}

# # print(re.search('[0-9]{2,3}-[0-9]{4}-[0-9]{4}','02-1111-1111'))

# print(re.search('^[0-9]{2,3}-[0-9]{4}-[0-9]{4}$','002-1111-1111 tel'))

# a-z = 소문자 처음~끝
# A-Z = 대문자 처음~끝
# []안에 소문자,대문자,숫자올 수 있음/+는 한자리 이상 와야됨
# 가-힣 = 일반적인 한글 다 들어감

# [^범위] = not
# [^A-Z]+ = 알파벳 대문자는 제외하고 한 글자 이상

# ^[범위] = or not
# ^[A-Z] = 대문자로 시작하는데 없을 수도 있다

# \d = [0-9],모든 숫자
# \D = [^0-9], 숫자빼고
# \w = [a-zA-Z0-9_],영어대소문자
# \W

# \s = 공백을 제외한 나머지,공백을 제외하고 \t,\n,\r,\f,\v만 포함
# \t = tab
# \n = enter
# \r = 캐리지 리턴
# \v = 수직탭

# p는 변수인데 아무거나 쓰면 됨 {4,} = 4개 이상
# p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
# print(p.search('ss7up@gmail.com'))
# print(p.search('shimseonjo@gmail.com'))

p = re.compile('^[a-z][a-z0-9_]{4,}@[a-z]{3,}[.][a-z]{2,}$')
email = ''
while not p.search(email):
    email = input('email >>> ')