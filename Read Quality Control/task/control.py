# write your code here
filename = input()
with open(filename, encoding="utf-8") as FASTQ_FILE:
    lines = FASTQ_FILE.readlines()
    lengths = [len(line.strip()) for line in lines[1::4]]
    amount = len(lengths)
print(f"Reads in the file = {amount}:")
for le in set(lengths):
    print(f"      with length {le} = {lengths.count(le)}")
print()
print(f"Reads sequence average length = {round(sum(lengths) / amount)}")
