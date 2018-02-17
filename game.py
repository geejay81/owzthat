import random
import time

allOutWickets = 10 # can reduce this down for testing
gameRate = 0.25 # seconds between balls
balls = ["0", "1", "2", "3", "4", "6", "Owzthat!"]
decisions = ["Not Out!","Bowled!","Caught!","LBW!","Run Out!","Stumped!","Not Out!"]
noScoreToBeat = -1
team1 = "Sussex"
team2 = "Kent"

def returnToMark():
    time.sleep(gameRate)

def makeDecision():
    time.sleep(gameRate * 2)

def roll(dice):
    if (dice == "bowl"):
        return balls[random.randint(0,len(balls) - 1)]
    elif (dice == "decision"):
        makeDecision()
        return decisions[random.randint(0, len(decisions) - 1)]
    else:
        return "0"

def innings(scoreToBeat):
    wickets = 0
    score = 0
    bowled = 0

    while wickets < allOutWickets and (not score > scoreToBeat or scoreToBeat == noScoreToBeat):
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
        print("{} - {}/{} ({}.{} overs)".format(event,score,wickets,overs,unfinishedOverBalls))

        returnToMark()


    return { "Runs": score, "Wickets": wickets, "Overs": overs, "Balls": unfinishedOverBalls }

firstInnings = innings(noScoreToBeat)
print("{} score {}/{} in {}.{} overs".format(team1,firstInnings["Runs"],firstInnings["Wickets"],firstInnings["Overs"],firstInnings["Balls"]))
secondInnings = innings(firstInnings["Runs"])
print("{} score {}/{} in {}.{} overs".format(team2,secondInnings["Runs"],secondInnings["Wickets"],secondInnings["Overs"],secondInnings["Balls"]))

if (firstInnings["Runs"] > secondInnings["Runs"]):
    print("{} win by {} runs!".format(team1,firstInnings["Runs"] - secondInnings["Runs"]))
elif (firstInnings["Runs"] < secondInnings["Runs"]):
    print("{} win by {} wickets!".format(team2,10 - secondInnings["Wickets"]))
else:
    print("Tied game!")