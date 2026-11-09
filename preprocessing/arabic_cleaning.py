"""Cleaning helper extracted from a later local research variant saved 2025-12-17.

The streaming CSV command below was added for publication in November 2026.
"""
import re

def clean_arabic_text(text):
    if not isinstance(text, str):
        return ""

    # 1. إزالة الروابط (URLs)
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # 2. إزالة المنشن والهاشتاج (ابقاء الكلمة وحذف الرمز #)
    text = re.sub(r'@\S+', '', text)
    text = re.sub(r'#', '', text)
    
    # 3. توحيد الحروف (Normalization)
    # تحويل (إ، أ، آ) إلى (ا) | تحويل (ة) إلى (ه) | تحويل (ى) إلى (ي)
    text = re.sub(r'[إأآ]', 'ا', text)
    
    # 4. إزالة التطويل (المد) مثل: "جمييييييل" تصبح "جميل"
    text = re.sub(r'(.)\1+', r'\1\1', text) # يبقي على حرفين فقط كحد أقصى
    
    # 5. إزالة الرموز التعبيرية (Emojis) والرموز غير العربية
    # سنبقي فقط على الحروف العربية والمسافات
    text = re.sub(r'[^\u0600-\u06FF\s]', ' ', text)
    
    # 6. إزالة المسافات الزائدة
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def main():
    import argparse
    import csv
    from pathlib import Path
    parser = argparse.ArgumentParser(description="Clean an authorized text/label CSV")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    source, destination = Path(args.input), Path(args.output)
    if source.resolve() == destination.resolve():
        parser.error("Choose a separate output file")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with source.open(encoding="utf-8-sig", newline="") as incoming:
        reader = csv.DictReader(incoming)
        if not {"text", "label"}.issubset(reader.fieldnames or []):
            parser.error("Input requires text and label columns")
        with destination.open("x", encoding="utf-8", newline="") as outgoing:
            writer = csv.DictWriter(outgoing, fieldnames=["text", "label"])
            writer.writeheader()
            for row in reader:
                cleaned = clean_arabic_text(row["text"])
                if row["label"] not in {"0", "1"}:
                    raise ValueError("Labels must be 0 or 1")
                if cleaned:
                    writer.writerow({"text": cleaned, "label": row["label"]})


if __name__ == "__main__":
    main()
