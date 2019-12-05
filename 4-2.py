import re

min_code = 124075
max_code = 580769

regexp = re.compile(r"(.)\1")
doubles = ['11', '22', '33', '44', '55', '66', '77', '88', '99', '00']
triples = ['111', '222', '333', '444', '555', '666', '777', '888', '999', '000']

count = 0
for val in range(min_code, max_code):
    match = re.search(regexp, str(val))
    if not match:
        continue

    db_c = 0
    tp_c = 0
    for db in doubles:
        if db in str(val):
            db_c += 1

    for tp in triples:
        if tp in str(val):
            tp_c += 1

    if tp_c >= db_c:
        continue

    digits = [int(d) for d in str(val)]
    if (digits[0] <= digits[1] and
       digits[1] <= digits[2] and
       digits[2] <= digits[3] and
       digits[3] <= digits[4] and
       digits[4] <= digits[5]):
        count += 1

print(count)
