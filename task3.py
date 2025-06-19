'''Task 3.
Find the First Non-Repeating Character
Given a string, return the first non-repeating character. If all characters repeat, return
"None".
def first_unique_char(s: str) -> str:
 pass
Example:
s = "swiss"
print(first_unique_char(s)) Output: "w"'''

def first_unique_char(s: str) -> str:
    dict = {}

    for char in s:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    for key in dict:
        if dict[key] == 1:
            return key
            break
        

s = "swiss"
print(first_unique_char(s))