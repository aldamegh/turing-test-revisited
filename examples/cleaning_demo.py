"""Synthetic text-cleaning example; no model, dataset, or predictions."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from preprocessing.arabic_cleaning import clean_arabic_text


def main():
    samples = [
        "أهلا #مثال @demo https://example.invalid/demo",
        "إبداع في آفاق اللغة العربية",
        "جميييييل",
        "مِثال",
    ]
    print("Synthetic Arabic cleaning examples")
    for text in samples:
        print(f"Input:  {text}")
        print(f"Output: {clean_arabic_text(text)}\n")
    print("Cleaning helper only; model training and scores are not shown.")


if __name__ == "__main__":
    main()
