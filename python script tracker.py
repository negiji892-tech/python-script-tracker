# Task 1 : details and welcome message 
# Project: Daily calorie tracker 
# Name: Ankur Singh Negi 
# date: 20-10-2025
# A simple program to track meal and calories
# -------------------------------------------
print("welcome to daily calories tracker!")
print("this program helps you record your meals and calories")

# Task 2 : Input & Data Collection

meal = [ ]
calorie = [ ]

num_meals = int(input("how many meals did you have today?"))

for i in range(num_meals):
    print(f"\nEnter details for meals{i + 1}:")
    meal_name = input("Meal name: ")
    meal_caloris = float(input("calories (kcal):"))

    meal.append(meal_name)
    calorie.append(meal_caloris)
    
# Task 3 : calories calculations 
Total_calories = sum(calorie)
avg_calories = Total_calories/len(calorie) 
daily_limit = float(input("\nWhat is your daily calorie limit?"))


# Task 4 : Exceed limit waring system 
if Total_calories > daily_limit:
    print("waring: you have gone over your daily limit!")
else:
    print("Good job! you are within your daily limit.")


# Task 5 : Display summary 
print("\n------DAILY CALORIE SUMMARY------") 
print("meal name\tcalories")
print("-----------------------------------")
for i in range(len(meal)):
    print(f"{meal[i]}\t\t{calorie[i]}")

print("----------------------------------")    
print(f"Total calories:{Total_calories}")
print(f"average calories per meal: {avg_calories:.2f}")
print(f"status: {message}")
print("----------------------------------")
