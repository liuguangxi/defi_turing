def solve():
    """
    Solves the cryptarithm CHAT + CHAT = MINOU.
    Each letter {C, H, A, T, M, I, N, O, U} represents a unique digit.
    Finds the smallest (x) and largest (y) possible values for MINOU and returns x + y.
    """
    results = []
    # CHAT must be at least 5000 for MINOU to be a 5-digit number.
    for chat in range(5000, 10000):
        minou = 2 * chat
        # MINOU is always 5 digits since 2 * 5000 = 10000 and 2 * 9999 = 19998.

        s_chat = str(chat)
        s_minou = str(minou)

        # Letters represent 9 distinct digits.
        # Digits of CHAT (C, H, A, T) and MINOU (M, I, N, O, U) are extracted.
        letters_digits = [
            s_chat[0], s_chat[1], s_chat[2], s_chat[3],  # C, H, A, T
            s_minou[0], s_minou[1], s_minou[2], s_minou[3], s_minou[4]  # M, I, N, O, U
        ]

        # In cryptarithms, the leading letters of words (C and M) cannot be 0.
        # Since chat >= 5000, s_chat[0] is >= 5 and s_minou[0] is 1. Both are non-zero.
        if len(set(letters_digits)) == 9:
            results.append(minou)

    x = min(results)
    y = max(results)
    return x + y

print(solve())
