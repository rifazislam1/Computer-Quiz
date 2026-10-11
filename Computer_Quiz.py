invite = input("Can you want to play Computer Quiz Game?")
if invite.lower() == 'yes':
  print("Let's Play Computer Quiz Game!")
else:
  quit()
score = 0
answers = input("Who is the inventor of python? ")
if answers.lower() == 'guido van rossum':
  print('Correct answer!')
  score+=1
else:
  print('Incorrect Answer!')
answers = input("What is the capital of India ? ")
if answers.lower() == 'delhi':
  print('Correct answer!')
  score+=1
else:
  print('Incorrect Answer!')
answers = input("Who is the prime minister of India? ")
if answers.lower() == 'narendra modi':
  print('Correct answer!')
  score+=1
else:
  print('Incorrect Answer!')
answers = input("What is the full form of CPU? ")
if answers.lower() == 'central processing unit':
  print('Correct answer!')
  score+=1
else:
  print('Incorrect Answer!')
print(f'You got {score} answers correct.')
