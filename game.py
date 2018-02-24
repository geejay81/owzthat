import random
import time

# game contstants
noRunsRequired = -1
unlimitedOvers = -1
allOutWickets = 10 # can reduce this down for testing
balls = ["0", "1", "2", "3", "4", "6", "Owzthat!"]
decisions = ["Not Out!","Bowled!","Caught!","LBW!","Run Out!","Stumped!","Not Out!"]

# match variables
team1 = "Sussex"
team2 = "Kent"
oversPerTeam = unlimitedOvers
gameRate = 0.25 # seconds between balls

def returnToMark():
    """ Function call to simulate the time taken 
        for the bowler to return to their mark """
            
    time.sleep(gameRate)

def makeDecision():
    """ Function call to simulate the time taken 
        for the umpire to make a decision and add tension to the game """

    time.sleep(gameRate * 2)

def roll(dice):
    """ Function call to simulate either the roll of a dice
        for either the bowl of a ball or an appeal decision """

    if (dice == "bowl"):
        return balls[random.randint(0,len(balls) - 1)]
    elif (dice == "decision"):
        makeDecision()
        return decisions[random.randint(0, len(decisions) - 1)]
    else:
        return "0"

def innings(battingTeam,maxOvers,runsRequired):
    """ Function call to simulate a single innings """

    wickets = 0
    score = 0
    bowled = 0
    overs = 0
    unfinishedOverBalls = 0

    while wickets < allOutWickets and \
        (not score > runsRequired or runsRequired == noRunsRequired) and \
        (overs < maxOvers or maxOvers == unlimitedOvers):
        ball = roll("bowl")
        event = ""
        if (ball == "Owzthat!"):
            print(ball)
            decision = roll("decision")
            event = decision
            if (decision != "Not Out!"):
                wickets = wickets + 1
        else:
            event = "{} run".format(ball)
            if (ball != "1"):
                event = event + "s"

            score = score + int(ball)
            
        bowled = bowled + 1
        unfinishedOverBalls = int(bowled % 6)
        overs = int((bowled - unfinishedOverBalls) / 6)
        print("{} - {} {}/{} ({}.{} overs)".format(event,battingTeam,score,wickets,overs,unfinishedOverBalls))

        returnToMark()


    return { "Runs": score, "Wickets": wickets, "Overs": overs, "Balls": unfinishedOverBalls }

firstInnings = innings(team1,oversPerTeam,noRunsRequired)
print("{} score {}/{} in {}.{} overs".format(team1,firstInnings["Runs"],firstInnings["Wickets"],firstInnings["Overs"],firstInnings["Balls"]))
secondInnings = innings(team2,oversPerTeam,firstInnings["Runs"])
print("{} score {}/{} in {}.{} overs".format(team2,secondInnings["Runs"],secondInnings["Wickets"],secondInnings["Overs"],secondInnings["Balls"]))

if (firstInnings["Runs"] > secondInnings["Runs"]):
    print("{} win by {} runs!".format(team1,firstInnings["Runs"] - secondInnings["Runs"]))
elif (firstInnings["Runs"] < secondInnings["Runs"]):
    print("{} win by {} wickets!".format(team2,10 - secondInnings["Wickets"]))
else:
    print("Tied game!")
