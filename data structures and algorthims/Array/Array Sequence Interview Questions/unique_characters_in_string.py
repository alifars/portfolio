
from collections import Counter
def unique_characters(s):
    counter = Counter(s)
    return all(([value == 1 for value in counter.values()]))



assert(unique_characters('') ==  True)
assert(unique_characters('goo') == False)
assert(unique_characters('abcdefg') ==  True)
