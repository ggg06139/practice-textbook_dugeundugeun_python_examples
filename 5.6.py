x = int(input('정수를 입력하십시오 :'))

if (x%2 ==0) and (x%3 ==0):
    print('이는 2와 3으로 나누어 떨어집니다.')
elif (x%2 ==0):
    print('이는 2로 나누어 떨어지고 3으로는 나누어 떨어지지 않습니다.')
elif (x%3 ==0):
    print('이는 3로 나누어 떨어지고 2으로는 나누어 떨어지지 않습니다.')
else:
    print('이는 2와 3으로 나누어 떨어지지 않습니다.')