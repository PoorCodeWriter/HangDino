hangmanword = ['d', 'i', 'n', 'o', 's', 'a', 'u', 'r']


def hang0():
    f = open("hangman.txt.py", "r")
    print(f.read())
    f.close()


def hang1():
    f = open("hangman1.py", "r")
    print(f.read())
    f.close()


def hang2():
    f = open("hangman2.py", "r")
    print(f.read())
    f.close()


def hang3():
    f = open("hangman3.py", "r")
    print(f.read())
    f.close()


def hang4():
    f = open("hangman4.py", "r")
    print(f.read())
    f.close()


def hang5():
    f = open("hangman5.py", "r")
    print(f.read())
    f.close()


def hang6():
    f = open("hangman6.py", "r")
    print(f.read())
    f.close()


def hang7():
    f = open("hangman7.py", "r")
    print(f.read())
    f.close()


def hang8():
    f = open("hangman8.py", "r")
    print(f.read())
    f.close()


def hang9():
    f = open("hangman9.py", "r")
    print(f.read())
    f.close()


hang0()
guesses = ''
turns = 8
while turns > 0:
    failed = 0
    for char in hangmanword:
        if char in guesses:
            print(char, )

        else:
            print("_", )
            failed += 1

    if failed == 0:
        print("\033[1;32;40mYou won\033[1;37;40m")
        print("You saved Mr.Dino")
        hang9()
        break
    guess = input("guess a character:")
    guesses += guess
    if guess not in hangmanword:
        turns -= 1
        print("HangDino is closer to drowned")
        print("Wrong")
        print("You have", + turns, 'more guesses')
    if turns == 0:
        print("You killed Mr.Dino")
        print("\033[1;31;40mYou Lose\033[1;35;40m\n")
    if turns == 7:
        hang1()
    if turns == 6:
        hang2()
    if turns == 5:
        hang3()
    if turns == 4:
        hang4()
    if turns == 3:
        hang5()
    if turns == 2:
        hang6()
    if turns == 1:
        hang7()
    if turns == 0:
        hang8()
