"""
Challenge Project #1 Personality Test

What type of weather are you?
"""

# Functions for each question
def question_one():
  print("1. How would you describe your personality?")
  print()
  print("1) Bright and sunny") 
  print("2) Warm and cozy") 
  print("3) Moody and mysterious")
  print("4) Refreshing and cleansing")

def question_two():
  print("2. What is your ideal vacation destination?")
  print()
  print("1) A tropical beach") 
  print("2) A cabin in the woods") 
  print("3) A haunted castle") 
  print("4) A mountain retreat")
  
def question_three():
  print("3. How do you like to spend your free time?")
  print()
  print("1) Playing sports")
  print("2) Reading a book by the fireplace")
  print("3) Watching a horror movie")
  print("4) Going for a hike")

def question_four():
  print("4. What is your favorite color?")
  print()
  print("1) Yellow")
  print("2) Red")
  print("3) Black")
  print("4) Green")

def question_five():
  print("What is your ideal job?")
  print()
  print("1) Lifeguard") 
  print("2) Movie theatre employee")
  print("3) Blogger") 
  print("4) Barista")


# Function that prints result of quiz
def print_result():
  if sunny_day_score > cozy_night_score and sunny_day_score > stormy_night_score and sunny_day_score > fresh_morning_score:
    print("You are a sunny day! You're cheerful and optimistic, and you brighten up everyone's day.")
    print()
  elif cozy_night_score > sunny_day_score and cozy_night_score > stormy_night_score and cozy_night_score > fresh_morning_score:
    print("You are a cozy night! You're warm and inviting, and you make people feel comfortable and at home.")
    print()
  elif stormy_night_score > sunny_day_score and stormy_night_score > cozy_night_score and stormy_night_score > fresh_morning_score:
    print("You are a stormy night! You're moody and mysterious, and people are drawn to your intense energy.")
    print()
  elif fresh_morning_score > sunny_day_score and fresh_morning_score > cozy_night_score and fresh_morning_score > stormy_night_score:
    print("You are a fresh morning! You're invigorating and refreshing, and you help people start their day on a positive note.")
    print()
  
  
# Function that prints a double result (if there is a draw)  
def print_double_result():
  if sunny_day_score == 2 and cozy_night_score == 2:
    print("You are both, a sunny day and a cozy night! You're cheerful and optimistic, and you brighten up everyone's day. Also, you're a warm and inviting, and you make people feel comfortable and at home.")
    print()
  elif sunny_day_score == 2 and stormy_night_score == 2:
    print("You are both, a sunny day and a stormy night! You're cheerful and optimistic, and you brighten up everyone's day. Also, you're moody and mysterious, and people are drawn to your intense energy.")
    print()
  elif sunny_day_score == 2 and fresh_morning_score == 2:
    print("You are both, a sunny day and a fresh morning! You're cheerful and optimistic, and you brighten up everyone's day. Also, you're invigorating and refreshing, and you help people start their day on a positive note.")
    print()
  elif cozy_night_score == 2 and stormy_night_score == 2:
    print("You are both, a cozy night and a stormy night! You're warm and inviting, and you make people feel comfortable and at home. Also, you're moody and mysterious, and people are drawn to your intense energy.")
    print()
  elif cozy_night_score == 2 and fresh_morning_score == 2:
    print("You are both, a cozy night and a stormy night! You're warm and inviting, and you make people feel comfortable and at home. Also, you're invigorating and refreshing, and you help people start their day on a positive note.")
    print()
  elif stormy_night_score == 2 and fresh_morning_score == 2:
    print("You are both, a stormy night and a fresh morning! You're moody and mysterious, and people are drawn to your intense energy. Also, you're invigorating and refreshing, and you help people start their day on a positive note.")
    print()
 


### Main


# Print welcome statement
print()
print("What type of weather are you??? Answer the following questions to find out.")
print()

# Initialize variables to keep track of the user's answers
sunny_day_score = 0
cozy_night_score = 0
stormy_night_score = 0
fresh_morning_score = 0


# print question 1
question_one()
# Read the answer and assign a point to its associated outcome
answer1 = int(input("Enter your answer: "))
print()
if answer1 == 1:
  sunny_day_score += 1
elif answer1 == 2:
  cozy_night_score += 1
elif answer1 == 3:
  stormy_night_score += 1
elif answer1 == 4:
  fresh_morning_score += 1


# print question 2
question_two()
# Read the answer and assign a point to its associated outcome
answer2 = int(input("Enter your answer: "))
print()
if answer2 == 1:
  sunny_day_score += 1
elif answer2 == 2:
  cozy_night_score += 1
elif answer2 == 3:
  stormy_night_score += 1
elif answer2 == 4:
  fresh_morning_score += 1


# print question 3
question_three()
# Read the answer and assign a point to its associated outcome
answer3 = int(input("Enter your answer: "))
print()
if answer3 == 1:
  sunny_day_score += 1
elif answer3 == 2:
  cozy_night_score += 1
elif answer3 == 3:
  stormy_night_score += 1
elif answer3 == 4:
  fresh_morning_score += 1


# print question 4
question_four()
# Read the answer and assign a point to its associated outcome
answer4 = int(input("Enter your answer: "))
print()
if answer4 == 1:
  sunny_day_score += 1
elif answer4 == 2:
  cozy_night_score += 1
elif answer4 == 3:
  stormy_night_score += 1
elif answer4 == 4:
  fresh_morning_score += 1


# print question 5
question_five()
# Read the answer and assign a point to its associated outcome
answer5 = int(input("Enter your answer: "))
print()
if answer5 == 1:
  sunny_day_score += 1
elif answer5 == 2:
  cozy_night_score += 1
elif answer5 == 3:
  stormy_night_score += 1
elif answer5 == 4:
  fresh_morning_score += 1

  
# Determine the user's weather type based on their answers
print_result()
print_double_result()