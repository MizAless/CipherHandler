def print_ascii_pairs_with_diff(s):
    pairs = [s[i:i+2] for i in range(0, len(s), 2)]
    for pair in pairs:
        ascii_nums = [str(ord(c)) for c in pair]
        diff = int(ascii_nums[0]) - int(ascii_nums[1])
        abs_diff = abs(diff)
        ascii_diff = chr(abs_diff)
        print(' '.join(ascii_nums), abs_diff, ascii_diff)

input_string = input("Введите строку: ")
print_ascii_pairs_with_diff(input_string)