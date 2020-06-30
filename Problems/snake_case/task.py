word_in = list(input())
word_out = ""

for i in range(len(word_in) - 1):
    if word_in[i].islower() and word_in[i + 1].isupper():
        word_in.insert(i + 1, "_")
        word_in[i + 2] = word_in[i + 2].lower()

for letter in word_in:
    word_out += letter

print(word_out)
