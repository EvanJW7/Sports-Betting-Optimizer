import numpy as np
import pandas as pd
def game_projection(spread, total, percent_of_bets, favteam, underdog):
    if spread<0:
        spread = spread *-1
    else:
        pass
    betsfinal = (percent_of_bets)/100
    optimizer = (spread + ((.5 - betsfinal)*30))
    ospread = (format(optimizer, ".2"))
    ospread = float(ospread)
    x = ((total + ospread)/2)
    y = total - x
    total = x + y
    ospread = x - y
    print(f"\nThe projected outcome of the game is:\n")
    favtotal = f"{favteam.title():<15}{x:>1}"
    print(favtotal)
    dogtotal = f"{underdog.title():<15}{y:>1}"
    print(dogtotal)
    format_ospread = "{:.1f}".format(ospread)
    format_ospread = float(format_ospread)*-1
    if format_ospread <0:
        points_final = format_ospread*-1
        print(f"\nThe {favteam.title()} are projected to win by {points_final} points")
    if format_ospread>0:
        print(f"\nUpset Alert! The {underdog.title()} are projected to win by {format_ospread} points")
    print(f"\nOriginal Spread: {spread}")
    print(f"\bOptimized Spread: {format_ospread}\n")
    #BET SUGGESTION
    print("Bet Suggestion: ")
    bet1 = spread
    bet2 = format_ospread
    bet = bet1 - bet2
    if bet <=-4 and format_ospread >0:
        print(f"Bet the moneline on the {underdog.title()}")
    elif bet <=-4 and format_ospread <0:
        print(f"Bet the spread on the {underdog.title()}")
    elif -4<bet<=-2:
        print(f"Bet the spread on the {underdog.title()}")
    elif -2<bet<2:
        print("Do not bet on this game, there isn't enough edge")
    elif 2<=bet<4:
        print(f"Bet the moneline on the {favteam.title()}")
    elif bet>=4:
        print(f"Bet the spread on the {favteam.title()}")
    start = 0
    f1 = x/4  
    f2 = x/4+ x/4
    f3 = x/4 + x/4 + x/4 
    f4 = x/4 + x/4 + x/4 + x/4
    favteam_points = start, f1, f2, f3, f4
    favteam_points = tuple([float("{0:.2f}".format(n)) for n in favteam_points])
    u1 = y/4
    u2 = y/4+ y/4  
    u3 = y/4 + y/4 + y/4  
    u4 = y/4 + y/4 + y/4 + y/4
    underdog_points = start, u1, u2, u3, u4
    underdog_points = tuple([float("{0:.2f}".format(n)) for n in underdog_points])
    from pandas import DataFrame
    f1 = "{:.1f}".format(f1)
    f2 = "{:.1f}".format(f2)
    f3 = "{:.1f}".format(f3)
    f4 = "{:.1f}".format(f4)
    u1 = "{:.1f}".format(u1)
    u2 = "{:.1f}".format(u2)
    u3 = "{:.1f}".format(u3)
    u4 = "{:.1f}".format(u4)
    boxscore = {
        "1": [f1, u1],
        "2": [f2, u2],
        "3": [f3, u3],
        "4": [f4, u4]
        
    }
    rows = favteam.title(), underdog.title()
    data = pd.DataFrame(boxscore, rows)
    
    
    import matplotlib.pyplot as plt
   
    Quarter = ['0','12','Halftime','36', '48']
    Points1 = favteam_points
    Points2 = underdog_points
    def getcolor(favteam):
        if favteam == 'bucks':
            colors = 'forestgreen'
        if favteam == '76ers':
            colors = 'royalblue'
        if favteam == 'bulls':
            colors = 'tab:red'
        if favteam == 'cavaliers':
            colors = 'tab:brown'
        if favteam == 'celtics':
            colors = 'green'
        if favteam == 'clippers':
            colors = 'mediumblue'
        if favteam == 'grizzlies':
            colors = 'lightskyblue'
        if favteam == 'hawks':
            colors = 'firebrick'
        if favteam == 'heat':
            colors = 'maroon'
        if favteam == 'hornets':
            colors = 'cyan'
        if favteam == 'jazz':
            colors = 'orange'
        if favteam == 'kings':
            colors = 'tab:purple'
        if favteam == 'knicks':
            colors = 'tab:orange'
        if favteam == 'lakers':
            colors = 'gold'
        if favteam == 'magic':
            colors = 'blue'
        if favteam == 'mavericks':
            colors = 'dodgerblue'
        if favteam == 'nets':
            colors = 'black'
        if favteam == 'nuggets':
            colors = 'midnightblue'
        if favteam == 'pacers':
            colors = 'yellow'
        if favteam == 'pelicans':
            colors = 'orangered'
        if favteam == 'pistons':
            colors = 'red'
        if favteam == 'raptors':
            colors = 'brown'
        if favteam == 'rockets':
            colors = 'crimson'
        if favteam == 'spurs':
            colors = 'gray'
        if favteam == 'suns':
            colors = 'darkorange'
        if favteam == 'thunder':
            colors = 'royalblue'
        if favteam == 'timberwolves':
            colors = 'lime'
        if favteam == 'blazers':
            colors = 'tomato'
        if favteam == 'trail blazers':
            colors = 'tomato'
        if favteam == 'warriors':
            colors = 'yellow'
        if favteam == 'wizards':
            colors = 'lightcoral'
        return colors
    colors = getcolor(favteam)
    def getcolor(underdog):
        if underdog == 'bucks':
            coloru = 'forestgreen'
        if underdog == '76ers':
            coloru = 'royalblue'
        if underdog == 'bulls':
            coloru = 'tab:red'
        if underdog == 'cavaliers':
            coloru = 'tab:brown'
        if underdog == 'celtics':
            coloru = 'green'
        if underdog == 'clippers':
            coloru = 'mediumblue'
        if underdog == 'grizzlies':
            coloru = 'lightskyblue'
        if underdog == 'hawks':
            coloru = 'firebrick'
        if underdog == 'heat':
            coloru = 'maroon'
        if underdog == 'hornets':
            coloru = 'cyan'
        if underdog == 'jazz':
            coloru = 'orange'
        if underdog == 'kings':
            coloru = 'tab:purple'
        if underdog == 'knicks':
            coloru = 'tab:orange'
        if underdog == 'lakers':
            coloru = 'gold'
        if underdog == 'magic':
            coloru = 'blue'
        if underdog == 'mavericks':
            coloru = 'dodgerblue'
        if underdog == 'nets':
            coloru = 'black'
        if underdog == 'nuggets':
            coloru = 'midnightblue'
        if underdog == 'pacers':
            coloru = 'yellow'
        if underdog == 'pelicans':
            coloru = 'orangered'
        if underdog == 'pistons':
            coloru = 'red'
        if underdog == 'raptors':
            coloru = 'brown'
        if underdog == 'rockets':
            coloru = 'crimson'
        if underdog == 'spurs':
            coloru = 'gray'
        if underdog == 'suns':
            coloru = 'darkorange'
        if underdog == 'thunder':
            coloru = 'royalblue'
        if underdog == 'timberwolves':
            coloru = 'lime'
        if underdog == 'blazers':
            coloru = 'tomato'
        if underdog == 'trail blazers':
            coloru = 'tomato'
        if underdog == 'warriors':
            coloru = 'yellow'
        if underdog == 'wizards':
            coloru = 'lightcoral'
        return coloru
    coloru = getcolor(underdog)
    
    plt.plot(Quarter, Points1, label = favteam.title(), color = getcolor(favteam), lw = 1, marker = '.', ms = 10)
    plt.plot(Quarter, Points2, label = underdog.title(), color = getcolor(underdog), lw = 1, marker = '.', ms = 10)
    plt.title('Game Spread Projection')
    plt.xlabel('Quarter (in minutes)')
    plt.ylabel('Expected Points')
    plt.legend(fontsize = 'large', loc=9)
    plt.style.use('fivethirtyeight')
    print(data)
    plt.show()
    #print(f'\n{favteam.title()} slope: ')

    #f4 = float(f4)
    #favteamslope = f4/48
    #print(format(favteamslope, ".3"))
    #print(f"\n{underdog.title()} slope: ")
    #u4 = float(u4)
    #underdogslope = u4/48
    #print(format(underdogslope, ".3"))
    #print(f"\nHalftime score: {f2} to {u2}")
    #print(f"\nFinal score: {f4} to {u4}")
a = float(input("Spread: "))
b = float(input("Over/Under: "))
c = float(input(f"Percent of bets on the favorite: "))
d = input("Favorite: ")
d = d.lower()
e = input("Underdog: ")
e = e.lower()
game_projection(a, b, c, d, e)
