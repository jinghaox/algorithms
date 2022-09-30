from operator import le


def letter_combinations(digits):
    res = []
    digit_to_char =  {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def backtrack(path):  # or use i, digit_to_char[digits[i]]
        if len(path) == len(digits):
            res.append(path)
            return
        for c in digit_to_char[digits[len(path)]]:
            backtrack(path + c)
        
    if digits:
        backtrack('')
    
    return res

digits = '56'
ret = letter_combinations(digits)
print(ret)
