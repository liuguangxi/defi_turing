# Strategy: Follower 1 is the counter.
# Participants (2-33) turn the lamp ON once when they find it OFF.
# The counter turns the lamp OFF and increments their count when they find it ON.
# When the counter's count reaches 32, all followers have visited the room.

def solve():
    with open('tirage.txt') as f:
        draws = [int(line.strip()) for line in f]

    counter = draws[0]
    others_who_turned_on = set()
    lamp_on = False
    count = 0

    for day, follower in enumerate(draws, 1):
        if follower == counter:
            if lamp_on:
                lamp_on = False
                count += 1
                if count == 32:
                    return day
        else:
            if not lamp_on and follower not in others_who_turned_on:
                lamp_on = True
                others_who_turned_on.add(follower)
    return None

print(solve())
