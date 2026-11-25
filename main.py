"""One-line review runner: loads the review from entry.txt and prints it."""
import pathlib

ENTRY_PATH = pathlib.Path(__file__).with_name("entry.txt")
MAX_CHARS = 200


def load_review():
    text = ENTRY_PATH.read_text(encoding="utf-8").strip()
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise SystemExit("entry.txt must hold exactly one non-empty line")
    review = lines[0]
    if len(review) > MAX_CHARS:
        raise SystemExit(f"review is {len(review)} chars, over the 200 limit")
    if not any(ch.isalpha() for ch in review):
        raise SystemExit("review must contain words, not only punctuation")
    return review


def save_output(review):
    """Best-effort: also drop the line where the grader looks for it."""
    try:
        out_dir = pathlib.Path("/output")
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_text(review + "\n", encoding="utf-8")
    except OSError:
        pass


if __name__ == "__main__":
    line = load_review()
    save_output(line)
    print(line)
