gender = input("Are you a (m)an or (w)oman? ")  # Prompt the user to enter their gender

if gender.lower() == "m":  # Check if the user is a man
    try:
        weight = float(input("How much do you weigh (LBS)? "))  # Prompt the user to enter their weight
        age = float(input("How old are you? "))  # Prompt the user to enter their age
        height = float(input("How tall are you in inches? "))  # Prompt the user to enter their height
        
        BMR_MEN = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)  # Calculate the Basal Metabolic Rate for men
        
        activity_level = input("How active are you? Choose one of the following options:"
                               "\n(S)edentary (little to no exercise)"
                               "\n(L)ightly active (light exercise/sports 1-3 days a week)"
                               "\n(M)oderately active (moderate exercise/sports 3-5 days a week)"
                               "\n(V)ery active (hard exercise/sports 6-7 days a week)\n")  # Prompt the user to enter their activity level
        
        if activity_level.upper() == "S":
            print(BMR_MEN * 1.2)  # Calculate and print the calorie intake based on sedentary activity level
        elif activity_level.upper() == "L":
            print(BMR_MEN * 1.375)  # Calculate and print the calorie intake based on lightly active activity level
        elif activity_level.upper() == "M":
            print(BMR_MEN * 1.55)  # Calculate and print the calorie intake based on moderately active activity level
        elif activity_level.upper() == "V":
            print(BMR_MEN * 1.725)  # Calculate and print the calorie intake based on very active activity level
        else:
            print("Invalid input")  # Print an error message for invalid activity level inputs
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")  # Print an error message for invalid numeric inputs
    
elif gender.lower() == "w":  # Check if the user is a woman
    try:
        weight = float(input("How much do you weigh (LBS)? "))  # Prompt the user to enter their weight
        age = float(input("How old are you? "))  # Prompt the user to enter their age
        height = float(input("How tall are you in inches? "))  # Prompt the user to enter their height
        
        BMR_WOMEN = 665 + (4.35 * weight) + (4.7 * height) - (4.7 * age)  # Calculate the Basal Metabolic Rate for women
        
        activity_level = input("How active are you? Choose one of the following options:"
                               "\n(S)edentary (little to no exercise)"
                               "\n(L)ightly active (light exercise/sports 1-3 days a week)"
                               "\n(M)oderately active (moderate exercise/sports 3-5 days a week)"
                               "\n(V)ery active (hard exercise/sports 6-7 days a week)\n")  # Prompt the user to enter their activity level
        
        if activity_level.upper() == "S":
            print(BMR_WOMEN * 1.2)  # Calculate and print the calorie intake based on sedentary activity level
        elif activity_level.upper() == "L":
            print(BMR_WOMEN * 1.375)  # Calculate and print the calorie intake based on lightly active activity level
        elif activity_level.upper() == "M":
            print(BMR_WOMEN * 1.55)  # Calculate and print the calorie intake based on moderately active activity level
        elif activity_level.upper() == "V":
            print(BMR_WOMEN * 1.725)  # Calculate and print the calorie intake based on very active activity level
        else:
            print("Invalid input")  # Print an error message for invalid activity level inputs
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")  # Print an error message for invalid numeric inputs

else:
    print("This input is invalid.")  # Print an error message for invalid gender inputs
