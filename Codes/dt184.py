count = 0
with open("dico.txt", "r", encoding="utf-8") as f:
    for line in f:
        # Extract only alphabetic characters and convert to lowercase
        letters = [char for char in line.lower() if char.isalpha()]
        # A word is a heterogram if all its letters are unique
        if letters and len(letters) == len(set(letters)):
            count += 1

print(count)
