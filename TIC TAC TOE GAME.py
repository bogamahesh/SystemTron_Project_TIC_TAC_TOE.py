import os
import time
import random

def type_text(text, delay=0.03):
    """Type text like a human with random delays"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay + random.uniform(0, 0.02))
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None
        self.game_count = 0
    
    def print_board(self):
        print("\n")
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("   " + " | ".join(row))
            if row != self.board[6:]:
                print("  -----------")
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
    
    def empty_squares(self):
        return " " in self.board
    
    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True
            
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
            
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

def get_player_names():
    clear_screen()
    type_text("Hey! Let's play Tic Tac Toe!", 0.05)
    time.sleep(0.5)
    type_text("\nPlayer 1, what's your name? ", 0.03)
    player1 = input().strip() or "Player 1"
    
    type_text(f"\nNice to meet you, {player1}!", 0.03)
    time.sleep(0.5)
    
    type_text("\nAnd Player 2, what's your name? ", 0.03)
    player2 = input().strip() or "Player 2"
    
    type_text(f"\nAwesome, {player2}! Let's get started!", 0.03)
    time.sleep(1)
    return player1, player2

def show_tutorial():
    clear_screen()
    type_text("Here's how to play:", 0.03)
    time.sleep(0.5)
    print("""
    The board positions are numbered like this:
    
       1 | 2 | 3
      -----------
       4 | 5 | 6
      -----------
       7 | 8 | 9
    """)
    type_text("\nJust enter the number where you want to place your mark!", 0.03)
    time.sleep(0.5)
    input("\nPress Enter when you're ready...")

def get_random_encouragement():
    messages = [
        "Nice move!",
        "Good choice!",
        "Interesting strategy...",
        "Well played!",
        "Let's see how this plays out!",
        "Getting exciting!",
        "Great move!",
        "This is getting interesting!"
    ]
    return random.choice(messages)

def play():
    game = TicTacToe()
    game.game_count += 1
    
    if game.game_count == 1:
        player1_name, player2_name = get_player_names()
        show_tutorial()
    
    players = {
        'X': player1_name,
        'O': player2_name
    }
    current_player = 'X'
    
    while game.empty_squares():
        clear_screen()
        game.print_board()
        
        current_name = players[current_player]
        type_text(f"\n{current_name}'s turn ({current_player})")
        
        move = None
        while move not in game.available_moves():
            try:
                move = int(input("\nWhere would you like to go? (1-9): ")) - 1
                if move not in game.available_moves():
                    type_text("Oops! That spot is already taken or invalid. Try another one!", 0.02)
            except ValueError:
                type_text("Please enter a number between 1 and 9!", 0.02)
        
        game.make_move(move, current_player)
        
        # Random thinking delay
        time.sleep(random.uniform(0.3, 0.7))
        type_text(get_random_encouragement(), 0.03)
        time.sleep(0.5)
        
        if game.current_winner:
            clear_screen()
            game.print_board()
            type_text(f"\nWow! Congratulations {players[current_player]}!", 0.05)
            time.sleep(0.5)
            type_text("You've won the game! 🎉", 0.05)
            return
        
        current_player = 'O' if current_player == 'X' else 'X'
    
    clear_screen()
    game.print_board()
    type_text("\nLooks like it's a tie game!", 0.03)
    time.sleep(0.5)
    type_text("You're both excellent players! 👏", 0.03)

def main():
    while True:
        play()
        time.sleep(1)
        type_text("\nWould you like to play again? (yes/no): ", 0.03)
        if not input().lower().startswith('y'):
            type_text("\nThanks for playing! See you next time!", 0.05)
            break
        type_text("\nAwesome! Let's go again!", 0.03)
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        type_text("\nGoodbye! Thanks for playing!", 0.05)