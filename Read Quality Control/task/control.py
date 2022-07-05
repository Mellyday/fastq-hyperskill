# write your code here
from collections import defaultdict
length_dict = defaultdict(lambda *_: 0)

filename = input()
reads_num = 0
with open(filename, encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines[1::4]:
        reads_num += 1
        length = len(line)
        length_dict[length] = length_dict[length] + 1
print(f"Reads in the file = {reads_num}:")
total_length = 0
for length, num in length_dict.items():
    total_length += length * num
    print(f"      with length {length} = {num}")
print(f"Reads sequence average length = {round(total_length / reads_num)}")
