import random


def choose_word():
    words = ['python', 'java', 'javascript',
             'ruby', 'php', 'html', 'css', 'perl']
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display


def main():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Adivinhe uma letra: ").lower()

        if guess in guessed_letters:
            print("Você já tentou essa letra. Tente outra.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Letra incorreta. Você tem {} tentativas restantes.".format(attempts))
            if attempts == 0:
                print("Você perdeu! A palavra era:", word)
                break
        else:
            print("Letra correta!")
            display = display_word(word, guessed_letters)
            print(display)
            if '_' not in display:
                print("Parabéns! Você ganhou!")
                break


if __name__ == "__main__":
    main()
