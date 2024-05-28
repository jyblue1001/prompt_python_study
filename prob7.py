
# 최대 공약수 계산을 위한 math 모듈 호출
import math


class Calculator:
    """ 계산기 부모 클래스
    
    덧셈, 뺄셈, 곱셈, 나눗셈 등 기초적인 계산을 하는 메소드 내장하고 있음

    """

    def __init__(
            self,
            first_number : (int | float),
            second_number : (int | float)
            ) -> None:
        """    
        
        Parameters
        ----------
        first_number : 사용자의 입력 중 첫 번째 숫자, 이후 생성자 num1로 사용
        second_number : 사용자의 입력 중 두 번째 숫자, 이후 생성자 num2로 사용

        """
        self.num1 = first_number
        self.num2 = second_number

    # (int | float)은 파라미터 형식 표시법이고, 메소드 파라미터로 int 혹은 float가 주어질 것을 기대함.

    # 1. 덧셈 메소드
    def addition(self) -> (int | float) :
        return self.num1 + self.num2

    # 2. 뺄셈 메소드
    def subtraction(self) -> (int | float) :
        return self.num1 - self.num2
    
    # 3. 곱셈 메소드
    def multiplication(self) -> (int | float) :
        return self.num1 * self.num2

    # 4. 나눗셈 메소드
    def division(self) -> (int | float) :
        return self.num1 / self.num2
    

class Improved_Calculator(Calculator):
    """Calculator 클래스를 상속한, 개선된 계산기 클래스
    
    Calculator 클래스에는 없는 추가적인 계산(제곱, 최대 공약수)을 하는 새로운 메소드 또한 추가됨.

    """
    def __init__(
            self,
            num1 : (int | float),
            num2 : (int | float),
            user_choice : int
            ) -> None:
        """
        
        Parameters
        ----------
        user_choice : 사용자가 선택한 메뉴, 이후 생성자 choice로 사용

        """
        super().__init__(num1, num2)
        self.choice = user_choice


    def calc_type(self):
        """calculation type selction 함수
        
        사용자 입력을 통해 어느 계산 함수를 호출할지 지정하는 메소드
        dictionary를 응용하여, if-else 조건문을 대체하는 pythonic 스타일 추구
        
        Returns
        -------
        selected_calc_type() : user_choice에 따른 메소드를 반환

        """
        calc_cases = {
            # key : user_choice에 해당
            # value : Improved_Calculator의 생성자 메소드
            1 : self.addition,
            2 : self.subtraction,
            3 : self.multiplication,
            4 : self.division,
            5 : self.power,
            6 : self.greatest_common_divisor,
        }

        # 선택한 계산법의 메소드를 반환함으로 호출
        return calc_cases.get(self.choice)()
    
    # 5. 제곱 메소드
    def power(self) -> (int | float) :
        return self.num1 ** self.num2 

    # 6. 최대 공약수 메소드
    def greatest_common_divisor(self) -> (int | float) :

        # 입력 중 하나가 0일 때, math.gcd()가 제대로 작동하지 않는 것을 해결
        if self.num1 or self.num2 == 0:
            return 0
        
        else:
            # 최대 공약수는 math 라이브러리로 간결하게 구현
            return math.gcd(self.num1, self.num2)


def print_menu() -> None:
    """
    메뉴 출력 함수    
    """
    print("\n")
    print('아래에 사용을 원하시는 사칙연산을 선택해주세요!')
    print('1. 더하기')
    print('2. 빼기')
    print('3. 곱하기')
    print('4. 나누기')
    print('5. 제곱')
    print('6. 최대 공약수')
    print('7. 종료')



def main():
    """
    계산기 작동 main 함수, 행동 단계는 아래처럼 나뉨. 

    1. 메뉴 출력
    2. 메뉴 선택
    3. 두 숫자 입력
    4. 계산 진행

    
    
    """
    while(True):
        try:
            # 1. 메뉴 출력
            print_menu()

            # 2. 메뉴 선택
            user_choice = int(input("\n"))
                
                # 2-a. 프로그램 종료 선택지(7을 입력 받을시)
            if user_choice == 7: print("\n계산기 프로그램을 종료합니다\n"); break

            # 3. 두 숫자 입력
            # 입력이 부족할 때의 예외 처리는, built-in exception "ValueError" 그대로 사용
            first_number, second_number = map(int,input("\n두 숫자를 입력해주세요. " ).split())

                # 3-a. 0인 분모에 대한 예외 처리, built-in exception "ZeroDivisionError" 그대로 사용
            if user_choice == 4 and second_number == 0:
                raise ZeroDivisionError
                   
        except ZeroDivisionError as e:
            print(f'{e}\n0으로 나눌 수 없습니다.\nNone')
            continue

        else:
            # 4. 계산 진행
            # Improved_Calculator의 객체인 "c" 인스턴스 선언 및 해당 인스턴스 변수 생성
            c = Improved_Calculator(first_number, second_number, user_choice)
            
            # "c" 인스턴스의 calc_type() 메소드 사용하여 결고 출력 
            calculation = c.calc_type()
            print(c.calc_type(),"\n")


"""
스크립트를 직접 실행했을 때만 작동 되도록 함
    ex) python prob7.py
"""
if __name__ == '__main__':
    main()