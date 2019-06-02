# Exercise 6.05

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0')
slice = text[pos:]
try:
    fl_slice = float(slice)
    print(fl_slice)
except Exception as e:
    print('Error conducting operation')
