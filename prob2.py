book_info = {
    "HarryPotter1" : [[1997], [6], [26]],
    "TheLordOfTheRings" : [[1954], [7], [29]],
    "engineering_mathematics1" : [[2018], [2], [28]]
}

while 1:
  print('원하시는 정보를 선택해주세요.')
  title = input('> ')

  if title in book_info:




    while 1:
      print("""
------------------------------------------
원하시는 정보를 선택해주세요.
1. 년
2. 월
3. 일
4. 종료
------------------------------------------
      """)
      num = int(input())
      print()

      if num == 1:
        print('{}년 입니다'.format(book_info[title][num-1][0]))
      elif num == 2:
        print(book_info[title][num-1][0],'월 입니다')
      elif num == 3:
        print(book_info[title][num-1][0],'일 입니다')
      elif num == 4:
        print('프로그램이 종료되었습니다.')
        break
      print()
    break

  else:
    print('제목을 다시 입력해주세요\n')

