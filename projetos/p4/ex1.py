import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇



itens = [rock,paper,scissors ,["Rock","Paper","Scissors"]]
opcao_usuario = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
opcao_ai = random.randint(0,2)

print(f"""O usuario escolheu {itens[3][opcao_usuario]}\n{itens[opcao_usuario]} \n
 O computador escolheu {itens[3][opcao_ai]}\n {itens[opcao_ai]}""")

if opcao_usuario == opcao_ai:
    print("draw")
else:
    if opcao_usuario == 0 and opcao_ai == 1:
        print("Computer wins!")
    elif opcao_usuario == 0 and opcao_ai == 2:
        print("usuario wins!")
    elif opcao_usuario == 1 and opcao_ai == 0:
        print("usuario wins!")
    elif opcao_usuario == 1 and opcao_ai == 2:
        print("Computer wins!")
    elif opcao_usuario == 2 and opcao_ai == 0:
        print("Computer wins!")
    elif opcao_usuario == 2 and opcao_ai == 1:
        print("Usuario wins!")

