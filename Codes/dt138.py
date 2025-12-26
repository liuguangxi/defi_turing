def solve():
    # The dictionary file is assumed to be in the current directory.
    # We look for words where the sequence of vowels (a, e, i, o, u)
    # follows the cyclic successor rule: each vowel must be the
    # immediate next one in the "aeiou" cycle.
    vowels = "aeiou"
    v_idx = {v: i for i, v in enumerate(vowels)}
    count = 0

    with open('dico.txt', 'r', encoding='utf-8') as f:
        for line in f:
            word = line.strip().lower()
            # Extract vowels in the word, ignoring consonants and 'y'.
            v_seq = [v_idx[c] for c in word if c in v_idx]
            # A word must contain at least one vowel.
            # All consecutive vowels must follow the cycle a->e->i->o->u->a.
            if v_seq and all(v_seq[i+1] == (v_seq[i] + 1) % 5 for i in range(len(v_seq) - 1)):
                count += 1
    print(count)

solve()
