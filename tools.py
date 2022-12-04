from pathlib import Path

ROOT = Path(__file__).parent


def load_input(path):
    return Path(ROOT / path / "input.txt").read_text()
