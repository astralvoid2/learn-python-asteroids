Asteroids Game

A basic imple,mentation of the classic Asteroids game using Python and Pygame.  This project was created as a learning exercise to explore game development concepts.

## Requirements
- Python 3.8 or higher
- uv (Install via `pip install uv`)
- Pygame (will be installed automatically with uv project)

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
2. Install dependencies:
    On Mac/Linux: ```curl -LsSf https://astral.sh/uv/install.sh | sh```
    On Windows (PowerShell): ```powershell -c "irm https://astral.sh/uv/install.psd1 | iex"```
    
## Running the Game

This project uses uv to manage dependencies and run the game in an isolated virtual environment. Assuming dependencies (like Pygame) are listed in a pyproject.toml or requirements.txt file (if not, add pygame via uv add pygame and commit the updated files).

To launch the game, run:
```launch:  uv run main.py
```

If you are using a traditional virtual environment, activate it and run:
```
python3 -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements.txt
python3 main.py
```
## Controls
- A/D Keys: Rotate the spaceship
- W Key: Thrust forward
- Spacebar: Shoot bullets

## Notes
- This is a very basic implementation and can be expanded with more features like scoring, levels, sound effects, etc.
- Feel free to fork and modify the code to enhance the game!



