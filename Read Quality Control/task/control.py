# write your code here
import gzip
from typing import List
from collections import Counter
from collections import defaultdict


class DNASequence:
    def __init__(self, lines: List[str]):
        self.lines = lines

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


def lowest_undefined_data(*dna_objs):
    result = dna_objs[0]
    lowest = dna_objs[0].freq_undefined_seq
    for i, dna in enumerate(dna_objs):
        if dna.freq_undefined_seq < lowest:
            lowest = dna.freq_undefined_seq
            result = dna
    return result


def read_gz_files(files_q):
    result = []
    for i in range(files_q):
        f = gzip.open(input(), "rt")
        lines = [line.strip() for line in f.readlines()]
        dna = DNASequence(lines)
        result.append(dna)
    return result


def main():
    dnas = read_gz_files(3)
    dna = lowest_undefined_data(*dnas)
    print()
    print(f"Reads in the file = {len(dna.dna_sequences) - dna.repeats}:")
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
