
# 예외처리 클래스
class InvalidIntegerInputError(Exception):
    """
    크기 범위를 벗어난 인자가 index인지 multiple인지에 따라 error message를 달리 출력하는 클래스
    """
    def __init__(self, index, multiple) -> None:
        error_message = "범위 밖입니다.\n"

        if ((index > 10 or index < 0) and (multiple > 10 or multiple < 0)):
           error_message = "index(가로세로 크기)와 multiple(늘릴 크기)가 " + error_message

        elif (multiple > 10 or multiple < 0):
           error_message = "multiple(늘릴 크기)가 " + error_message

        else:
           error_message = "index(가로세로 크기)가 " + error_message

        super().__init__(error_message)


# 배수 크기만큼 행 출력을 반복하고, 각 행에는 배수 크기만큼 내부 인자 반복
def upsampling(multiple, row):
    
    # 세로 방향으로 반복
    for j in range(multiple):
      # 가로 방향으로 반복
      for k in range(multiple):
        print(multiple * (row[k] + " "), end="")
      print()


# main
if __name__ == '__main__':
  while(True):
    try:
      # 입력 받기 (가로세로 길이: index, 늘릴 배수: multiple)
      index, multiple = map(int, input().split())

      # 입력된 길이와 배수가 크기 조건에 맞는지 확인
      if ((index < 11 and index > 0) and (multiple < 11 and multiple > 0)):
          matrix = []
          
          # N개의 픽셀 정보를 한 줄씩 입력하여 list로 저장, 그 list를 "matrix" list에 추가
          for i in range(index):
              row = input().split()
              matrix.append(row)
          
          # 행 하나당 upsampling 함수 호출
          for i in range(index):
            upsampling(multiple, matrix[i])

          # 프로그램 종료
          break
      
      # 조건에 맞지 않으면 error 발생시키기, 길이와 배수 인자 모두를 예외처리 클래스에 전달
      else:
          raise InvalidIntegerInputError(index, multiple)

    except InvalidIntegerInputError as e:
      print(e)
      continue