import modules.game as g
from modules.questions import *
import json as j


class mode:
    # Mode is a class which is used to store the mode of transport
    # It contains all the information about this transport
    # Including speed, its optimal distance, optimal weather, and its name

    def __init__(self, name, speed, minDis, maxDis, optimalWeather):
        self.name = name
        self.speed = speed
        self.minDis = minDis
        self.maxDis = maxDis
        # Array, since there can be transport which
        # are optimal for multiple kinds of weather
        self.optimalWeather = optimalWeather

        # Optimal weather is a dictionary array
        # responsible for determining whether the mode of transport is optimal
        # in a certain situation(refer to function below)
        # Format:
        # {
        #     "rain": optimal intensities of rain in array form,
        #     "snow": optimal intensities of snow in array form,
        #     "wind": optimal intensities of win in array form,
        #     "other": other optimal weather types in array form
        # }
        # Instead of number indexes, dictionary arrays
        # uses string indexes, or keys, to access its elements.
        # Therefore we are able to give our elements a name, making it very easy
        # to find and change its elements.

    def calcTime(self, distance):
        # This function calculates the time it takes to travel a certain distance
        # It takes in the distance as a parameter
        # And returns the time it takes to travel that distance

        time = distance / self.speed
        # time is a float rounded to 2 decimal places
        return round(time, 2)

    def isOptimal(self, distance, rain, snow, wind, other):
        # This function checks if the mode of transport is optimal for the situation
        # It takes in the distance and the weather as parameters
        # And returns a boolean value
        # True if the mode of transport is optimal for the situation
        # False if the mode of transport is not optimal for the situation

        if distance >= self.minDis and distance <= self.maxDis:
            # If the distance is within the optimal distance range
            if rain in self.optimalWeather["rain"]:
                # If the rain intensity is optimal
                if snow in self.optimalWeather["snow"]:
                    # If the snow intensity is optimal
                    if wind in self.optimalWeather["wind"]:
                        # If the wind intensity is optimal
                        if other in self.optimalWeather["other"]:
                            # If the other weather type(s) is optimal
                            return True
            return False
        else:
            return False


situation = {
    "rain": None,  # All start with None as the user hasn't started inputting yet
    "snow": None,
    "wind": None,
    "other": None,
    "distance": None,
    "avaliableTransports": [
        mode("Car", 60, 10, 300, {
            "rain": ["medium", "light", "none"],
            "snow": ["medium", "light", "none"],
            "wind": ["medium", "light", "none"],
            "other": ["sunny", "cloudy", "none"]
        }),
        mode("Train", 100, 50, 1000, {
            "rain": ["heavy", "medium", "light", "none"],
            "snow": ["heavy", "medium", "light", "none"],
            "wind": ["heavy", "medium", "light", "none"],
            "other": ["sunny", "cloudy", "none"]
        }),
        mode("Plane", 800, 200, 10000, {
            "rain": ["heavy", "medium", "light", "none"],
            "snow": ["medium", "light", "none"],
            "wind": ["heavy", "medium", "light", "none"],
            "other": ["sunny", "cloudy", "none"]
        }),
        mode("Bus", 50, 10, 100, {
            "rain": ["heavy", "medium", "light", "none"],
            "snow": ["heavy", "medium", "light", "none"],
            "wind": ["medium", "light", "none"],
            "other": ["sunny", "cloudy", "none"]
        }),
        mode("Walking", 5, 0, 10, {
            "rain": ["light", "none"],
            "snow": ["light", "none"],
            "wind": ["medium", "light", "none"],
            "other": ["sunny", "cloudy", "none"]
        }),
        mode("Bicycle Riding", 20, 0, 50, {
            "rain": ["light", "none"],
            "snow": ["light", "none"],
            "wind": ["medium", "light", "none"],
            "other": ["sunny", "cloudy", "none"]
        }),
        mode("Running", 15, 0, 10, {
            "rain": ["light", "none"],
            "snow": ["none"],
            "wind": ["medium", "light", "none"],
            "other": ["sunny", "cloudy", "none"]
        })
    ]  # All the transport modes. You can add or change some if you want
}


print("Welcome to the Journey Planner!")
q = question("Open or new journey", ["open", "new"])
action = q.ask()
print("")

# If the action is "new", repeats itself forever(until the loop is broken)
while True and action == "new":
    optimal = None  # Optimal transport not decided yet

    # Just repeats itself until the program has finished
    # The bottom code determines the current intensity of rain
    # It is the same for determining the current intensities of snow and wind
    rain = question("Is it raining, currently", [
                    "y", "n"])  # Asks if it is raining
    ans = rain.ask()  # Asks for the answer
    if ans == "y":  # If it is raining
        situation["other"] = "none"  # There is no other weater
        situation["rain"] = ""  # Prepare the situation["rain"] variable
        rain = question("How heavy is it raining", [
            "storm", "heavy", "medium", "light"
        ])
        # Four options for the intensity of rain:
        # storm, heavy, medium, light
        situation["rain"] = rain.ask()  # Sets the intensity of rain
        if situation["rain"] == "storm":  # If it is stormy
            print("Don't go out. It's too dangerous.")  # Warns the user
            game = question(
                "Meanwhile, would you want to play a game while you wait for the rain to stop", [
                    "y", "n"]
            )  # Asks if the user wants to play a game
            if game.ask() == "y":  # If the user wants to play a game
                print("You have been transported to a game. \n")
                g.game("raining")  # Starts the game
                ans = "n"
                # The user has finished playing the game, therefore it is not raining
                # anymore. Refer to game(event) in modules/game.py for more information
            else:  # If the user doesn't want to play a game
                break
                # Exits the journey planner, because the rain is too dangerous.
                # But the user doesn't want to play a game to wait for the rain to stop.
        else:
            situation["snow"] = "none"  # If it is raining, there is no snow
    if ans == "n":  # If it is not raining
        situation["rain"] = "none"  # There is no rain

        # The same for snow
        snow = question("Is it snowing", ["y", "n"])
        ans = snow.ask()
        if ans == "y":
            situation["other"] = "none"
            situation["snow"] = ""
            snow = question("How heavy is it snowing", [
                "storm", "heavy", "medium", "light"
            ])
            situation["snow"] = snow.ask()
            if situation["snow"] == "storm":
                print("Don't go out. It's too dangerous.")
                game = question(
                    "Meanwhile, would you want to play a game while you wait for the snow to stop", ["y", "n"])
                if game.ask() == "y":
                    print("You have been transported to a game. \n")
                    g.game("snowing")
                    ans = "n"  # Therefore no more rain once game has finished
                    # Refer to g.game() for more info.
                else:
                    break
        if ans == "n":

            # If it is not snowing or raining, then it is sunny or cloudy
            situation["snow"] = "none"
            situation["other"] = ""
            other = question("Is it sunny", ["y", "n"])
            ans = other.ask()
            if ans == "y":
                situation["other"] = "sunny"
            elif ans == "n":
                situation["other"] = "cloudy"

    # The same for wind
    wind = question("Is there any wind", ["y", "n"])
    ans = wind.ask()
    if ans == "y":
        situation["wind"] = ""
        wind = question("How heavy is the wind", [
                        "storm", "heavy", "medium", "light"])
        ans = wind.ask()
        situation["wind"] = ans
        if situation["wind"] == "storm":
            print("Don't go out. It's too dangerous.")
            game = question(
                "Meanwhile, would you want to play a game while you wait for the wind to stop", ["y", "n"])
            if game.ask() == "y":
                print("You have been transported to a game. \n")
                g.game("windy")
                ans = "n"
            else:
                break
    if ans == "n":
        situation["wind"] = "none"

    # The program will ask the user how far they want to travel
    dis = question("How far do you want to travel in km", "PosInt")
    situation["distance"] = dis.ask()

    # Asks if the user is in a hurry
    hurry = question("Are you in a hurry", ["y", "n"])
    ans = hurry.ask()
    print("")  # New line
    if ans == "y":
        # If the user is in a hurry, then the program will only show the fastest mode of transport
        modes = []  # List of optimal modes of transport
        modesTime = []  # List of times of optimal modes of transport
        for i in situation["avaliableTransports"]:  # For each mode of transport
            if i.isOptimal(situation["distance"], situation["rain"], situation["snow"], situation["wind"], situation["other"]):
                # Determines if it is optimal
                modes.append(i)  # Add it to the list of optimal modes
                # Add the time it takes to the list of times
                modesTime.append(i.calcTime(situation["distance"]))
        if len(modes) == 0:  # If there are no optimal modes of transport
            print(
                "There is no mode of transport that is optimal for you in this situation."
            )
            optimal = None  # Sets optimal to None
        else:
            # Now find the fastest
            fastest = min(modesTime)
            # Get index of fastest
            index = modesTime.index(fastest)
            print(
                f"The fastest optimal mode of transport is {modes[index].name} which takes {fastest} hours.")
            # Sets optimal to the fastest mode of transport
            optimal = modes[index]
    elif ans == "n":
        # If the user is not in a hurry, then the program will show all the optimal modes of transport
        optimal = []  # List of optimal modes of transport
        for i in situation["avaliableTransports"]:
            if i.isOptimal(situation["distance"], situation["rain"], situation["snow"], situation["wind"], situation["other"]):
                optimal.append(i)
        if len(optimal) == 0:
            print("There are no optimal modes of transport for this situation.")
            optimal = None
        else:
            print("The optimal modes of transport are:")
            for i in optimal:  # For each optimal mode of transport, prints the name and time it takes
                print(
                    f" - {i.name} which takes {i.calcTime(situation['distance'])} hours.")

    # Asks if the user wants to save their journey
    q5 = question("\nDo you want to save your journey", ["y", "n"])
    ans = q5.ask()  # Gets answer
    if ans == "y":  # If the user wants to save their journey
        if optimal == None:  # If there is no optimal mode of transport
            print(
                "There is no optimal transport in this situation and thus it cannot be saved."
            )  # Cannot save
        else:
            name = ""  # Prepares the name of journey
            invalidNames = ["list", "quit", ""]  # Invalid names
            # These names are invalid because they are commands
            # or because they are empty
            while name in invalidNames:  # While the name is invalid
                q6 = question(
                    "What name should this journey be called", "string"
                )  # Asks for name
                name = q6.ask()  # Gets name
                if name in invalidNames:  # If the name is invalid
                    print("Invalid name.")  # Prints error message

            # Opens data file
            with open("journey.json", "r+") as file:
                try:
                    content = file.read()
                    json = j.loads(content)
                    if type(optimal) == list:
                        # Find optimal
                        modes = []
                        modesTime = []
                        for i in optimal:
                            modes.append(i)
                            modesTime.append(i.calcTime(situation["distance"]))
                        fastest = min(modesTime)
                        index = modesTime.index(fastest)
                        optimal = modes[index]
                    json[name] = {
                        "optimal": optimal.name,
                        "rain": situation["rain"],
                        "snow": situation["snow"],
                        "wind": situation["wind"],
                        "other": situation["other"],
                        "distance": situation["distance"],
                        "time": optimal.calcTime(situation["distance"])
                    }
                    file.seek(0)
                    file.truncate()
                    file.write(j.dumps(json))
                    success = True
                    # Tries to write to file
                    # The saved journey is in this format:
                    # {
                    #   "journey name": {
                    #       "optimal": "optimal mode of transport",
                    #       "rain": "rain intensity",
                    #       "snow": "snow intensity",
                    #       "wind": "wind intensity",
                    #       "other": "other weather",
                    #       "distance": "distance",
                    #       "time": "time it takes for the optimal transport to travel the distance"
                    #   }
                except:  # If there is an error
                    print("Error in saving journey")
                    success = False  # Sets success to False
                if success:  # If the journey was saved successfully
                    print("Success!")

    # Now, the program will ask if the user wants to plan another journey
    # Asks if the user wants to plan another journey
    q7 = question("\nWould you like to plan another journey", ["y", "n"])
    ans = q7.ask()  # Gets answer
    if ans == "n":  # If the user does not want to plan another journey
        print("Have a good journey!")
        break  # Exits the journey planner
    else:
        print("\n\n")  # Three spaces
        continue  # Continues the journey planner

while True and action == "open":  # While the user wants to open a journey
    q1 = question(
        "Journey name('list' if forgotten, 'quit' to quit)", "string"
    )  # Asks for journey name
    ans = q1.ask()  # Gets answer
    if ans == "list":  # If the user wants to see a list of journeys
        a = 0  # Counter
        with open("./journey.json", "r") as file:  # Opens data file
            content = j.loads(file.read())  # Loads data
        for i in content:  # For each journey
            a += 1  # Adds one to counter
            print(str(a)+" - "+i)  # Prints journey name
    elif ans == "quit":  # If the user wants to quit
        print("Have a good journey!")
        break
    else:  # For all non command answers, it is assumed that the user wants to open a journey with that name
        with open("./journey.json", "r") as file:
            content = j.loads(file.read())
        conversionKeys = {
            "none": "no",
            "light": "light",
            "medium": "medium",
            "heavy": "heavy",
            "storm": "storm"
        }  # Converts the keys to a more readable format
        try:  # Tries to open journey
            content = content[ans]
        except:  # If there is an error
            # The most likely error is that the journey does not exist
            # Therefore we need to warn the user
            print(
                "Error when opening journey, does it exist? Try 'list' to see a list of saved journeys.")
            continue  # Continues to prevent the bottom code from running

        # Prints the journey situation
        toPrint = (content['optimal'] + " is the optimal transport.\n" +
                   "It will take "+str(content['time']) +
                   " to travel "+str(content['distance']) + " km.\n"
                   + "There is "+conversionKeys[content['rain']] + " rain.\n" +
                   "There is "+conversionKeys[content['snow']] + " snow.\n" +
                   "There is "+conversionKeys[content['wind']] + " wind.")
        if content['other'] != "none":  # If there is other weather
            toPrint += "\nIt is also " + \
                content['other'] + "."  # Adds other weather
        print(toPrint)
    print("")  # Prints a new line
