bit = "101111111000"
count = 0
result = ""

for i in bit:
    if i == '1':
        count += 1
    else:
        count = 0  # Reset count if the character is not '1'
    
    result += i  # Add the current character to the result
    
    # Check if we've counted exactly five consecutive '1's
    if count == 5:
        result += '0'  # Append a '0' after five consecutive '1's
        count = 0  # Reset count to check for the next sequence

print(result)
