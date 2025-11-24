MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# Convert matrix string to 2D list

rows = MATRIX_STR.strip().split("\n")
matrix = [list(row) for row in rows]

# Read column by column

num_rows = len(matrix)
num_cols = len(matrix[0])

raw_message = ""

for col in range(num_cols):
    for row in range(num_rows):
        raw_message += matrix[row][col]

# Replace symbol groups with spaces

decoded = ""
space_needed = False

for char in raw_message:
    if char.isalpha():
        if space_needed:
            decoded += " "
            space_needed = False
        decoded += char
    else:
        space_needed = True

# Display
print(decoded)