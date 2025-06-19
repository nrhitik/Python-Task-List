'''Valid Parentheses Checker
Write a function to check whether a given string containing only (), {}, [] is
balanced.
def is_valid(s: str) -> bool:
 pass
Example:
s = "{[()]}"
print(is_valid(s)) Output: True
s = "{[(])}"
print(is_valid(s)) Output: False'''



list1 = [1,2,3,4,5]


def is_empty(stack):
    pass

def is_valid(s: str) -> bool:
    stack = []
    for char in s:
        if char == "[" or char == "{" or char == "(":
            stack.append(char)
        elif (stack[-1] == "[" and char == "]") or (stack[-1] == "{" and char == "}") or (stack[-1] == "(" and char == ")"):
            stack.pop()
        else:
            return False
            break
    
    if len(stack) == 0 :
        return True
    
s = "{[({}{)}][]}"
print(is_valid(s))