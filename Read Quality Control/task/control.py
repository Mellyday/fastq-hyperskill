# write your code here
from collections import Counter


class DNASequence:
    def __init__(self, filename):
        with open(filename) as file:
            self.lines = [line.strip() for line in file.readlines()]

    @property
    def dna_sequences(self):
        sequences = [line for line in self.lines[1::4]]
        return sequences

    @property
    def seq_lengths(self):
        lengths = [len(line) for line in self.dna_sequences]
        return lengths


def main():
    dna = DNASequence(input())
    # Need lines, lengths, amount
    print(f"Reads in the file = {len(dna.dna_sequences)}:")
    counter = Counter(dna.seq_lengths)
    for length, count in counter.items():
        print(f"      with length {length} = {count}")
    print()
    avg = sum(dna.seq_lengths) / len(dna.seq_lengths)
    print(f"Reads sequence average length = {round(avg)}")


if __name__ == "__main__":
    main()
