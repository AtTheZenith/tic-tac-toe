from __future__ import annotations
import typing
import urwid
from time import sleep

if typing.TYPE_CHECKING:
    from collections.abc import Iterable

body_placeholder = urwid.WidgetPlaceholder(urwid.SolidFill(' '))

xturn = True
board = [[' ' for _ in range(3)] for _ in range(3)]
selected_row, selected_col = 1, 1
game_over = True
winner = None

def clamp(value: float, min_value: float, max_value: float) -> float:
    return max(min_value, min(value, max_value))

def exit_program(*args, **kwargs) -> None:
    raise urwid.ExitMainLoop()

def lazy_fun(*args, **kwargs):
    game_over = False
    tic_tac_toe(None)

def start_screen() -> urwid.ListBox:
    global game_over
    body = [urwid.Text('\nTic Tac Toe', align='center'), urwid.Divider()]
    maintext = urwid.Text(['Welcome to Tic Tac Toe.\n'])
    start = urwid.Button('Start')
    quit = urwid.Button('Quit')
    urwid.connect_signal(start, 'click', lazy_fun)
    urwid.connect_signal(quit, 'click', exit_program)
    body.append(urwid.Filler(urwid.Pile([
        maintext,
        urwid.AttrMap(start, None, focus_map='reversed'),
        urwid.AttrMap(quit, None, focus_map='reversed'),
    ])))
    return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def render_board() -> urwid.Text:
    lines = []
    for i, row in enumerate(board):
        col_0 = row[0] if selected_col != 0 or selected_row != i else row[0] if row[0] == 'X' or row[0] == 'O' else '█'
        col_1 = row[1] if selected_col != 1 or selected_row != i else row[1] if row[1] == 'X' or row[1] == 'O' else '█'
        col_2 = row[2] if selected_col != 2 or selected_row != i else row[2] if row[2] == 'X' or row[2] == 'O' else '█'
        lines.append(f" {col_0} | {col_1} | {col_2}")
        if i != 2:
            lines.append('---+---+---')
    board_str = '\n'.join(lines)
    return urwid.Text(board_str, align='center')

def check_winner() -> typing.Optional[str]:
    global board
    winning_combinations = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    
    for combination in winning_combinations:
        if combination[0] == combination[1] == combination[2] != ' ':
            return combination[0]
    
    return False

def tic_tac_toe(winner: any) -> None:
    global xturn, game_over, selected_row, selected_col
    body = [urwid.Text('\nTic Tac Toe', align = 'center'), urwid.Divider()]
    if winner == 'X' or winner == 'O':
        body.append(urwid.Filler(urwid.Text(f"\n Player {winner} has won the game,\n Restarting in 3 seconds.\n\n\n", align = 'center'), valign = 'top'))
    elif winner == 'Draw':
        body.append(urwid.Filler(urwid.Text(f"\n It's a draw, nobody has won the game.\n Restarting in 3 seconds.\n\n\n", align = 'center'), valign= 'top'))
    else:
        body.append(urwid.Filler(urwid.Text(f"\n It's player {xturn and 'X' or 'O'}'s turn.\n\n\n\n", align = 'center'), valign = 'top'))
    body.append(urwid.Filler(render_board(), valign='middle'))
    body.append(urwid.Filler(urwid.Text("\n\n\n\nPress arrow keys to move, enter to place, or 'q' to quit.\n", align = 'center'), valign = 'bottom'))

    body_placeholder.original_widget = urwid.ListBox(urwid.SimpleFocusListWalker(body))
    
    if game_over:
        game.set_alarm_in(3,reset_game)

def exit_on_q(key):
    global winner, xturn, selected_row, selected_col, game_over
    
    if key in ['q', 'Q']:
        exit_program()
    
    if not game_over:
        if key == 'enter':
            place_marker()
            winner = check_winner()
            if winner:
                game_over = True
                tic_tac_toe(winner)
            elif all(board[row][col] != ' ' for row in range(3) for col in range(3)):
                game_over = True
                tic_tac_toe('Draw')
            else:
                tic_tac_toe(None)
        elif key == 'up':
            selected_row = clamp(selected_row - 1, 0, 2)
            tic_tac_toe(None)
        elif key == 'down':
            selected_row = clamp(selected_row + 1, 0, 2)
            tic_tac_toe(None)
        elif key == 'left':
            selected_col = clamp(selected_col - 1, 0, 2)
            tic_tac_toe(None)
        elif key == 'right':
            selected_col = clamp(selected_col + 1, 0, 2)
            tic_tac_toe(None)

def place_marker():
    global xturn
    global selected_row, selected_col
    if board[selected_row][selected_col] == ' ':
        board[selected_row][selected_col] = 'X' if xturn else 'O'
        xturn = not xturn

def reset_game(*args, **kwargs) -> None:
    global board, xturn, selected_row, selected_col, game_over, winner
    board = [[' ' for _ in range(3)] for _ in range(3)]
    xturn = True
    winner = None
    selected_row, selected_col = 1, 1
    game_over = False
    tic_tac_toe(None)

top = urwid.Overlay(
    body_placeholder,
    urwid.SolidFill('\N{MEDIUM SHADE}'),
    align=urwid.CENTER,
    width=(urwid.RELATIVE, 80),
    valign=urwid.MIDDLE,
    height=(urwid.RELATIVE, 80),
    min_width=12,
    min_height=14,
)

body_placeholder.original_widget = start_screen()

game = urwid.MainLoop(top, palette=[('reversed', 'standout', '')], unhandled_input=exit_on_q)
game.run()