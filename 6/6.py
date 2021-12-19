with open('input.txt') as file:
    binaryStrings = file.read().splitlines()


def find_life_support_ratings(binary_strings, index, is_most_common_digit):
    if len(binary_strings) == 1:
        return binary_strings

    binary_strings_by_digit = {
        "0": [],
        "1": []
    }
    for binary_string in binary_strings:
        if binary_string[index] == "1":
            binary_strings_by_digit["1"].append(binary_string)
        else:
            binary_strings_by_digit["0"].append(binary_string)

    most_common_digit = "0"
    least_common_digit = "0"
    if len(binary_strings_by_digit["1"]) == len(binary_strings_by_digit["0"]):
        most_common_digit = "1" if is_most_common_digit else "0"
    elif len(binary_strings_by_digit["1"]) > len(binary_strings_by_digit["0"]):
        most_common_digit = "1"
    else:
        least_common_digit = "1"

    if is_most_common_digit:
        return find_life_support_ratings(binary_strings_by_digit[most_common_digit], index + 1, True)

    return find_life_support_ratings(binary_strings_by_digit[least_common_digit], index + 1, False)


print(int(find_life_support_ratings(binaryStrings, 0, False)[0], 2) *
      int(find_life_support_ratings(binaryStrings, 0, True)[0], 2))
