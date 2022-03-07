import random
def decide_winner(user_choice, computer_choice):
  if user_choice.lower() == "taş":
    user_choice = 0
  elif user_choice.lower() == "kağıt":
    user_choice = 1
  elif user_choice.lower() == "makas":
    user_choice = 2

  if (user_choice + computer_choice) % 2 == 1:
    return "user" if user_choice > computer_choice else "computer"
  elif(user_choice + computer_choice) % 2 == 0:
    return "user" if user_choice == 0 else "computer"

  
move_choice = input(f"Lütfen Taş, Kağıt veya Makastan birini seçiniz.\n")

computer_choice = random.randint(0, 2)
print(computer_choice)
str_com_choice = ""
if computer_choice == 0:
  str_com_choice = "Taş"
elif computer_choice == 1:
  str_com_choice = "Kağıt"
elif computer_choice == 2:
  str_com_choice = "Makas"
print(f"Comptuer's choice is {str_com_choice}")
print(decide_winner(move_choice, computer_choice))

