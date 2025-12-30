import collections

t9_map = str.maketrans("abcdefghijklmnopqrstuvwxyz", "22233344455566677778889999")
counts = collections.defaultdict(int)

with open("dico.txt", "r", encoding="utf-8") as f:
    for line in f:
        word = line.strip().lower()
        if word.isalpha():
            counts[word.translate(t9_map)] += 1

print(max(counts, key=counts.get))
