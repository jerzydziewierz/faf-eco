# this assumes that faf is already installed.
import faf
from faf import init_game_state, game_step


def main():
    print("Hello world!")
    for idx, item in enumerate(dir(faf)):
        if not item.startswith("_"):
            print(f"|{idx:04d} : {item}")

    gs = init_game_state()

    for idx in range(300000):
        gs, is_game_over = game_step(gs)
        if is_game_over:
            break

    print(gs)
    print(f'game over in {gs.idx_gamecycle} steps.')
