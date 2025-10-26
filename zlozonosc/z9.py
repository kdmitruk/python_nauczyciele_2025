def permutation(seq):
    n = len(seq)

    i = n - 2
    while i >= 0 and seq[i] >= seq[i+1]:
        i -= 1

    if i == -1:
        return None

    j = n - 1
    while seq[j] < seq[i]:
        j -= 1

    seq[i], seq[j] = seq[j], seq[i]

    seq[i+1:] = reversed(seq[i+1:])


    return seq


text = "ABCDE"
chars = sorted(list(text))

counter = 0
while chars:
    print(chars)
    chars = permutation(chars)
    counter += 1

print(counter)

# O(N) = N!
# M(N) = N




