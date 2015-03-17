import pickle 

class game_record:
    def __init__(self):
        self.name = None
        self.platform = None
        self.genre = None
        self.cost = None
        self.players = None
        self.online = None
games =game_record()
games_list = []

def load_games(filename):
    with open(filename, mode = "rb") as file:
        games_list = pickle.load(file)
        return games_list  
        
def save_games(filename,games_list):
    with open(filename, mode = "wb") as file:
        pickle.dump(games_list,file)
    
#the parameter is games because eventually you will be displaying
#multiple games using this function
def display_games(games_list):
    name = "Name"
    platform = "Platform"
    genre = "Genre"
    cost = "Cost"
    players = "Players"
    online = "Online"
    print("-" * 79)
    print("| {0:^10} | {1:^10} | {2:^10} | {3:^10} | {4:^10} | {5:^10} |".format(name, platform, genre, cost, players, online))
    print("-" * 79)
    for game in games_list:
        print("| {0:^10} | {1:^10} | {2:^10} | {3:^10} | {4:^10} | {5:^10} |".format(game.name, game.platform, game.genre, game.cost, game.players, game.online))
        print("-" * 79)
      

def get_game_from_user(games,games_list):
    rogue = "0"
   
    while rogue!= "-1":
        games =game_record()
        games.name= input("Please enter the name: ")
        games.platform= input("Please enter the platform: ")
        games.genre= input("Please enter the genre: ")
        games.cost= input("Please enter the cost: ")
        games.players= input("Please enter the number of players: ")
        games.online= input("Please enter the games online status: ")
        games_list.append(games)
        rogue = input("Enter rogue: ")
    return games_list

def display_menu():
    print()
    print("***Welcome to the Computer and Video Game Database***")
    print()
    print("1. Add new games")
    print("2. Display games")
    print("3. Exit program")
    print()

def main():
    game_list = []
    user_file = input("Please enter the file name: ")
    games_list = load_games(user_file)
    exit_program = False
    while not exit_program:
        display_menu()
        selected_option = input("Please select a menu option: ")
        if selected_option == "1":
            games_list = get_game_from_user(games,games_list
                                        )
        elif selected_option == "2":
            display_games(games_list)
        elif selected_option == "3":  
            save_games(user_file, games_list)
            exit_program = True
        else:
            print("That wasnt acceptable becuase it wasnt one of the given options.")
            print("Please enter a valid option (1-3)")
            print()

if __name__ == "__main__":
    main()




