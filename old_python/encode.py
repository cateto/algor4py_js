text = [
        '   + -- + - + -   ',
        '   + --- + - +   ',
        '   + -- + - + -   ',
        '   + - + - + - +   ',
        ]

#ord() : 문자 -> 숫자 변환 함수
#chr() : 숫자 -> 문자 변환 함수

'''for i in text:
    print(chr(int(i.strip()
    .replace(' ','')
    .replace('+','1')
    .replace('-','0'), 2)))
'''

'''
l = []
for i in text:
    l.append(chr(int(i.strip()
    .replace(' ','')
    .replace('+','1')
    .replace('-','0'), 2)))    

print(''.join(l))
'''

print(''.join([chr(int(i.strip()
    .replace(' ','')
    .replace('+','1')
    .replace('-','0'), 2)) for i in text]))

# list comprehensions :

[i for i in range(10) if i % 2 == 0] 
# 짝수 출력

print([f'{i} X {j} = {i*j}' for i in range(2, 10) for j in range(1, 10)])
# 구구단 출력
    
# replace :  

i = '011011011'.replace('0', '!').replace('!','+').replace('+','~')
print(i)

k = '111'.zfill(10)
print(k)


# example

s = [i.strip()
    .replace(' ','')
    .replace('+','1')
    .replace('-','0') for i in text]
    
print(''.join(list(map(lambda x : chr(int(x, 2)), s))))
#lambda 인자 : 표현식 : 함수를 받아서 한 줄로 만들어 줌.
#map(함수, 리스트) : 함수를 받아서 적용시키고 새로운 리스트에 담음

def f(x) :
    return chr(int(x,2))

print(''.join(list(map(f,s))))