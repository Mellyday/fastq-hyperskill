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

    @property
    def gc_content(self):
        all_gc_mean = []
        for seq in self.dna_sequences:
            counter = Counter()
            for nucleo in seq:
                counter[nucleo] += 1
            gc_total = counter['G'] + counter['C']
            gc_mean = gc_total / len(seq)
            all_gc_mean.append(gc_mean)
        return sum(all_gc_mean) / len(all_gc_mean) * 100


def main():
    dna = DNASequence(input())
    # Need lines, lengths, amount
    print(f"Reads in the file = {len(dna.dna_sequences)}:")
    avg = sum(dna.seq_lengths) / len(dna.seq_lengths)
    print(f"Reads sequence average length = {round(avg)}")
    print(f"\nGC content average = {round(dna.gc_content, 2)}%")


if __name__ == "__main__":
    main()
