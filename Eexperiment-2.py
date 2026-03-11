for i in range(3):
    print("\nEnter the player detail:", i+1)

    name = input("Enter the player name: ")
    runs = int(input("Enter the number of runs: "))
    balls = int(input("Enter the number of balls: "))
    wickets = int(input("Enter the number of wickets: "))
    runs_conceded = int(input("Enter the runs conceded: "))
    overs = int(input("Enter the remaining overs: "))
    catches = int(input("Enter the number of catches: "))

    strike_rate = (runs / balls) * 100
    economy = runs_conceded / overs

    # Batter decision
    if runs >= 50 and strike_rate >= 120:
        batter = "Excellent batter"
    elif runs >= 30 and strike_rate >= 100:
        batter = "Good batter"
    elif runs >= 20:
        batter = "Average batter"
    else:
        batter = "Poor batter"

    # Bowler decision
    if wickets >= 3 and economy <= 6:
        bowler = "Excellent bowler"
    elif wickets >= 2 and economy <= 8:
        bowler = "Good bowler"
    elif wickets >= 1:
        bowler = "Average bowler"
    else:
        bowler = "Poor bowler"

    # Fielder decision
    if catches >= 2:
        fielder = "Outstanding fielder"
    elif catches == 1:
        fielder = "Active fielder"
    else:
        fielder = "Need improvement"

    # All-rounder decision
    if batter == "Excellent batter" and bowler == "Excellent bowler":
        all_rounder = "Star all rounder"
    elif batter == "Good batter" and bowler == "Good bowler":
        all_rounder = "Strong all rounder"
    elif batter == "Good batter" or bowler == "Good bowler":
        all_rounder = "Supporting all rounder"
    else:
        all_rounder = "Need improvement"

    print("Player name =", name)
    print("Strike rate =", strike_rate)
    print("Economy =", economy)
    print("Batter =", batter)
    print("Bowler =", bowler)
    print("Fielder =", fielder)
    print("All rounder decision =", all_rounder)