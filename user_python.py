# Get user's name
name = input("Hello! What's your name? ")

# Get user's age (convert input to integer)
age = int(input("How old are you, " + name + "? "))

# Get user's location
location = input("Where do you live, " + name + "? ")

# Print personalized message
print(f"Hello {name}, you are {age} years old and live in {location}.")