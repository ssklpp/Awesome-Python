# 문자열 변수 선언 또한 그냥 대입하면 된다
s = 'hello'
# 작은따옴표로 묶을 수도 있고, 큰 따옴표로 묶을 수도 있다
s = "hello"
# 문자열을 만드는 방법은 총 4가지가 있다
s = '''hello'''
s = """hello"""

# 1. 문자열 안에 작은따옴표나 큰따옴표를 포함시키기 위해서
s = "Mingyu's pizza"
# 백슬래시 써도 된다
s = 'Mingyu\'s pizza'

# 2. 여러 줄에 문자열을 표현하기 위해서
s = '''Hello
        HelloHello'''
# 이스케이프 시퀀스를 쓰는 방법도 있지만 이게 더 편하다

# 문자열 연산 : 단순 concat
s = 'Hello' + ' World'
# + 기호로 문자열을 연결하는 건 평범한 일인데, 문자열과 정수간의 곱셈이 가능하다
s = 'Hello' * 2
# 'HelloHello'

# 파이썬에서 문자열은 인덱싱이 가능하다
print(s[0])
# 음수로 인덱싱하는 것도 된다
print(s[-1])
# 뒤쪽부터 접근하는데, -1이 맨 뒤쪽을 나타낸다
# zero-based numbering 개념에 따라 0은 양수 인덱싱에 포함된다

# 파이썬은 시퀀스를 잘라서 최소한의 노력으로 아이템의 부분집합을 얻어올 수 있다
print(s[0:3])
# 슬라이싱이라고 부른다. n:m으로 슬라이싱하면 n부터 m-1의 요소까지 잘린다
# __getitem__과 __setitem__이라는 특별한 메소드를 구현하는 파이썬의 다른 클래스에도 슬라이싱을 적용할 수 있다

print(s[-4:-1])
# 당연히 음수 슬라이싱도 되고

print(s[:-2])
# 처음부터 슬라이스할 때는 보기 편하게 인덱스 0을 생략

print(s[1:])
# 끝까지 슬라이스할 때도 마지막 인덱스는 생략하는 것이 좋음

print(s[:20])
# 슬라이싱은 start와 end 인덱스가 경계를 벗어나도 적절하게 처리한다. 덕분에 입력 시퀀스에 대응해 처리할 최대 길이를 설정할 수 있게 된다

print(s[::2])
# 슬라이싱 할 때 두번째 콜론 뒤에 오는 숫자는 stride라고 한다
# 위의 말의 뜻은 '0번 인덱스부터 마지막 인덱스까지 매 두 번째 원소를 모아 배열을 만든다'
