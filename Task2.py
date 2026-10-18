''' Count the number of strings in a list '''
text = [12312, "ADasdasd", 13123231, 0.4343, "sfsfsd", "dsfsdfsdf", 1 < 3]
count = 0

for i in text:
    if type(i) == str:
        count += 1

print(count)