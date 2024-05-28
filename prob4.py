def hanoi_top_calc(n, current, target, sub) -> None:
  if n == 1:
    print(current, target)

  else:
      hanoi_top_calc(n-1, current, sub, target)
      print(current, target)
      hanoi_top_calc(n-1, sub, target, current)

def hanoi_top(num:int) -> None:
  print(2**num-1)
  return(hanoi_top_calc(num,1,3,2))


# main
if __name__ == '__main__':
  while(True):
    try:
      num_plates = int(input('원판의 갯수를 입력하면, 원판이 옮겨질 순서를 자동으로 출력해드립니다!\n'))
      hanoi_top(num_plates)
      break

    except ValueError as e:
      print(f'{e}\n숫자를 입력해주세요')
      continue