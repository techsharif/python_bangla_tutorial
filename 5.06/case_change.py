char = "p"
ascii_value = ord(char)

lower_case_ascii_value = ascii_value + 32
upper_case_ascii_value = ascii_value - 32

lower_case = chr(lower_case_ascii_value)
upper_case = chr(upper_case_ascii_value)

output = (ascii_value <= 90 and lower_case) or upper_case
print(output)