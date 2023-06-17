from pdfminer.high_level import extract_text, extract_text_to_fp
import difflib

fp = "E:/my_works/programming/python/pdf-compare/samples/pdfs/receipt.pdf"

sample1 = "E:/my_works/programming/python/pdf-compare/samples/pdfs/Sample1.pdf"
sample2 = "E:/my_works/programming/python/pdf-compare/samples/pdfs/Sample2.pdf"

text = extract_text(fp)
sample1_text = extract_text(sample1)
sample2_text = extract_text(sample2)

# diffs = difflib.Differ(sample1_text, sample2_text)
diffs2 = difflib.context_diff(sample1_text, sample2_text)
for diff in diffs2:
    print(diff)
# print(diffs2)