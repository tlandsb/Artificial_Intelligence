## Small business AI program that assigns 'emotional' states to agents based on an event stream.
## Final project for 'CSC 594 - Topis in Artifical Intelligence', completed under the direction of Dr. Clark Elliot
## Spring 2021

import random
import time

## Content Theory Domain
print(" ")
print("****************************************")
print("Smalbizzz - Small Business AI Analyzer**")
print("**********By Trey Landsburg*************")
print("****************************************")
print(" ")

input("Welcome, Hit any key to begin")

print(" ")
print("****************************************")
print("**Goals, Standards and Preferences******")
print("****************************************")
print(" ")

# Goals
goals = ['Preservation: Keep small business afloat',
'Good relationships with other small businesses.',
'Staying competitive with large corporations',
'Operating in a lean and nimble manner',
'Increasing profits',
'Expanding into different markets',
'Expanding the existing product line',
'Increasing customers',
'Increasing existing market share',
'Healthy economies of their neighborhoods - ensuring vibrancy']
for i in goals:
    print("GOAL:", i)
print(' ')

time.sleep(1)

# Principles
principlesRight = ['Workers should always do what is best for the company',
'Management should see themselves as serving those that do the work, by getting them the resources they need',
'Small businesses care if their people are successful',
'The community in which a small business resides should be vibrant',
'Small businesses should help other small businesses']
for i in principlesRight:
    print("Principles (RIGHT):", i)
print(' ')
time.sleep(1)

principlesWrong = ['Employees should always have the goal of doing what is best for the group, and not have the primary goal of doing what makes them look good.',
'Big companies should put small businesses out out business',
'Companies should do whatever they want, without consideration of consequences',
'Greed is good',
'Money is more important than people',
'You should do whatever it takes to get ahead']
for i in principlesWrong:
    print("Principles (WRONG):", i)
print(' ')
time.sleep(1)

# Preferences
preferencesLike = [
'Attracting new customers',
'Increasing revenue',
'Increasing sales',
'Decreasing costs',
'Decreasing taxes',
'Increasing government subsidies',
'Component employees',
'Educated employees',
'Employee advancement']
for i in preferencesLike:
    print("Preferences (Like):", i)
print(' ')
time.sleep(1)

preferencesDislike = [
'Lost customers',
'Lost revenue',
'Decreased sales',
'Increased costs',
'Increased taxes',
'Decreased government subsidies',
'Incompotent employees']
for i in preferencesDislike:
    print("Preferences (Dislike):", i)
print(' ')
time.sleep(1)

objects = [
'Office/Cubicle -- as in some are more desirable than others. We can like some, but not others',
'Financial metrics - financial numbers above certain thresholds will lead to different business “emotional responses',
'Inventories',
'Sales',
'employees'
'Money',
'Government',
'Operations',
'Office equipment',
'Taxes',
'Vendors',
'Partners',
'Community leaders',
'Neighborhoods',
'Customers ',
'Investors']
for i in objects:
    print("Objects:", i)
print(' ')
time.sleep(1)

input("To continue - Hit any key")


##############################
###      **Events **       ###
##############################

print(" ")
print("****************************************")
print("****************Events******************")
print("****************************************")
print(" ")

# eventListRaw = ['profits increased', 'profits decreased', 'costs increased', 'costs decreased',
# 'customers increased', 'customers decreased', 'marketshare increased', 'marketshare decreased']
##eventList = [word for line in eventListRaw for word in line.split()] # List comprehension

# eventListRaw = ['Lost customers', 'Lost revenue', 'Decreased sales', 'Increased costs', 'Increased taxes',
# 'Decreased government subsidies', 'Incompotent employees']

eventListRawDictionary = [
{
  "event": "Increasing customers",
  "object": "Customers",
  "actor": "smallbusiness"
},
{
  "event": "Attracting new customers",
  "object": "Customers",
  "actor": "smallbusiness"
},
{
  "event": "Decreased government subsidies",
  "object": "Government",
  "actor": "smallbusiness"
},
{
  "event": "Small businesses should help other small businesses",
  "object": "employees",
  "actor": "smallbusiness"
}, 
{
  "event": "Increasing revenue",
  "object": "Sales",
  "actor": "smallbusiness"
}, 
{
  "event": "Decreased government subsidies",
  "object": "Government",
  "actor": "smallbusiness"
},
{
  "event": "Operating in a lean and nimble manner",
  "object": "operations",
  "actor": "smallbusiness"
},
{
  "event": "Lost customers",
  "object": "Customers",
  "actor": "smallbusiness"
}, 
{
  "event": "Increased taxes",
  "object": "Government",
  "actor": "smallbusiness"
}]

eventnumber = 0
for i in eventListRawDictionary:
    eventnumber += 1
    print("Event",eventnumber)
    print("event:", i["event"])
    print("object:", i["object"])
    print("actor:", i["actor"])
    print(' ')

input("To continue - Hit any key ")

# Intialize sentiment counters
negativeSentimentCounter = 0
positiveSentimentCounter = 0

print(' ')
actor = input("Choose actor for event appraisal: smallbusiness or bigbusiness - must be typed as shown: ")
print(actor, " chosen")
time.sleep(2)

print("APPRAISAL STARTING...")
time.sleep(1)
print("APPRAISAL STARTING...")
time.sleep(1)
print("APPRAISAL STARTING...")
time.sleep(1)
print(' ')

# Appraise each event and count the number of events that our relevant in the gsp list.
def appraiseEvent(eventListRawDictionary, gsps, actor):
    count = 0
    for event in eventListRawDictionary:
        print("**Appraising event: ** ",  event["event"])
        print("**Appraising object: ** ", event["object"])
        print("**Appraising actor: ** ",  event["actor"])
        for gsp in gsps:
            # print("**preference: ** ", preference)
            if (event["event"] == gsp and event["actor"] == actor.lower()):
                print("RELEVANCE DETECTED IN EVENT FRAME: ", event)
                count += 1
        print("Total relevant events: ", count, actor)
    return count

print("**Begin looking for achieved goals**")
print("**********************")
positiveSentimentCounter += appraiseEvent(eventListRawDictionary, goals, actor)
print("positiveSentimentCounter ", positiveSentimentCounter)
print(" ")

input("To continue - Hit any key")
print(' ')

print("**Begin looking for RIGHT princples**")
print("**********************")
positiveSentimentCounter += appraiseEvent(eventListRawDictionary, principlesRight, actor)
print("positiveSentimentCounter ", positiveSentimentCounter, actor)
print(" ")

input("To continue - Hit any key")

print("**Begin looking for WRONG princples**")
print("**********************")
negativeSentimentCounter += appraiseEvent(eventListRawDictionary, principlesWrong, actor)
print("positiveSentimentCounter ", negativeSentimentCounter, actor)
print(" ")

input("To continue - Hit any key")
print(' ')

print("**Begin looking for DISLIKED Preferences**")
print("**********************")
negativeSentimentCounter += appraiseEvent(eventListRawDictionary, preferencesDislike, actor)
print("negativeSentimentCounter ", negativeSentimentCounter, actor)
print(" ")

input("To continue - Hit any key")
print(' ')

print("**Begin looking for LIKED Preferences**")
print("**********************")
positiveSentimentCounter += appraiseEvent(eventListRawDictionary, preferencesLike, actor)
print("positiveSentimentCounter ", positiveSentimentCounter, actor)
print(" ")

input("To continue - Hit any key")
print(' ')

print("Overall favorability")
print("********************")

disposition = 0
if (positiveSentimentCounter > negativeSentimentCounter):
    print(actor," is happy with current event frames")
    print("Agent disposition will be set to +5")
    disposition = 5
elif (positiveSentimentCounter < negativeSentimentCounter):
    print(actor," is unhappy with current event frames")
    print("Agent disposition will be set to -5")
    disposition = -5
else:
    print(actor, " is neutral with current event frames")
    # disposition stays at 0
print(" ")

input("To continue - Hit any key")
print(' ')

##############################
### ** Appraisal Agents ** ###
##############################

## Emotionally Intelligent Agent - Goal Appraisal
## When percentage of achieved is above 50%.. return True  for goal/standard/preference achieved. 
## When percentage of achieved is below 50%.. return False for goal/standard/preference not achieved
def EIAInterpreterIsGoalAchieved(goals):
    if goals >  50:
        return True
    else:
        return False

## Emotionally Intelligent Agent - Standard Appraisal
def EIAInterpreterIsStandardAchieved(standards):
    if standards > 50:
        return True
    else:
        return False

## Emotionally Intelligent Agent - Preference Appraisal
def EIAInterpreterIsPreferenceAchieved(preferences):
    if preferences >  50:
        return True
    else:
        return False


#Build out a list of simulated frames. Each agent GSPs are assigned random integer values between
#1 and 100 to denote what percentage of a goal standard or preference has been met.
frames = list()
class FrameBuilder:
    def __init__(self, agent, goal, standard, preference, emotionalAppraisal):
        self.agent = agent
        self.goal = goal   
        self.standard = standard
        self.preference = preference
        self.emotionalAppraisal = emotionalAppraisal

#Get Agent Number
agentNumber = input("Enter Number of Agents to Generate ")
agentNumber = int(agentNumber)
print("Generating ",agentNumber, "agents", "with a disposition of", disposition)       

print("GENERATING AGENTS...")
time.sleep(1)
print("GENERATING AGENTS...")
time.sleep(1)
print("GENERATING AGENTS...")
time.sleep(1)
print(' ')

#Populate the agents percentages with simulated random ints
for i in range(agentNumber):
    agent = i
    goal = random.randint(1,100) + disposition 
    standard = random.randint(1,100) + disposition
    preference = random.randint(1,100) + disposition

    frames.append(FrameBuilder(agent, goal, standard, preference, ''))
    # print("frame: ", i, "EIAInterpreterIsGoal:", getattr(frames[i], "EIAInterpreterIsGoal"),
    #               "EIAInterpreterIsStandard:", getattr(frames[i], "EIAInterpreterIsStandard"),
    #               "EIAInterpreterIsPreference:", getattr(frames[i], "EIAInterpreterIsPreference"),
    #               "EmotionalAppraisal:", getattr(frames[i], "EmotionalAppraisal"))

#Appraisals - Goal Achieved:
#If all Goals, Standards and Preferences Achieved - Happy
#If all Goals, Standards and Preferences Not Achieved - Unhappy
#If some Goals, Standards and Preferences Not Achieved - Neutral
for frame in frames:
    if (EIAInterpreterIsGoalAchieved(frame.goal) == True) and (EIAInterpreterIsStandardAchieved(frame.goal) == True) and (EIAInterpreterIsPreferenceAchieved(frame.goal) == True):
        frame.EmotionalAppraisal = 'Favorable'
    elif (EIAInterpreterIsGoalAchieved(frame.goal) == False) and (EIAInterpreterIsStandardAchieved(frame.goal) == False) and (EIAInterpreterIsPreferenceAchieved(frame.goal) == False):
        frame.EmotionalAppraisal = 'Unfavorable'
    else:
        frame.EmotionalAppraisal = 'Neutral'

#Print outcomes for each agent
countFavorable = 0
countUnfavorable = 0
for frame in frames:
    if (frame.EmotionalAppraisal == 'Favorable'):
        countFavorable +=1
    elif (frame.EmotionalAppraisal == 'Unfavorable'):
        countUnfavorable +=1
    print("agent #:", frame.agent, "outcome:", frame.EmotionalAppraisal)
print("Favorable Agent Count: ",countFavorable)
print("Unfavorable Agent Count",countUnfavorable)


