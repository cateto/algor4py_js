돌의내구도 = [1, 2, 1, 4]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4"
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3"
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1"
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1"
    }
]

"""def 징검다리를건너라(돌의내구도, 독):
    answer = [ 독[i]['이름'] for i in range(len(독)) ]
    return answer

print(징검다리를건너라(돌의내구도, 독))"""
#아래와 같은 코드

def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    return answer

print(징검다리를건너라(돌의내구도, 독))

def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도)-1:
            독의위치 +=int(i['점프력'])
            돌의내구도[독의위치-1] -=int(i['몸무게'])
            if 돌의내구도[독의위치-1] <0:
                answer[answer.index(i['이름'])] = 'fail'
                break;
    return [ i for i in answer if i !='fail']

print(징검다리를건너라(돌의내구도.copy(), 독.copy()))
#copy를 해주는 이유 : 객체복사 -> copy를 안하면 값이 함수에 의해 바뀜


ll = [1,2,3,4,5]

def change(l):
    l[0] = 1000

change(ll)
print(ll)
#list는 주소를 전달하기 때문에 안에서 수정하면 수정이 됨. 그래서 copy해야함.

xx = 100

def change(x):
    x += 1000
    return x

print(change(xx))
print(xx)
#여기서는 값이 안바뀜.. 값을 복사해서 전달하기 때문에 안에서 수정하더라도 수정이 되지 않음.

#remove O(N) 시간복잡도
#del O(1) 시간복잡도 더 적음~!

def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도)-1:
            독의위치 +=int(i['점프력'])
            돌의내구도[독의위치-1] -=int(i['몸무게'])
            if 돌의내구도[독의위치-1] <0:
                del answer[answer.index(i['이름'])]
                break;
    return answer

print(징검다리를건너라(돌의내구도.copy(), 독.copy()))

"""fail을 이름 대신 대입해서 걸러낼 수도 있고, 
이런식으로 del 함수를 활용해서 결과를 같게 할 수도 있다."""

"""다른 데이터를 다룰 경우에 예시""""

돌의내구도 = [5, 3, 4, 1, 3, 8, 3]
독 = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    },
]

def 징검다리를건너라(돌의내구도, 독):
    answer = [i['이름'] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도)-1:
            독의위치 +=int(i['점프력'])
            돌의내구도[독의위치-1] -=int(i['몸무게'])
            if 돌의내구도[독의위치-1] <0:
                del answer[answer.index(i['이름'])]
                break;
    return answer

print(징검다리를건너라(돌의내구도.copy(), 독.copy()))


""" json dump"""
import json

JSON독= json.dumps(독, ensure_ascii=False)
JSON독
JSON독[0]
JSON독[:10] #문자열을 슬라이싱

JSON독 = json.loads(JSON독)
JSON독[0]


