def count_words(text):
    words = text.split()
    return len(words)

def main():
    text = input("Enter a sentence or paragraph: ")
    if len(text)==0:
        print("Empty text")
    else:
        word_count = count_words(text)
        print("Number of words:", word_count)

if __name__ == "__main__":
    main()