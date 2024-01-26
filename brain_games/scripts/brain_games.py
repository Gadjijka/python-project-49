#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.game_logic import play_game
from brain_games.games import brain_even, brain_calc, brain_gcd, brain_prime, brain_progression


def main():
    welcome_user()


if __name__ == '__main__':
    main()

