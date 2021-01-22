
class Stack(list):
    # def __init__(self=list):
    #     pass

    def is_empty(self):
        return len(self) == 0

    def push(self, element):
        self.append(element)

    def pop(self):
        if self.is_empty():
            return 'List is already empty'
        else:
            self.pop()

    def peek(self):
        return self[-1]

    def size(self):
        return len(self)


if __name__ == '__main__':
    def are_brackets_balanced(string,  brackets="〈〉()[]{}"):
        opening, closing = brackets[::2], brackets[1::2]
        my_stack = Stack()
        input_string = string
        for bracket in input_string:
            if bracket in opening:
                my_stack.push(bracket)
            elif bracket in closing and my_stack.size() > 0:
                if (my_stack[-1] + bracket == '()')\
                        or (my_stack[-1] + bracket == '{}') \
                        or (my_stack[-1] + bracket == '[]'):
                    my_stack.pop()
                else:
                    return 'Not Balanced'
            else:
                return 'Not Balanced'
        if my_stack.is_empty():
            return 'Balanced'

    print(are_brackets_balanced('(((([{}]))))'))
    print(are_brackets_balanced('[([])((([[[]]])))]{()}'))
    print(are_brackets_balanced('{{[()]}}'))
    print(are_brackets_balanced('}{}'))
    print(are_brackets_balanced('{{[(])]}}'))
    print(are_brackets_balanced('[[{())}]'))
