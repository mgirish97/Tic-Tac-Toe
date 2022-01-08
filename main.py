

def main():
    
    start = True
    while start:
        print("Let's play Tic Tac Toe!")
        
        # List of marker positions
        marker_positions = [' ' for i in range(9)]
        
        # Make and print board
        board = make_board(marker_positions)
        print(board)
        
        # Player dictionaries
        player1 = {
            'name': 'Player 1',
            'marker': '',
            'positions': []
        }
    
        player2 = {
            'name': 'Player 2',
            'marker': '',
            'positions': []
        }
    
        # Player 1 and 2 choose their markers
        player1['marker'] = make_marker(player1['name'])
        player2['marker'] = make_marker(player2['name'])
        
        game_on = True
        while game_on:
            for player in [player1, player2]:
                # Numbered board is shown. Player chooses position
                show_numbered_board(marker_positions)
                chosen_position = int(input(f'{player["name"]}, choose from 1-9 to draw {player["marker"]}:  '))
                # Chosen position is marked
                marker_positions[chosen_position - 1] = player['marker']
                # Chosen position is added to player's dict
                player['positions'].append(chosen_position)
                # print(player['positions'])
                print(make_board(marker_positions))
                # Check if player won
                if check_win(player['positions']) or ' ' not in marker_positions:
                    game_on = False
                    if check_win(player['positions']):
                        print(f"{player['name']} has won!")
                    break
        play_again = input("Would you like to play again? Type 'Yes' or 'No':  ")
        if play_again.lower() == 'no':
            start = False


def make_board(positions):
    """Makes a blank 9 x 9 board."""
    board = f'''
      {positions[0]}  |  {positions[1]}  |  {positions[2]}
    -----------------
      {positions[3]}  |  {positions[4]}  |  {positions[5]}
    -----------------
      {positions[6]}  |  {positions[7]}  |  {positions[8]}
    '''
    return board


def make_marker(player_name):
    """Player chooses 'X' or 'O' marker."""
    marker_valid = False
    marker = ''
    while not marker_valid:
        marker = input(f"{player_name}, would you like to be 'X' or 'O'?\n").upper()
        if marker.upper() == 'X' or marker.upper() == 'O':
            marker_valid = True
        else:
            print("Please choose a valid option: 'X' or 'O'")
    return marker


def show_numbered_board(marker_positions):
    """Shows board with numbered positions. Takes in list of marked positions. Returns numbered positions"""
    numbers = [i + 1 for i in range(9)]
    for i in range(len(marker_positions)):
        if marker_positions[i] != ' ':
            numbers[i] = marker_positions[i]
    print(make_board(numbers))


def check_win(player_positions):
    win_conditions = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]
    win = False
    for cond in win_conditions:
        if cond[0] in player_positions and \
                cond[1] in player_positions and \
                cond[2] in player_positions:
            win = True
            break
    return win
    
    
if __name__ == '__main__':
    main()

