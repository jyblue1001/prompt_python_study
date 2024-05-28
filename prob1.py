while 1:

  print('------------------------------------------')
  print('\"구구단을 외자, 구구단을 외자\" 프로그램을 실행합니다.')
  print('1. 홀수 구구단')
  print('2. 짝수 구구단')
  print('3. 종료')
  print('------------------------------------------')

  num = int(input('숫자를 입력하세요: '))
  print()

  if num == 1:
    for i in range(4):
      print('{}단'.format((i*2+3)))
      for j in range(9):
        print("{0} * {1} = {2}".format((i*2+3),(j+1),((i*2+3)*(j+1))))
      print()

  elif num == 2:
    for i in range(4):
      print('{}단'.format((i*2+2)))
      for j in range(9):
        print("{0} * {1} = {2}".format((i*2+2),(j+1),((i*2+2)*(j+1))))
      print()

  elif num == 3:
    print('프로그램을 종료합니다.')
    break

  else:
    print("잘못 입력하셨습니다. 1~3 번 숫자를 입력하세요.")