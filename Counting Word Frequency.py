# Function to count word frequency in a text
def count_word_frequency(text):
    # text to upper case
    text = text.upper()

    # text split
    words = text.split()

    # Dictionary for freq
    word_freq = {}

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


if __name__ == "__main__":
    input_text = "if a wood chuck chuck wood, how much can a wood chuck chuck wood if a chuck can chuck wood?"
    word_frequencies = count_word_frequency(input_text)

    for word, freq in word_frequencies.items():
        print(f"{word}: {freq}")