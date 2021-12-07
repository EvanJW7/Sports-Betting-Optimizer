import numpy as np
import pandas as pd
def game_projection(spread, percent_of_bets, total, favteam, underdog):
    betsfinal = (percent_of_bets)/100
    optimizer = spread + ((.5 - betsfinal)*30)
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
    print(f"\n{favteam.title()} is projected to win by {format_ospread} points")
    print(f"\nOriginal Spread: {spread}")
    print(f"\bOptimized Spread: {format_ospread}\n")
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
    
    fig = plt.figure(figsize = (12,9))
    Quarter = ['0','15','Halftime','45', '60']
    Points1 = favteam_points
    Points2 = underdog_points
    plt.plot(Quarter, Points1, label = favteam.title(), color = 'green', lw = 1, marker = '*', ms = 10)
    plt.plot(Quarter, Points2, label = underdog.title(), color = 'red', lw = 1, marker = '*', ms = 10)
    plt.title('Game Spread Projection')
    plt.xlabel('Quarter (in minutes)')
    plt.ylabel('Expected Points')
    plt.legend(fontsize = 'large', loc=9)
    plt.style.use('fivethirtyeight')
    
    print(f'\n{favteam.title()} slope: ')
    f4 = float(f4)
    favteamslope = f4/48
    print(format(favteamslope, ".3"))
    print(f"\n{underdog.title()} slope: ")
    u4 = float(u4)
    underdogslope = u4/48
    print(format(underdogslope, ".3"))
    print(f"\nHalftime score: {f2} to {u2}")
    print(f"\nFinal score: {f4} to {u4}")
    return data, plt.plot()
a = float(input("Spread: "))
b = float(input(f"Percent of bets on the favorite: "))
c = float(input("Over/Under: "))
d = input("Favorite: ")
d = d.lower()
e = input("Underdog: ")
e = e.lower()
game_projection(a, b, c, d, e)
