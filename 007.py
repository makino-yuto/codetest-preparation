count = {}

count[3] = 2
count["eg"] = "3g"
count["5"] = "gji"

print(count)

for key, value in count.items():
    print(key, value)

for key in count.keys():
    print(key)

for value in count.values():
    print(value)