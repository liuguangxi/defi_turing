import collections

count = 0
with open("dico.txt", "r", encoding="utf-8") as f:
    for line in f:
        # Extract only alphabetic characters and convert to lowercase
        letters = [char for char in line.lower() if char.isalpha()]

        if letters:
            # Count the occurrences of each letter
            counts = collections.Counter(letters)

            # A gemellogram is a word where every letter appears exactly twice
            if all(v == 2 for v in counts.values()):
                count += 1

print(count)
