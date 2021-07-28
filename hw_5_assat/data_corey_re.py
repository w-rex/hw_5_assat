import re
with open("./src/data_corey.txt", "r") as text:
    nums = 0
    end7 = 0
    for line in text:
        search = re.compile(r"[\d]{3}-[\d]{3}-[\d]{4}")
        n7 = re.compile(r"[\d]{3}-[\d]{3}-[\d]{3}7$")
        f = re.search(search, line)
        found7 = re.search(n7, line)
        if f:
            nums += 1
        if found7:
            end7 += 1


print(f"Total amount of phone numbers: {nums}")
print(f"Total amount of phone numbers with ending 7: {end7}")
text = text.close()