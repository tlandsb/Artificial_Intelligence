## Starter code provided by Christian Stigen Larsen of the University of Stavanger, Norway (who placed this in the public domain).
## Modified and implemented by Trey Landsburg for his CSC 594 class animal.py program.

# Libraries
import sys
import random

# Take the user input and add the appropriate indefinite article
def definiteNoun(s):
  "Add definite form to a noune, for instance 'whale' becomes 'a whale'"
  s = s.lower().strip()
  if s in ['a', 'e', 'i', 'o', 'u', 'y']:
    return "an " + s
  else:
    return "a " + s

# Take the user input and remove the appropriate indefinite article
def removeArticle(s):
  "Remove the definite article 'a' or 'an' from a noun."
  s = s.lower().strip()
  if s[0:3] == "an ": return s[3:]
  if s[0:2] == "a ": return s[2:]
  return s

# Take question and yes answer and no answer, put them in an array
def makeQuestion(question, yes, no):
  return [question, yes, no]

# Return a boolean value if the answer is a list or not
def isQuestion(p):
  "Check if node is a question (with answers), or a plain answer."
  return type(p).__name__ == "list"

# Get the user's answer to the question from the standard input
def askQuestion(question):
  print ("\r%s " % question),
  return sys.stdin.readline().strip().lower()

# If its a question, return the first element which is the question, otherwise ask the question
def getAnswer(question):
  if isQuestion(question):
    return askQuestion(question[0])
  else:
    return askQuestion("Were you thinking about %s?" % definiteNoun(question))

# If the user answered yes return a y, otherwise return false
def answeredYes(answer):
  if len(answer) > 0:
    return answer.lower()[0] == "y"
  return False

def gameOver(message):
  global tries
  print ("")
  print ("\r%s" % message)
  print ("I used", tries, "questions!")
  print ("")

def playAgain():
  return answeredYes(askQuestion("Do you want to play again?"))

def correctGuess(message):
  global tries
  gameOver(message)

  if playAgain():
    print ("")
    tries = 0
    return Q
  else:
    sys.exit(0)

# personality selection functions, generate a random int and return the response associated with that index
def makeDepressedPersonality():
    randomInt = random.randint(0, 2)
    winResponse = ["I'm so bad", "I won, but I shoudln't have","I just got lucky.. I'm not very smart,", "I got it, but this is the only skill I have"]
    return winResponse[randomInt]

def makeManicPersonality():
    randomInt = random.randint(0, 2)
    winResponse = ["Im so great!", "I am so amazing!", "You cant do anything better than me!", "Hahaha, I cant believe how smart I am!"]
    return winResponse[randomInt]

def makeSeriousPersonality():
    randomInt = random.randint(0, 2)
    winResponse = ["OK, I got it right, but lets get on with it", "I got it right, but there is so much more to do",
     "I got this question right, but I should be studying for the next question", "I got this right, but I need to be something more with my life"]
    return winResponse[randomInt]
  
# Set personality based on the users selection 
def choosePersonality(personality):
  print("personality ",personality )
  if personality == "depressed":
    return makeDepressedPersonality()
  elif personality =="manic":
    return makeManicPersonality()
  elif personality =="serious":
    return makeSeriousPersonality()

 
def nextQuestion(question, answer):
  global tries
  tries += 1

  if isQuestion(question):
    if answer:
      return question[1]
    else:
      return question[2]
  else:
    if answer:
      return correctGuess(choosePersonality(personality))
    else:
      return makeNewQuestion(question)



def replaceAnswer(tree, find, replace):
  if not isQuestion(tree):
    if tree == find:
      return replace
    else:
      return tree
  else:
    return makeQuestion(tree[0],
      replaceAnswer(tree[1], find, replace),
      replaceAnswer(tree[2], find, replace))

def makeNewQuestion(wrongAnimal):
  global Q, tries

  correctAnimal = removeArticle(askQuestion("I give up.  What did you think about?"))

  newQuestion = askQuestion("Enter a question that would distinguish %s from %s:"
      % (definiteNoun(correctAnimal), definiteNoun(wrongAnimal))).capitalize()

  yesAnswer = answeredYes(askQuestion("If I asked you this question " +
    "and you thought about %s, what would the correct answer be?" % definiteNoun(correctAnimal)))

  # Create new question node
  if yesAnswer:
    q = makeQuestion(newQuestion, correctAnimal, wrongAnimal)
  else:
    q = makeQuestion(newQuestion, wrongAnimal, correctAnimal)

  # Create new question tree and start over again
  Q = replaceAnswer(Q, wrongAnimal, q)
  tries = 0 # reset since we'll play again
  return Q

tries = 0
Q = (makeQuestion('Can it fly?', 'pelican', 'whale'))
q = Q

print ("Imagine an animal.  I will try to guess which one.")
print ("Please only answer YES or NO.")
print ("")

#Get personality from the user
print ("First, tell me the desired personality: (depressed, manic or serious) ")

Done = False
while not Done:
  personality = sys.stdin.readline().strip().lower()
  if personality == 'manic' or personality == 'depressed' or personality == 'serious':
    print("[~",personality, "personality activated~]")
    Done = True
  else:
    print("thats not a personality, please enter either depressed, manic or serious")


while True:
         ans = answeredYes(getAnswer(q))
         q = nextQuestion(q, ans)

