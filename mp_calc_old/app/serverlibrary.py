

def merge(array, p, q, r, byfunc):
    nleft = q - p + 1                 #number of elements on the left
    nright = r+1 - (q+1)              #because the start index on the right size is q + 1
    left_array = array[p:q+1]         #left side array
    right_array = array[q+1:r+1]      #right side array
    left = 0                          #left arrow
    right = 0                         #right arrow
    dest = p                          #destination (merged) arrow
    while left < nleft and right < nright:
        if byfunc(left_array[left]) <= byfunc(right_array[right]):
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right += 1
        dest += 1
    while left < nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right < nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1

def mergesort_recursive(array, p, r, byfunc):
    if len(array[p:r+1]) > 1:                       #if first element is not the last element,
        q = (p+r)//2                                #divide the arrays into 2
        mergesort_recursive(array,p,q, byfunc)      #run mergesort_recursive again for the 2 separated arrays
        mergesort_recursive(array,q+1,r, byfunc)
        merge(array,p,q,r,byfunc)                   #merge the arrays

def mergesort(array, byfunc=None):
    return mergesort_recursive(array, 0, len(array) - 1, byfunc) #Uses mergesort_recursive from element 0 to last element in the array [0,1,2,3,4,5]

class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) == 0:
            return None
        else:
            temp = self.__items[-1]
            self.__items.pop()
            return temp

    def peek(self):
        if len(self.__items) == 0:
            return None
        else:
            return self.__items[-1]

    @property
    def is_empty(self):
        if len(self.__items) == 0:
            return True
        else:
            return False
    @property
    def size(self):
        return len(self.__items)

class EvaluateExpression:
    valid_char = '0123456789+-*/() '
    operator_char = '+-*/()'
    def __init__(self, string=""):
        self.expression = string

    @property
    def expression(self):
        return self.__expr

    @expression.setter
    def expression(self, new_expr):
        valid = True
        for char in new_expr:
            if char not in self.valid_char:
                valid = False
        if valid:
            self.__expr = new_expr
        else:
            self.__expr = ""

    def insert_space(self):
        for element in self.operator_char:
            if element in self.expression:
                self.expression = self.expression.replace(element, " " + element + " ")
        return self.expression

    def process_operator(self, operand_stack, operator_stack):
        operator = operator_stack.pop()
        if operator == "+":
            value1 = operand_stack.pop()
            value2 = operand_stack.pop()
            result = value2 + value1
            operand_stack.push(result)
        elif operator == "*":
            value1 = operand_stack.pop()
            value2 = operand_stack.pop()
            result = value2 * value1
            operand_stack.push(result)
        elif operator == "-":
            value1 = operand_stack.pop()
            value2 = operand_stack.pop()
            result = value2 - value1
            operand_stack.push(result)
        elif operator == "/":
            value1 = operand_stack.pop()
            value2 = operand_stack.pop()
            result = value2 // value1
            operand_stack.push(result)

    def evaluate(self):
        operand_stack = Stack()
        operator_stack = Stack()
        expression = self.insert_space()
        tokens = expression.split() #['(', '1', '+', '2', ')', '*', '3']
        for char in tokens:
            if char.isnumeric():
                operand_stack.push(int(char))
            if char == "+" or char == "-":
                while operator_stack.peek() != "(" and operator_stack.peek() != ")" and not operator_stack.is_empty:
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(char)
            if char == "*" or char == "/":
                while operator_stack.peek() == "*" or operator_stack.peek() == "/":
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.push(char)
            if char == "(":
                operator_stack.push(char)
            if char == ")":
                while operator_stack.peek() != "(":
                    self.process_operator(operand_stack, operator_stack)
                operator_stack.pop()
        while not operator_stack.is_empty:
            self.process_operator(operand_stack, operator_stack)
        return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





