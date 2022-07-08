# write your code here
from collections import Counter
from collections import defaultdict


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

    @property
    def undefined_content(self):
        total = 0
        for seq in self.dna_sequences:
            count = seq.count('N') / len(seq)
            total += count
        return total / len(self.seq_lengths) * 100

    @property
    def freq_undefined_seq(self):
        count = 0
        for seq in self.dna_sequences:
            if 'N' in seq:
                count += 1
        return count

    @property
    def repeats(self):
        dictionary = defaultdict(lambda *_: -1)
        for seq in self.dna_sequences:
            dictionary[seq] += 1
        return sum(dictionary.values())


def main():
    dna = DNASequence(input())
    # Need lines, lengths, amount
    print(f"Reads in the file = {len(dna.dna_sequences)}:")
    avg = sum(dna.seq_lengths) / len(dna.seq_lengths)
    print(f"Reads sequence average length = {round(avg)}")
    print()
    print(f"Repeats = {dna.repeats}")
    print(f"Reads with Ns = {dna.freq_undefined_seq}")
    print()
    print(f"\nGC content average = {round(dna.gc_content, 2)}%")
    print(f"Ns per read sequence = {round(dna.undefined_content, 2)}%")


if __name__ == "__main__":
    main()
