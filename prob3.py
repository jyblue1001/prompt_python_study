class StringOutOfRange(Exception):
    def __init__(self) -> None:
        super().__init__('\nID의 길이가 1000자를 초과했습니다.\n아이디를 다시 입력해주세요.\n')


# 2단계에 쓰이는 함수
def character_check(id_str) -> str:
  ascii_values = []
  for character in id_str:
    if (
        (ord(character) > 96) and (ord(character) < 123)
    ) or (
        (ord(character) > 47) and (ord(character) < 58)
    ) or (
        ord(character) == 45
    ) or (
        ord(character) == 46
    ) or (
        ord(character) == 95
    ):
      ascii_values.append(character)
    else:
      ascii_values = ascii_values
  id_str = ''.join(ascii_values)
  return id_str


# 3단계에 쓰이는 함수
def replace_dots(id_str) -> str:
  while(id_str.count('..') > 0):
    id_str = id_str.replace("..",".")
  return id_str

# 5단계에 쓰이는 함수
def fill_empty_str(id_str) -> str:
  if len(id_str) == 0:
    id_str = 'a'
  else:
    id_str = id_str
  return id_str


# 6단계에 쓰이는 함수
def str_len15 (id_str) -> str:
  if len(id_str) >= 16:
    id_str = id_str[:15]
    id_str = id_str.rstrip('.')
  else:
    id_str = id_str
  return id_str

# 7단계에 쓰이는 함수
def str_extend (id_str) -> str:
  while(len(id_str) < 3):
    if len(id_str) <= 2:
      id_str = id_str + id_str[-1]
    else:
      id_str = id_str
  return id_str


def id_rule_check(id_under_check:str) -> str:
  
  # 1단계 (대문자 -> 소문자)
  id_under_check = id_under_check.lower()

  # 2단계 (소문자 숫자 - _ . 빼고 제거)
  id_under_check = character_check(id_under_check)

  # 3단계 (.. -> .)
  id_under_check = replace_dots(id_under_check)

  # 4단계 (처음 and 끝에 있는 마침표 제거)
  id_under_check = id_under_check.lstrip('.')
  id_under_check = id_under_check.rstrip('.')

  # 5단계 (빈 문자열 -> a로 채움)
  id_under_check = fill_empty_str(id_under_check)

  # 6단계 (16자 이상 제거, 끝의 마침표 제거)
  id_under_check = str_len15(id_under_check)

  # 7단계 (id 길이 2 이하, 끝 char 이어 붙이기)
  id_under_check = str_extend(id_under_check)

  return id_under_check


# main
if __name__ == '__main__':
  while(True):
    try:
      new_id = input('아이디를 입력하세요: ')
      if len(new_id) <= 1000:
        print('answer =',id_rule_check(new_id))
        break
      else:
        raise StringOutOfRange

    except StringOutOfRange as e:
      print(e)
      continue