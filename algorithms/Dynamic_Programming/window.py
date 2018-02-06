import random
import time

t1 = time.time()
window_len = 100000
# window = [1, 3, -1, -3, 5, 3, 6, 7]
window = [random.randint(0, 543556334) for _ in range(1000000)]
cache = []

cache.append((-1,-1))
cache.append((min(window[0:window_len]), max(window[0:window_len])))

print(time.time()-t1)
t = time.time()
for i in range(1, len(window)-window_len+1):

    min_, max_ = cache[i]
    if window[i-1] == min_:
        if window[i+window_len-1] < min_:
            min_ = window[i+window_len-1]
        else:
            min_ = min(window[i:i+window_len-1])
    if window[i-1] == max_:
        if window[i+window_len-1] > max_:
            max_ = window[i+window_len-1]
        else:
            max_ = max(window[i:i + window_len])

    if i+window_len-1 <= len(window) - 1 and window[i+window_len-1] > max_:
        max_ = window[i+window_len-1]
    if i+window_len-1 <= len(window) - 1 and window[i + window_len-1] < min_:
        min_ = window[i + window_len-1]

    cache.append((min_,max_))

print(cache[-1])
print(time.time()-t)