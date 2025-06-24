import random
print("You are about to view the scorecard for your team's most recent match")

def generate_batting_scorecard():
    print("BATTING SCORECARD")
    player_number = 0
    batting_scorecard = []
    print("Player Number, Runs scored, Balls faced")
    for i in range(0,6):
        player_number += 1
        player_runs = random.randint(5,50)
        player_balls = random.randint(10,30)
        batting_scorecard.append([player_number,player_runs,player_balls])
    return batting_scorecard
    
batting_scorecard = generate_batting_scorecard()
print(batting_scorecard)

def generate_bowling_scorecard():
    print("BOWLING SCORECARD")
    player_numero = 6
    bowling_scorecard = []
    print("Player Number, Overs Bowled, Runs Given, Wickets Taken")
    for i in range(0,5):
        player_numero += 1
        player_overs = random.randint(2,8)
        player_runs_given = random.randint(5,27)
        player_wickets = random.randint(0,5)
        bowling_scorecard.append([player_numero,player_overs,player_runs_given,player_wickets])
    return bowling_scorecard

bowling_scorecard = generate_bowling_scorecard()
print(bowling_scorecard)

def list_top_three_runs_scorers(batting_scorecard):
    top_run_scorers = []
    
    for i in range(0,len(batting_scorecard)):
        player_batting_stats = batting_scorecard[i]
        
    


top_three_runs = list_top_three_runs_scorers(batting_scorecard)
print(top_three_runs)


  





 



    














        
    




    