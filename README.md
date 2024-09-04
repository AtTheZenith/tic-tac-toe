# Tic Tac Toe

This is a simple Tic Tac Toe game implemented using the Urwid library in Python. The game features a start screen, a game board, and the ability to place markers on the board. The game checks for a winner or a draw after each move.

## Requirements

Python (3.12 is preferred as 3.12.1 is what I used to make this.) and the following packages:

- urwid

```bash
pip install urwid
# or alternatively
python -m pip install urwid
```

### Setting this up in pyvenv

Run the following in your shell with the current directory being this repo.

```bash
python -m venv venv     # the last venv is what the folder should be named,
                        # can be .venv, or venv, or anything else.

venv/Scripts/activate   # to enter the venv

pip install urwid       # install the needed packages

python main.py          # will run the script, preferred if your terminal
                        # uses a monospace font such as fira code.
```
