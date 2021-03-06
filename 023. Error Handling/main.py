﻿# 파이썬은 Exception(예외) 말고 Error(오류)라는 표현을 쓴다
# 에러 핸들링을 위해선 try - except - finally 구문을 사용한다
# 가장 보편적인 오류인 IndexError를 잡아 보자
lst = [1, 2, 3]
try:
    print(lst[3])
except IndexError:
    print('Index Error!')
finally:
    print('Anyway')

# 여러 에러를 잡을 땐
try:
    print(lst[3])
except (IOError, IndexError):
    # 괄호로 묶고 콤마로 나열
    print('IOError or IndexError')
# except 구문을 여러개 두는 방법도 있다

# 파이썬에서는 try문에도 else문이 있다. full handling은 try-except-else-finally 형태다
try:
    print(lst[2])
except:
    print('IOError or IndexError')
else:
    print('Success')
# try문 내에서 오류가 발생하지 않을 경우 else문 내의 작업을 수행한다
