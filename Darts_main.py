print('Welcome To Darts!')

Select_Game = input('Select Game, 301/501: ')

while Select_Game not in ['301','501']:
    print('Nonexistent Game')
    Select_Game = input('Select Game, 301/501: ')

Num_Players = 0

while True:
    try:
        Num_Players = int(input('Enter the number of players: '))
        if Num_Players < 1 or Num_Players > 100:
            print('Invalid Number')
            continue
    except ValueError:
        print('Invalid Number')
        continue
    break

Int_Select_Game = int(Select_Game)
Game_Points = [Int_Select_Game] * Num_Players
winner = False

print(f'Starting Points: {Game_Points}')
Dart1 = 0
Dart2 = 0
Dart3 = 0

while True:
    for i in range(Num_Players):
        while True:
            try:
                Dart1 = int(input(f'Player {i + 1} First Dart: '))
                if not 0 <= Dart1 <= 60:
                    print('Must be a number between 1 and 60')
                    continue
            except ValueError:
                print('Invalid Number')
                continue
            break
        while True:
            try:
                Dart2 = int(input(f'Player {i + 1} Second Dart: '))
                if not 0 <= Dart2 <= 60:
                    print('Must be a number between 1 and 60')
                    continue
            except ValueError:
                print('Invalid Number')
                continue
            break
        while True:
            try:
                Dart3 = int(input(f'Player {i + 1} Third Dart: '))
                if not 0 <= Dart3 <= 60:
                    print('Must be a number between 1 and 60')
                    continue
            except ValueError:
                print('Invalid Number')
                continue
            break

        Int_Points = Game_Points[i] - (Dart1 + Dart2 + Dart3)

        if Int_Points < 0:
            print(f'You went too far. Points stay the same!')
        elif Int_Points == 0:
            Game_Points[i] = 0
            print(f'Player {i+1} won!')
            winner = True
            break
        else:
            Game_Points[i] = Int_Points
            print(f'Player {i+1} remaining points: {Int_Points}')
    if  winner:
        break

