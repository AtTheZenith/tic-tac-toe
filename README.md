<h1 align='center'>
    Tic Tac Toe
</h1>

<h3 align='center'>
    A simple Tic Tac Toe game implemented using the urwid library in Python. 
</h3>

### Features:
- A start screen
- A game board
- 2 player gameplay
- WASD and ⬆⬅⬇➡ to place markers on the board.
- Replay button.

</br>

# Installation and usage

- Install any modern python version. (3.7+)
- Install git. (Optional)

### Without git

- Download the source code.

![Tutorial Screenshot 1](https://i-dont-use.arch-linux.xyz/-->/zv2pzqpq.png)
- Extract it and navigate to the folder.
- Open command prompt in it.

### With git

- Open command prompt and navigate to your downloads folder.

```bash
git clone https://github.com/AtTheZenith/tic-tac-toe/ # To download the repo.

cd ./tic-tac-toe    # To change directories after downloading.
```

</br>

## Setting up tic-tac-toe with pyvenv

- Run the following in your shell with the current directory being this repo.
```bash
python -m venv .venv    # The last venv is what the folder should be named,
                        # It can be .venv, or venv, or anything else.

.venv/Scripts/activate  # Enter the virtual enviroment.

pip install urwid       # Install the needed packages

python main.py          # will run the script, preferred if your terminal
                        # uses a monospace font such as fira code.
```

## Setting up tic-tac-toe with uv

- Run the following in your shell with the current directory being this repo.
```bash
uv venv                 # Set up a virtual enviroment.

.venv/Scripts/activate  # Enter the virtual enviroment.

uv run main.py          # Check dependencies and run main.py
                        # uv will auto-manage packages
                        # and the python version.
```
