import random
# reads a file that has the number of dice being rolled followed by the number of sides on the dice
# number of dice is the first number, number of sides is the second number
def main():
    with open('D:\\microservice\\randomNumbers.txt', 'r') as file: #Enter file path that contains numbers to be received
        characters = []                                            #The microservice expecting 2 numbers seperated by a space
        while True:

            number = file.read(1)
            if number.isdigit() == True or number == " ":
                characters.append(number)
            elif number.isdigit() == False:
                break

    #loop through characters and form them into new lists of number of dice and number of sides
    number_of_dice = []
    number_of_sides = []
    number_of_dice_flag = True
    for i in range(0, len(characters)):
        char = characters[i]
        if char.isdigit() == True and number_of_dice_flag == True:
            number_of_dice.append(char)
        elif char == " ":
            number_of_dice_flag = False
        if char.isdigit() == True and number_of_dice_flag == False:
            number_of_sides.append(char)

    #convert the number of dice and number of sides lists into ints
    number_of_dice = ''.join([str(char) for char in number_of_dice])
    number_of_sides = ''.join([str(char) for char in number_of_sides])
    number_of_dice = int(number_of_dice)
    number_of_sides = int(number_of_sides)
    print()

    with open('D:\\microservice\\randomNumbersOutput.txt', 'w') as file:        #enter your file path for the outputted
        file.write('@')                                                         # random numbers
        for i in range(number_of_dice):
            number = random.randint(1, number_of_sides)
            file.write(str(number))
            file.write(' ')



if __name__ == '__main__':
    main()