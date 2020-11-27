def isPalindrome (word):
    return True if(word == word[::-1]) else False


def backCounting(word):
    if(isPalindrome(word)):
        return 0
    word = word[:-2]
    return 1 + backCounting(word)

def frontCounting(word):
    if(isPalindrome(word)):
        return 0
    word = word[1:]
    return 1 + frontCounting(word)


def comparations(word):
    return min(backCounting(word), frontCounting(word))


def main():
    word = input("Write:\n")
    # word = [c for c in input_word]
    print(comparations(word))


if __name__ == "__main__":
    main()