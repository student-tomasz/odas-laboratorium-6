#!./env/bin/python

def pad(data):
    numdata = map((lambda d: ord(d) + 100), data)
    paddata = []
    while True:
        if len(numdata) > 4:
            chunk = reduce((lambda r, n: r * 1000 + n), numdata[:4])
            paddata.append(chunk)
            numdata = numdata[4:]
        else:
            chunk = reduce((lambda r, n: r * 1000 + n), numdata)
            chunk *= 1000 ** (4 - len(numdata))
            paddata.append(chunk)
            break
    return paddata

def unpad(paddata):
    data = []
    for numchunk in paddata:
        chunk = []
        for i in range(4):
            d = numchunk % 1000
            if d != 0:
                chunk.append(d)
            numchunk //= 1000
        chunk.reverse()
        data.extend(chunk)
    return ''.join(map((lambda d: chr(d - 100)), data))



if __name__ == '__main__':
    samples = ['a', 'asd', 'asda', 'asdasd', 'asdasdas']
    assumptions = map((lambda s: s == unpad(pad(s))), samples)
    for assumption in assumptions:
        if assumption:
            print 'passed'
        else:
            print 'failed'
