def solve():
    # Thomas has 10 cards with scores 1 to 10.
    # Initial ranking: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cards = list(range(1, 11))
    week = 1

    while True:
        # Check if the customer with score 10 is in 4th place (index 3).
        if cards[3] == 10:
            return week

        # Invite the client corresponding to the top card.
        score = cards.pop(0)

        # Place this card behind a number of cards equal to its score.
        # This is equivalent to inserting it at the index equal to its score.
        cards.insert(score, score)

        # Increment week count.
        week += 1

print(solve())
