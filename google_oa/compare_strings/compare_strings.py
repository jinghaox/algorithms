from typing import List

def compare_strings_mine(str1: List[str], str2: List[str]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    ret = []
    str2_list = []
    for s2 in str2:
        all_chars = [x for x in s2]
        smallest_char = min(all_chars)
        s2_dict = {}
        # s2_dict[smallest_char] = all_chars.count(smallest_char)
        # str2_list.append(s2_dict)
        s2_smallest_count = all_chars.count(smallest_char)
        str2_list.append(s2_smallest_count)

    str1_list = []
    for s1 in str1:
        all_chars = [x for x in s1]
        smallest_char = min(all_chars)
        s1_dict = {}
        # s1_dict[smallest_char] = all_chars.count(smallest_char)
        # str1_list.append(s1_dict)
        s1_smallest_count = all_chars.count(smallest_char)
        str1_list.append(s1_smallest_count)

    
    for y in str2_list:
        cnt = 0
        for x in str1_list:
            # v1 = list(x.values())[0]
            # v2 = list(y.values())[0]
            # if v1<v2:
            if x < y:
                cnt += 1
        ret.append(cnt)    
        
    return ret

MAX_STRING_SIZE = 10

# "Lex Count" is the short hand for the occurrence of the lexicographically smallest
# character present.
def find_lex_count(test_str: str) -> int:
    min_character = None
    min_count = 0
    for char in test_str:
        if min_character is None or char < min_character:
            min_character = char
            min_count = 1
        elif min_character == char:
            min_count += 1
    return min_count

def compare_strings(str1: List[str], str2: List[str]) -> List[int]:
    # This keeps track of the number of strings in str1 has a particular lex index.
    lex_counts = [0] * (MAX_STRING_SIZE + 1)
    for one_str in str1:
        # str1 lex_count is [1, 2, 1], i.e. first one has 1 smallest, second string has 2 smallest, then 1 smallest
        # so totally 2 strings have 1 smallest, 1 string has 2 smallest
        # lex_counts is [0,2,1,0,0,...0]
        lex_counts[find_lex_count(one_str)] += 1

    # This keeps track of how many strings in str1 has a lex index less than the key.
    strictly_smaller_count = [0]
    for entry in lex_counts:
        strictly_smaller_count.append(strictly_smaller_count[-1] + entry)
    print(strictly_smaller_count)
    # [0,0,2,3,3,...]
    # 0 strings has lex index < 0
    # 0 strings has lex index < 1 (==0)
    # 2 strings has lex index < 2 (==1)
    # 3 strings has lex index < 3 (==1 and ==2)
    # 3 strings has lex index < 4 (==1 and ==2 and ==3) has no strings has lex index 3


    return_count = []
    for one_str in str2:
        print(one_str)
        print(find_lex_count(one_str))
        return_count.append(strictly_smaller_count[find_lex_count(one_str)])
    return return_count

str1 = ['abcd', 'aabc', 'bd']
str2 = ['aaa', 'aa']
# ret = compare_strings(str1,str2)
ret = compare_strings_mine(str1,str2)
print(ret)
