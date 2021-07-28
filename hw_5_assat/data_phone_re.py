import re
file1 = open("src/data_phone.json", "r")
file = file1.read()

reg = re.compile("(\d{13})")
reg1 = re.findall("[(][0-6][0-9][0-9][)][ ]?[\d]{3}-[\d]{4}", file)

found = re.findall(reg, file)
phone = len(found)

print(f"Total amount of phone numbers with 13 digits: {phone}")
print(reg1)

file1.close()