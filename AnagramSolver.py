# Sorts the inputted string - much easier in python than cpp
def sort(string):
    list = sorted(string)
    return list

# Finds an anagram using all of the letters
def findAnagramAllLetters(list):
    with open('EnglishWords.txt', 'r') as EnglishWords:
        foundWords = []
        for currentWord in EnglishWords:             
            boolList = initBoolList(list)
            currentWord = currentWord.strip()
            if len(list) != len(currentWord):
                continue
            for iterator in range(len(list)):
                if doesLetterMatch(list, currentWord[iterator], boolList) == False:
                    break
            if checkBoolList(boolList) == True:
                foundWords.append(currentWord)
    return foundWords

# Checks to see if all letters have been used
def checkBoolList(boolList):
    for iterator in range(len(boolList)):
        if boolList[iterator] == False:
            return False
    return True

def initBoolList(list):
    boolList = []
    for iterator in range(len(list)):
        boolList.append(False)
    return boolList

def doesLetterMatch(list, currentLetter, boolList):
    for iterator in range(len(list)):
        if list[iterator] > currentLetter:
            return False
        elif list[iterator] == currentLetter and boolList[iterator] == False:
            boolList[iterator] = True
            return True
    return False

if __name__ == '__main__':
    string = input("Enter letters: ")
    list = sort(string)
    foundWords = findAnagramAllLetters(list)
    for iterator in range(len(foundWords)):
        print(foundWords[iterator])