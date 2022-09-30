from string import ascii_letters
from collections import deque

# def get_neighbors(word):
#     for i in range(len(word)):
#         # replace word[i] with every ascii letter
#         for c in ascii_letters:
#             next_word = word[:i] + c + word[i + 1:]
#             # this is pseudo code
#             if in_wordlist(next_word):
#                 process(next_word)

def get_neighbors(word):
    for i in range(len(word)):
        for c in ascii_letters:
            if c == word[i]:
                continue
            next_word = word[:i] + c + word[i+1:]
            yield next_word

def word_ladder(start, end, word_list):
    q = deque([start])
    words = set(word_list)

    distance = 0
    distance = {start:0}

    while q:
        n = len(q)
        # distance += 1
        # for _ in range(n):
        #     word = q.popleft()

        #     for i in range(len(word)):
        #         for n_word in get_neighbors(word):
        #             if n_word not in words:
        #                 continue
        #             if n_word == end:
        #                 return distance
        #             q.append(n_word)
        #             words.remove(n_word)

        word = q.popleft()
        for i in range(len(word)):
            for n_word in get_neighbors(word):
                if n_word not in words:
                    continue
                # it's like having a else here:
                distance[n_word] = distance[word] + 1
                if n_word == end:
                    return distance[n_word]
                q.append(n_word)
                words.remove(n_word)
    return 0

start = "COLD"
end = "WARM"
word_list = ["COLD", "GOLD", "CORD", "SOLD", "CARD", "WARD", "WARM", "TARD"]
ret = word_ladder(start, end, word_list)
print(ret)



