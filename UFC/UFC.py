def titlefightpredictor(moneyline, percent_of_bets, favorite, underdog):
    betsfinal = (percent_of_bets)/100
    optimizer = moneyline - ((.5 - betsfinal)*500)
    optimizer = format(optimizer, ".4")
    optimizer = float(optimizer)
    if optimizer >=90:
        outcome = f'{underdog.title()} will upset {favorite.title()} in the 1st round'
    elif 90>optimizer>30:
        outcome = f'{underdog.title()} will upset {favorite.title()} in the 2nd round'
    elif 30>=optimizer>-10:
        outcome = f'{favorite.title()} will upset {underdog.title()} in the 3rd round'
    elif -10>=optimizer>-55:
        outcome = f'{underdog.title()} will upset {favorite.title()} in the 4th round'
    elif -55>=optimizer>-80:
        outcome = f'{underdog.title()} will defeat {favorite.title()} in the 5th round'
    elif -80>=optimizer>-100:
        outcome = f'{underdog.title()} will upset {favorite.title()} by unanimous decision'
    elif -100>=optimizer>-105:
        outcome = f'{underdog.title()} will upset {favorite.title()} in a split decision'
    elif -110<=optimizer<=-105:
        outcome = f'{favorite.title()} wins a close match against {underdog.title()} in a split decision'
    elif -130<=optimizer<-110:
        outcome = f'{favorite.title()} will defeat {underdog.title()} by unanimous decision'
    elif -155<=optimizer<-130:
        outcome = f'{favorite.title()} will defeat {underdog.title()} in the 5th round'
    elif -200<=optimizer<-155:
        outcome = f'{favorite.title()} will defeat {underdog.title()} in the 4th round'
    elif -240<=optimizer<-200:
        outcome = f'{favorite.title()} will defeat {underdog.title()} in the 3rd round'
    elif -300<optimizer<-240:
        outcome = f'{favorite.title()} will defeat {underdog.title()} in the 2nd round'
    elif optimizer <=-300:
        outcome = f'{favorite.title()} will defeat {underdog.title()} in the 1st round'
        
    print(f"\nOriginal odds for {favorite.title()}: {moneyline}")
    
    if optimizer >-105:
        optimizer = optimizer+210
        print(f"Optimized odds for {favorite.title()}: +{optimizer}")
    else: 
        optimizer = optimizer
        print(f"Optimized odds for {favorite.title()}: {optimizer}")

    
    print(f"\n{outcome}")
            
a = float(input("Moneyline: "))
b = float(input("Percent of bets on the favorite: "))
c = input("Favorite: ")
d = input("Underdog: ")
titlefightpredictor(a,b,c,d)