def find_polydivisible():
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def solve(current_num, remaining_digits):
        # k is the length of the prefix we are currently forming
        k = 10 - len(remaining_digits)

        # Base case: if we have used all 9 digits
        if k == 10:
            return current_num

        for d in remaining_digits:
            next_num = current_num * 10 + d
            # Check the divisibility constraint for the current prefix length
            if next_num % k == 0:
                result = solve(next_num, [x for x in remaining_digits if x != d])
                if result:
                    return result
        return None

    return solve(0, digits)

print(find_polydivisible())
