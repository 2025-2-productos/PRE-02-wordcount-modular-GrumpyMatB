# obtain a list of files in the input directory

from ._internals.count_words import count_words
from ._internals.preprocess_lines import preprocess_lines
from ._internals.read_all_lines import read_all_lines
from ._internals.split_in_words import split_in_words
from ._internals.write_count_words import write_count_words


def main():

    ##mover a función "read all lines"
    all_lines, input_files_list = read_all_lines()

    ###mover a función "preprocess lines"
    all_lines = preprocess_lines(all_lines)

    ###mover a función "split in words"
    words = split_in_words(all_lines)

    # count the frequency of the words in the files in the input directory
    counter = count_words(input_files_list)

    write_count_words(counter)


if __name__ == "__main__":
    main()
