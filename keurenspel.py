from GameSettings import GameSettings
from gameStates.StartMenuState import StartMenuState


def main():
    settings = GameSettings()
    StartMenuState(settings).activate()


if __name__ == "__main__":
    main()
