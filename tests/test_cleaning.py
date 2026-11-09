
import unittest
import tempfile
import subprocess
import sys
import csv
from pathlib import Path
from preprocessing.arabic_cleaning import clean_arabic_text

ROOT=Path(__file__).resolve().parents[1]
class CleaningTests(unittest.TestCase):
    def test_non_text(self): self.assertEqual(clean_arabic_text(None),'')
    def test_synthetic_links_and_mentions(self): self.assertEqual(clean_arabic_text('أهلا #مثال @demo https://example.invalid/x'),'اهلا مثال')
    def test_repetitions(self): self.assertEqual(clean_arabic_text('جميييييل'),'جمييل')
    def test_ascii(self): self.assertEqual(clean_arabic_text('hello 123 !!!'),'')
    def test_alef(self): self.assertEqual(clean_arabic_text('إ أ آ'),'ا ا ا')
    def test_diacritics_retained(self): self.assertEqual(clean_arabic_text('مِثال'),'مِثال')
    def test_csv_wrapper(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/'input.csv';dest=Path(d)/'output.csv'
            with src.open('w',encoding='utf-8',newline='') as f:
                w=csv.writer(f);w.writerow(['text','label']);w.writerow(['أهلا #مثال','1']);w.writerow(['hello','0'])
            subprocess.run([sys.executable,'-B',str(ROOT/'preprocessing/arabic_cleaning.py'),'--input',str(src),'--output',str(dest)],check=True,timeout=10)
            with dest.open(encoding='utf-8',newline='') as f:self.assertEqual(list(csv.DictReader(f)),[{'text':'اهلا مثال','label':'1'}])

if __name__=='__main__':unittest.main()
