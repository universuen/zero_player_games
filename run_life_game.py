from games.life_game import LifeGame
from games.utils import generate_random_board

if __name__ == '__main__':
    LifeGame(
        generate_random_board(900, 1600, 0.6),
    ).run(
        interval=30
    )

