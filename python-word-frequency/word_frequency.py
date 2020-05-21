import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


def get_file_contents(file):
    """
    Given a filename `file`, open the file, read the contents into a string, and close the file.
    Return the contents.
    """

    opened_file = open(file)
    contents = opened_file.read()
    opened_file.close()
    return contents


def get_words_from_string(a_string):
    """
    Given a string full of words, break that string into the words, lowercase them,
    and remove all punctuation.
    """
    words = a_string.split()
    cleaned_words = [word.lower().strip(string.punctuation) for word in words]
    return cleaned_words


def calculate_freqs(a_list):
    """
    Given a list of strings, count how many times each string appears in the list
    and return a dict of those counts.
    """
    freqs = {}
    for item in a_list:
        freqs[item] = freqs.get(item, 0) + 1

        ## same as:
        # if word in word_freqs:
        #     word_freqs[word] += 1
        # else:
        #     word_freqs[word] = 1

    return freqs


def remove_stop_words(words):
    return [word for word in words if word not in STOP_WORDS]


def get_second_item(seq):
    return seq[1]


def print_freq_table(word_freqs):
    sorted_word_freqs = sorted(word_freqs.items(),
                               key=get_second_item,
                               reverse=True)
    words_to_display = [freq[0] for freq in sorted_word_freqs[:10]]
    longest_word_length = max([len(word) for word in words_to_display])
    for word, count in sorted_word_freqs[:10]:
        print(word.rjust(longest_word_length + 1), "|",
              str(count).ljust(4), "*" * count)


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    contents = get_file_contents(file)
    words = get_words_from_string(contents)
    words = remove_stop_words(words)
    word_freqs = calculate_freqs(words)
    print_freq_table(word_freqs)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
