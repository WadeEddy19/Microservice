
def main():
    with open('D:\\microservice\\randomNumbers.txt', 'w') as file:
        pass
    number_of_sides = input("How many sides? ")
    number_of_dice = input("How many dice? ")

    with open('D:\\microservice\\randomNumbers.txt', 'w') as file:
        file.write(number_of_dice + " " + str(number_of_sides))
        file.close()





if __name__ == '__main__':
    main()