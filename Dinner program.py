dinner_one_setup = "\nPlease take out the following items for prep \n\n1. 2 Baking sheets \n2. Cutting board \n3. Knife \n4. Onion \n5. Big bowl for potatoes \n6. Skinner \n7. Collander \n8. Potatoes \n9. Black skillet \n10. Medium bowl \n11. Chicken \n12. Two plates \n13. Two forks \n14. My lunch dish \n15. Max's dog bowl"
dinner_one_instruction = "\n\nCooking instructions \n\n1. Preheat grill and oven (375) \n2. Wash asparagus and prepare \n3. Prepare mac and cheese \n4. Put chicken on grill 1x14m \n5. Place mac and cheese in oven for 35m \n6. Put asparagus in oven for 8m \n7. Flip chicken"
dinner_one = "1. Chicken, mac and cheese, and asparagus"
dinner_two = "2. Chicken, roasted potatoes and carrots, broccoli"
dinner_two_instructions = "\n\nCooking instructions \n\n1. Preheat grill and oven \n2. Wash potatoes, broccoli, and carrots \n3. Put chicken on grill for 14m \n4. Chop potatoes and carrots. Place on pan and cook once oven is preheated \n5. Chop broccoli, season, and place on baking sheet. Cook for 15m \n6."
dinner_three = "3. Chicken, pasta, and roasted brussel sprouts"

# First line when opening
print("Hello and welcome to Skynet. Please choose from the following options. \n 1. Chicken, asparagus, mac and cheese 2. Chicken, broccoli, pasta")

if input() == "1":
    input(print("Lets begin! Hit enter when ready"))
    print(dinner_one_instruction)

if input() == "2":
    input(print("Lets begin! Hit enter when ready"))
    print(dinner_two_instructions)


# Print dinner one prep list

print(dinner_one_setup)
input(print("Hit enter when ready"))

print(dinner_one_instruction)
input(print("Hit enter when ready"))

print("Clean up and eat!")
