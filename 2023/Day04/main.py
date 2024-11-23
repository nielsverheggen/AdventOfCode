word_counts = [len(set(line[:40].split()) & set(line[42:].split())) for line in open('input.txt')]
cumulative_counts = [1] * len(word_counts)

for index, count in enumerate(word_counts):
    for offset in range(count):
        cumulative_counts[index + offset + 1] += cumulative_counts[index]

total_sum = sum(2 ** (count - 1) for count in word_counts if count > 0)
cumulative_sum = sum(cumulative_counts)

print(total_sum, cumulative_sum)