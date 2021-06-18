
def reverse_each_word(given):
    words = given.split()
    inverted_words = [word[::-1] for word in words]
    expected = " ".join(inverted_words)
    return expected

def reverse_file_text(text_file):
    try:
        with open(text_file) as f:
            input_text = f.read()
            f.close()
    except FileNotFoundError:
        input_text = None

    inverted_text = "".join(reverse_each_word(input_text))
    with open("C:\PythonTraining\Marius\python-1o1\examples\expected_file.txt", "w") as f:
        f.write(inverted_text)
    f.close()


def main():
    print(reverse_each_word("Hi my name is Jessica"))
    reverse_file_text("C:\PythonTraining\Marius\python-1o1\examples\given.txt")


if __name__ == "__main__":
    main()