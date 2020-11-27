import sys

def justify(text, max_width=30):
    sliced = []

    for letter in text:
        sliced.append(letter)

    for index, item in enumerate(sliced):
        if index % (max_width+1) == 0:
            sliced.insert(index, '\n')

            if sliced[index+1] == ' ':
                sliced[index+1] = ''

    for item in sliced:
        sys.stdout.write(item)
    sys.stdout.write('\n')

def main():
    just = input('Ingresá un texto: ')
    justify(just)

main()