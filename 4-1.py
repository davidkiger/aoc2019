import re

min_code = 124075
max_code = 580769

regexp = re.compile(r"(.)\1")

count = 0
for val in range(min_code, max_code):
    match = re.search(regexp, str(val))
    if not match:
        continue

    digits = [int(d) for d in str(val)]
    if (digits[0] <= digits[1] and
       digits[1] <= digits[2] and
       digits[2] <= digits[3] and
       digits[3] <= digits[4] and
       digits[4] <= digits[5]):
        count += 1

print(count)
