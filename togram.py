#convert baking ingredients from cups/ounces to metric

print("What ingredient would you like to convert?")
ingredient = input('Enter ingredient: ')
print("C for cups, S for tablespoon")
unit = input("Enter measuring unit: ")
amount = int(input("Enter amount: "))

volume_dict = {
# cm3
	"C" : 236.588,
	"S" : 14.7868
}

ingredient_density_dict = {
# in g/cm3
  "butter": 0.911,
  "brown sugar": 0.93,
  "white sugar": 1.59
}

converted = volume_dict[unit] * amount * ingredient_density_dict[ingredient] 

result = "{0} {1} of {2} is {3} grams "
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(result.format(amount, unit, ingredient, converted))