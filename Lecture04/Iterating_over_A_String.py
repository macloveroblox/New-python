str_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
masked_string = ""
for char in str_input:
    upper_char = char.upper()
    if upper_char in vowels:
        masked_string += "*"
    else:
        masked_string += char
print(masked_string)