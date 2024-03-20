"""" Built a program for KBC game in which you would ask a ques to user and take
ans from them and then check with correct and and display with there winning amount and vice versa."""

questions=[[ "What is the capital of India?", "Mumbai", "Chennai", "Kolkata", "Delhi", 4],
           [ "What is the National game of India?", "Cricket", "Hockey", "Football", "Kabaddi", 2],
           [ "What is the Natinal bird of India?", "Parrot", "Owl", "Peacock", "Kingfisher", 3],
           [ "Who has won the first bharat ratna award in sports category?", "Sachin Tendulkar", "Kapil dev", "Sunil gavaskar", "Rahul dravid", 1],
           [ "What is the capital of India?", "Mumbai", "Chennai", "Kolkata", "Delhi", 4],
           [ "What is the National game of India?", "Cricket", "Hockey", "Football", "Kabaddi", 2],
           [ "What is the Natinal bird of India?", "Parrot", "Owl", "Peacock", "Kingfisher", 3],
           [ "Who has won the first bharat ratna award in sports category?", "Sachin Tendulkar", "Kapil dev", "Sunil gavaskar", "Rahul dravid", 1],
           [ "What is the capital of India?", "Mumbai", "Chennai", "Kolkata", "Delhi", 4],
           [ "What is the National game of India?", "Cricket", "Hockey", "Football", "Kabaddi", 2],
           [ "What is the Natinal bird of India?", "Parrot", "Owl", "Peacock", "Kingfisher", 3],
           [ "Who has won the first bharat ratna award in sports category?", "Sachin Tendulkar", "Kapil dev", "Sunil gavaskar", "Rahul dravid", 1]
]

Price= [1000, 2000, 5000, 10000, 20000, 40000, 60000, 120000, 240000, 360000, 720000, 1600000, 2500000, 5000000]

money=0
for i in range(0, len(questions)):
  question= questions[i]
  que= question[0]
  print(f"Question for Rs. {Price[i]} :-\n")
  print(que)
  print (f"a.{question[1]}       b.{question[2]}")
  print (f"c.{question[3]}       d.{question[4]}\n\n")
  ans= int(input("Enter your answer in (1-4) or 0 to quit"))
  if (ans == 0):
      money=Price[i-1]
      break
  if (ans == question[len(question)-1]):
      print("Congrats, Your answer is right.")
      if (i == 4):
          money=10000
      elif (i == 9):
          money= 320000
  else:
      print("Sorry, Your answer is wrong.")
      print("The Game has ended")
      break
  
print(f"you have won {money} Ruppee's")


