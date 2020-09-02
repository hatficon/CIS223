import math

def main():
    playerName = input("What is the player's name?")
    hits = int(input("How many hits?"))
    bats = int(input("How many at-bats?"))
    string = (playerName + "'s batting average is " + str(hits/bats))
    print(string)


main()