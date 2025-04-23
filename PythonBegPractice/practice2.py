#building a robot barista
print("Hello welcome to network chuck coffee!!!!!!!!!!!!!!!")

name = input("What is your name?: \n")

if name in ["Ben", "Patricia", "Loki"]:
  evil_status = input("Are you evil?\n")
  good_deeds = int(input("How many good deeds have you done today?:\n"))
  if evil_status == "Yes" and good_deeds < 4:
    print(f"You're not welcome here evil {name} GET OUT!!")
    exit()
  else:
    print(f"Thank you for not being an Evil {name} you can never be too sure!")
else:
  print(f"Hello {name},Thank you for coming in today!")


#Prints name and thanks you for coming

menu = " Mocha $8\n Espresso $10\n Latte $8\n Cappucino $8\n French Vanilla $9\n Frappucino $13\n Black Coffee $6" 



print(f"We have a wide variety of coffee available " + {name} + "\nHere is our menu: \n" + {menu})

mychoice = input("What would you like?: \n")

if mychoice == "Frappucino":
  price = 13
elif mychoice == "Mocha":
  price = 8
elif mychoice == "Espresso":
  price = 10
elif mychoice == "Latte":
  price = 8
  whipped_cream = input("Would you like whipped cream with that?: ")
  if whipped_cream == "yes":
    price = 10
elif mychoice == "Cappucino":
  price = 8
elif mychoice == "Black Coffee":
  price = 6
elif mychoice == "French Vanilla":
  price = 9
else:
  print("Sorry we dont serve that here.")
  exit()

number_of_coffees = input("How many would you like?: \n")

calculate_total = price * int(number_of_coffees)

print(f"Youre total today is: ${str(calculate_total)}")

print(f"Thank you {name} your {number_of_coffees} {mychoice}" +
      " will be ready momentarily!")









