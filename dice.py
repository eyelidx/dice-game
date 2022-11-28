import random
import os 
sPlay = "y"

while(sPlay == "y"):
  player1 = "null"
  player2 = "null"
  score1 = 0
  score2 = 0
  rollnum = 0
  rollnum2 = 0
  temptotal = 0
  roundnum = 1

  player1 = input("Please enter the name of player 1")
  player2 = input("Please enter the name of player 2")

  while (roundnum < 6):
    print ("Round" +str(roundnum) + "!\n\n")
    roll1 = str(input(player1 + str(", type roll to roll the dice")))
    rollnum = random.randrange (2,12)
    if (roll1 == "roll"):
      print("You rolled a total of" + " " + str(rollnum))
    temptotal = (rollnum)
    score1 = (score1 + temptotal)
    roll2 = str(input(player2 + str(", type roll to roll the dice")))
    rollnum2 = random.randrange (2,12)
    if (roll2 == "roll"):
      print("You rolled a total of" + " " + str(rollnum2))
    temptotal = (rollnum2)
    score2 = (score2 + temptotal)
    print(player1 + str("\'s score is") + " " + str(score1) + ","+ player2 + str("\'s score is") + " " + str(score2))
    roundnum = roundnum + 1
    print("n/Next round is round " + str(roundnum) + ", " + player1 + " has " + str(score1) + " points and " + player2 + 
  " has " + str(score2) + " points.")

    input("Press enter to start the next round")
    os.system('cls')
  else:
    print("After 5 rounds, the scores are:\n\n" + player1 + " has " + str(score1) + " points, and " + player2 + " has " + str(score2) + " points")
  if (score1 == score2):
    print("As you both have the same number of points, there will be a tie breaker round.")
    while (score1 == score2):
      print("Bonus round\n\n")
      roll1 = str(input(player1 + str(", type roll to roll the dice")))
      rollnum = random.randrange (2,12)
      if (roll1 == "roll"):
        print("You rolled a total of" + " " + str(rollnum))
      temptotal = (rollnum)
      score1 = (score1 + temptotal)
      roll2 = str(input(player2 + str(", type roll to roll the dice")))
      rollnum2 = random.randrange (2,12)
      if (roll2 == "roll"):
        print("You rolled a total of" + " " + str(rollnum2))
      temptotal = (rollnum2)
      score2 = (score2 + temptotal)
      print("The final scores are:" + player1 + str("\s score is") + " " + str(score1) + "," + player2 + str("\'s score is") + " " + str(score2))
  elif(score1 > score2):
    print(player1 + str(" wins the game! Congrats."))
  elif(score1 < score2):
    print(player2 + str(" wins the game! Congrats"))
      


 
