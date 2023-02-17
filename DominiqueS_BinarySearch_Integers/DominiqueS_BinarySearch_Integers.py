
# Array = Dataset being used (In this case a list of numbers)
# Query = Whatever number the user inputed to search
# Length = Current high range of list
# Start = Current low range of list
# HeroArray = The array of heroes to be compared to later

def check(array, query, length, start, heroArray):                  # Passing through values from previous function (I probably could have used 1 instead of 2)

    global numberNotFound
    global previousIndex

    index = int(length + (start - length) // 2)                     # Index is set to half of the current range

    if (index != previousIndex):                                    # Fallback in case program gets stuck on the value closest to the query
        if (array[index] == query):
            hero = compare(array, index, heroArray)                 # Obtains name of hero with matching power value
            return print(f"Your Selected Hero, {hero} Was Found At Index {index+1} with a power level of {query}!\n")
      
        elif (array[index] > query):                                # Since the array is sorted in order from highest to lowest, it checks the values of
            previousIndex = index                                   # whatever number is at the current index and sets the current floor or ceiling of the range
            return check(array, query, index, start, heroArray)    # in accordance to whatever the case may be.
                                                                    
        elif (array[index] < query):                                # eg. query = 70, dataset = [55, 60, 71, 75], it would start at 60, due to rounding, then
            previousIndex = index                                   # it would see that 70 is larger than 60 and would move the floor upwards.
            return check(array, query, length, index, heroArray)             
    else:
        return print("Sorry, The Selected Power Level Doesn't Match Any Hero In Our Database.\n")

def compare(array, index, heroArray):

    global previousHero
    power = array[index]                                            # Compares the two lists (ugly elif ladder I know) to check which hero has been chosen

    if (power == 0.10):
        heroindex = 0
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Scrap Metal"
        previousHero = 0

    elif (power == 0.42):
        heroindex = 1
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Hairless Cat"
        previousHero = 1

    elif (power == 0.50):
        heroindex = 2
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Pea Plant"
        previousHero = 2

    elif (power == 0.64):
        heroindex = 3
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Mr. Cube Man"
        previousHero = 3

    elif (power == 0.69):
        heroindex = 4
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Space Alien Monkey"
        previousHero = 4

    elif (power == 0.75):
        heroindex = 5
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Egyptian Cat"
        previousHero = 5

    elif (power == 0.80):
        heroindex = 6
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Red Balloon"
        previousHero = 6

    elif (power == 0.87):
        heroindex = 7
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Slugcat"
        previousHero = 7

    elif (power == 0.90):
        heroindex = 8
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Mrs. Woman"
        previousHero = 8

    elif (power == 0.99):
        heroindex = 9
        if (previousHero == heroindex):
            print("Your Selected Superhero Has Lost Their Power!")
            heroArray[heroindex] = "Gamer Boyfriend"
        previousHero = 9

    return heroArray[heroindex]                                     # Returns current hero name to print in the output later

# ------------------------------------------------------------------------------------------------------------------------ #
                                                                    # The start of the program (in terms of code run)
heroes = ["Amazon Alexa", 
          "Bingle", 
          "Peashooter from hit indie game Plants Vs. Zombies", 
          "Minecraft Steve",  
          "Goku", 
          "Ned", 
          "Bloon from BloonsTD6", 
          "Scug", 
          "Your Mom", 
          "Sir Chromium"]
integers = [0.42, 0.90, 0.75, 0.99, 0.87, 0.69, 0.80, 0.64, 0.10, 0.50 ] # Current dataset (could be implemented in a way that the data is entered instead of hardcoded)
integers.sort()                                                     # Sorts dataset (important for later in program)
length = len(integers)

numberNotFound = True
previousIndex = -1
previousHero = -1

while numberNotFound:
    query = input("Input A Power Level (0.00 - 0.99) To Check If Your Hero Is In The Database, Or Type 'exit' To Exit The Program:\n")
    try:
        query = float(query)                                        # Small try-except check for if the user enters an input that isn't numerical
        if (query > 9000):
            print("That Power Level Is Way Too High! It's Over 9000!\n")        
        elif (query > 0.99):
            print("Woah! That Power Level Is Too High! Please Input A Smaller Value.\n")
        else:
            check(integers, query, length, 0, heroes)                   # Runs the search function above
    except:
        if (query == "exit"):
            print("Thank You For Using Our Program.")
            quit()                                                  # Typing 'exit' kills the program
        else:
            print("Invalid Input, Please Try Again.\n")
    
# Finally finished! Not too bad once the groundwork was laid out.
# Notable Changes:
#   - Added a variable to check if picked hero is same as the last hero
#   - Changes list permanently so they dont magically regain power





