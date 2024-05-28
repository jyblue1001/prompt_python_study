
# 예외처리 클래스
class InvalidInputRangeError(Exception):
    """
    크기 범위를 벗어난 인자가 index인지 multiple인지에 따라 error message를 달리 출력하는 클래스
    """
    def __init__(
        self,
        num_commands,
        push_number            
        ) -> None:

        error_message = "범위 밖입니다.\n"

        if num_commands not in range(10000) and push_number == None :
           error_message = "num_commands(명령의 수)가" + error_message

        elif push_number == None and push_number not in range(100000) :
           error_message = "push_number(정수 X)가 " + error_message

        super().__init__(error_message)


class Stack:
    """
    덧셈, 뺄셈, 곱셈, 나눗셈 등 기초적인 계산을 하는 메소드 내장
    """
    stack = []
    _num_commands = 0

    def __init__(
            self,
            input_command,
            push_number            
            ) -> None:
        """
        Parameters
        ----------
        push_number : 스택에 넣을 정수, 이후 생성자 X로 사용
        """
        self._input_command = input_command
        self._push_number = push_number


    def command_type(self):
        """
        어느 계산 함수를 고를지 정하는 함수
        
        Returns
        -------
        selected_calc_type() : user_choice에 따른 메소드를 반환
        """
        
        Stack._num_commands -= 1

        # if-else 조건문을 대체하는 pythonic 스타일의 함수 지정 메소드
        command_cases = {
            # key : user_choice에 해당
            # value : Improved_Stack의 생성자 메소드
            'push'  : self.push,
            'pop'   : self.pop,
            'size'  : self.size,
            'empty' : self.empty,
            'top'   : self.top
        }

        # 선택한 계산법의 메소드를 반환함으로 호출
        return command_cases[self._input_command]()


    # 1. push 메소드
    def push(self) -> int :
        Stack.stack.append(self._push_number)
        return Stack.stack

    # 2. pop 메소드
    def pop(self) -> (int | float) :
        if len(Stack.stack) == 0 :
            print("-1")
        else:
            print(Stack.stack[-1])
            Stack.stack.pop()
        return Stack.stack

    # 3. size 메소드
    def size(self) -> (int | float) :
        print(len(Stack.stack))

    # 4. empty 메소드
    def empty(self) -> (int | float) :
        if len(Stack.stack) == 0 :
            print("1")
        else:
            print("0")

    # 5. top 메소드
    def top(self) -> (int | float) :
        if len(Stack.stack) == 0 :
            print("-1")
        else:
            print(Stack.stack[-1])        



def stack_operation(num_commands):
    while(num_commands):
        try:
            input_command, push_number = command_options_config()
            
            if input_command == 'push' and push_number not in range(100000):
                raise InvalidInputRangeError(None, push_number)
            
                
        except InvalidInputRangeError as e:
            print(e)
            continue

        else:
            s = Stack(input_command, push_number)
            s.command_type()
            num_commands -= 1


def command_options_config():
    user_input = input()
    input_command = user_input.split()[0]

    print("input_command is {}".format(input_command))

    command_options = {
        # key : user_choice에 해당
        # value : Improved_Stack의 생성자 메소드
        'push'  : None if len(user_input.split()) == 1 else int(user_input.split()[1]),
        'pop'   : None,
        'size'  : None,
        'empty' : None,
        'top'   : None
    }
    
    if input_command not in command_options.keys():raise KeyError
    
    push_number = command_options[input_command]
    print("push_number is {}\n".format(push_number))

    return (input_command, push_number)



def command_count_config():
    while(True):
        try:
            num_commands = int(input("명령의 수 : "))
            if num_commands not in range(10000):
                raise InvalidInputRangeError(num_commands, None)
            
        except InvalidInputRangeError as e:
            print(e)
            continue
        
        else:
            break

    return num_commands



def main():
    """
    계산기 작동 main 함수, 행동 단계는 아래처럼 나뉨. 

    1. 메뉴 출력
    2. 메뉴 선택
    3. 두 숫자 입력
    4. 계산 진행
    
    """
    num_commands = command_count_config()
    stack_operation(num_commands)


"""
스크립트를 직접 실행했을 때만 작동 되도록 함
    ex) python prob8.py
"""
if __name__ == '__main__':
    main()