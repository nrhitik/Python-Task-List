'''Task 1.
Find the Missing Number in an Array
A list contains n distinct numbers taken from 0, 1, 2, ..., n, but one number is
missing.
Write a function to find the missing number.
def find_missing_number(arr: list) -> int:
 pass
Example:
arr = [3, 0, 1]
print(find_missing_number(arr)) Output: 2'''


def find_missing_number(arr: list):
    
    arr.sort()
    # print(arr)
    
    length = len(arr)
    missing_number = []
    
    for i in range (0, length):
        if i < (length-1):
            
            if i == 0 and arr[i] != 0:
                missing_number.append(0)
            
            if (arr[i]-arr[i+1]) != -1:    
                # print(f"ans: {arr[i]+1}")
                missing_number.append(arr[i]+1)
    
    if len(missing_number) == 0:
        return len(arr)
    else:
        return missing_number


missing_num_arr = [0,3,1,4,5,6,7,9,2,8]
ans = find_missing_number(missing_num_arr)
print(ans)
