
# random 모듈 호출
import random

# 단어장
words = ["python", "programming", "line", "hangman"]

# 시도 횟수 초기값
attempts = 5


class InvalidInputLengthError(Exception):
    """
    길이가 하나 이상인 문자를 입력으로 받았을 시 경고 메시지 출력하는 클래스
    """
    def __init__(self) -> None:
        super().__init__('하나의 문자만 입력하세요. 시도 횟수는 유지됩니다.\n')


# 단어장에서 무작위로 단어를 가져와서 정답에 저장, 단어 길이만큼의 정답란 "_" 만드는 함수
def get_answer_guess():
    answer = list(random.choice(words))

    # 단어 길이만큼의 정답란 "_" 만들기
    guess = []
    for i in range (len(answer)):
      guess.append("_ ")
    
    return (answer,guess)


# "_ "로 이루어진 정답란 guess 갱신하는 함수
def guess_correction(guess,user_guess):
    print("Correct\n")
    
    """
    for (answer_idx, answer_letter) in enumerate(answer):
        if answer_letter == user_guess:
            guess_idx = answer_idx
    """
    # 아래 코드는 위처럼 해석 가능
    guess_idx = [answer_idx for (answer_idx, answer_letter) in enumerate(answer) if answer_letter == user_guess]
    
    # 맞춘 글자들에 대해 정답란 갱신    
    for idx in guess_idx:
        guess[idx] = user_guess

    # 갱신된 정답란 반환
    return (guess)


# 시도 횟수 갱신하는 함수
def guess_attempts_deduct():
    
    # 전역변수로써 시도 횟수 불러옴, 따라서 이 함수 내에서 변형된 attempts는 전역적으로 변형됨.
    global attempts
    print("Wrong 남은 시도 횟수: {}\n".format(attempts))

    # 시도 횟수 전부 소진 시, 정답을 알려주고 프로그램 종료
    if attempts == 0:
        print("word = " + "".join(answer))
        exit()
    
    # 시도 횟수가 0이 되기 전까지 시도 횟수 차감
    else:
        attempts -= 1


# 사용자 입력 후 바뀐 정답란 출력하는 함수
def show_current_guess(guess,answer)-> None:
  
  # 정답란과 단어가 동일하면 success, 정답 출력
  if guess == answer:
    print("success\n" + "word = " + "".join(guess))
  # 사용자 입력 후 바뀐 정답란 출력
  else:
    print(" ".join(guess))


# main
if __name__ == '__main__':
    
    # 단어장에서 무작위로 단어를 가져와서 정답에 저장, 단어 길이만큼의 정답란 "_" 만드는 함수 호출
    answer, guess = get_answer_guess()

    # 사용자가 맞춘 것과 정답이 같아질 때까지 반복문 계속
    while(guess != answer):
        try:
            # 입력 받기
            user_guess = input("input letter > ")

            # 입력이 하나의 글자일 때 검사 진행
            if len(user_guess) == 1:
                  
                  # 입력이 정답 안에 있으면, 메세지를 출력하고, 해당 index의 "_"를 정답의 글자로 바꿈
                  if user_guess in answer:
                      guess = guess_correction(guess,user_guess)
                  
                  # 입력이 정답 안에 없으면, 메세지를 출력하고, 시도 횟수 차감
                  else:
                      guess_attempts_deduct()
                  
                  # 현재까지의 사용자가 맞춘 것 출력
                  show_current_guess(guess,answer)

            # 입력이 하나의 글자가 아닐 때 예외처리 
            else:
              raise InvalidInputLengthError

        except InvalidInputLengthError as e:
            print(e)
            continue