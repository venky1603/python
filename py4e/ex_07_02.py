#Exercise 7.02

valid = None
while valid is None:
    fileName = input('Enter file name: ')
    try:
        fileHandle = (open(fileName))
        valid = 1
        value = 0
        count = 0
        text = "X-DSPAM-Confidence:"
        for line in fileHandle:
            if not line.startswith(text):
                continue
            pos = line.find(':')
            slice = line[pos+1:]
            try:
                fl_slice = float(slice)
            except Exception as e:
                print('Error conducting operation')
            count = count + 1
            value = value + fl_slice
        avg = value / count
        print('Average spam confidence:',avg)
    except Exception as e:
        print('Enter a valid file name')
