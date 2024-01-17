# character_dict = {}
#
# text = input()
#
# for char in text:
#     character_dict[char] = character_dict.get(char, 0) + 1
#
#
# sorted_character_dict = sorted(character_dict.items())
#
# print(f'{char}: {count}' for char, count in sorted_character_dict)

text = input("Enter text: ")

# Using a dictionary to count occurrences of each character
character_counts = {}
for char in text:
    if char.isalpha():  # consider only alphabetic characters
        char = char.lower()  # convert to lowercase to treat 'A' and 'a' as the same character
        character_counts[char] = character_counts.get(char, 0) + 1

# Sorting the dictionary by keys in lexicographical order
sorted_character_counts = sorted(character_counts.items())

# Printing the results
print("Character counts:")
for char, count in sorted_character_counts:
    print(f"{char}: {count} time{'s' if count > 1 else ''}")