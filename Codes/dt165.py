import collections

def solve():
    # Range of the third millennium
    START, END = 2001, 3000
    counts = collections.Counter()

    # Opening the dictionary file dico.txt
    with open('dico.txt', 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip().lower()
            product = 1
            for char in word:
                if 'a' <= char <= 'z':
                    # Assigning a=1, b=2, ..., z=26
                    product *= (ord(char) - ord('a') + 1)

            # Check if the product falls within the third millennium
            if START <= product <= END:
                counts[product] += 1

    # Finding the most frequent year and its frequency
    year, freq = counts.most_common(1)[0]
    return year * freq

print(solve())
