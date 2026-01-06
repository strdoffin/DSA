"""parent"""
class ArrayStack:
    """Array Stack"""
    def __init__(self):
        self.size = 0
        self.data = []
    def push(self, input_data):
        """push data"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".","",1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError , ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        """pop data"""
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        delete = self.data.pop()
        self.size -= 1
        return delete
    def is_empty(self):
        """is_empty"""
        if self.size == 0:
            return True
        else:
            return False
    def get_stack_top(self):
        """get top"""
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.data[-1]
    def get_size(self):
        """get size"""
        return self.size
    def print_stack(self):
        """print stack"""
        print(self.data)

text = input()
stack1 = ArrayStack()

def is_parentheses_matching(word):
    """find parent"""
    cnt = 0
    for i in word:
        if i in ('(','[','{'):
            stack1.push(i)
        elif i in (')',']','}'):
            check = stack1.pop()
            if check == None:
                cnt += 1
            else:
                match (i):
                    case (')'):
                        if check != '(':
                            return [False,cnt]
                    case (']'):
                        if check != '[':
                            return [False,cnt]
                    case ('}'):
                        if check != '{':
                            return [False,cnt]
    return [stack1.is_empty() , cnt]
FINAL = is_parentheses_matching(text)
if FINAL[1] > 0 or FINAL[0] == False:
    # print("Parentheses in",text,"are unmatched")
    print(False)
else:
    # print("Parentheses in",text,"are matched")
    print(True)

