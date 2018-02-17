import random
import time

allOutWickets = 10 # can reduce this down for testing
gameRate = 1 # seconds between balls
balls = ["0", "1", "2", "3", "4", "6", "Owzthat!"]
decisions = ["Not Out!","Bowled!","Caught!","LBW!","Run Out!","Stumped!","Not Out!"]

def returnToMark():
    time.sleep(gameRate)

def makeDecision():
    time.sleep(gameRate * 5)

def roll(dice):
    if (dice == "bowl"):
        return balls[random.randint(0,len(balls) - 1)]
    elif (dice == "decision"):
        makeDecision()
        return decisions[random.randint(0, len(decisions) - 1)]
    else:
        return "0"

def innings():
    wickets = 0
    score = 0

    while wickets < allOutWickets:
        ball = roll("bowl")
        print(ball)
        if (ball == "Owzthat!"):
            decision = roll("decision")
            print(decision)
            if (decision != "Not Out!"):
                wickets = wickets + 1
        else:
            score = score + int(ball)
            
        print("{}/{}".format(score,wickets))
        
        returnToMark()

    print("Innings over!")

innings()