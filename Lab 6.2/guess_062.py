from random import randint

top = 1000000
bottom = 0
z = randint(bottom, top)

def guess(g):
    if g == z:
        return 0
    elif g < z:
        return -1
    else:
        return 1

# Find z *efficiently* by calling guess() (and without peeking at z!)
def find():
    initial = 0
    top = 1000000
    while initial < top:
        mid = (initial + top) // 2
        result = guess(mid)
        if result == 0:
            return mid
        else:
            if result == -1:
                initial = mid + 1
            else:
                top = mid - 1
    return initial


def main():
    a = find()
    if a == z:
        print('Correct!')
    else:
        print('Incorrect!')
    print('You said {} and answer is {}'.format(a, z))

if __name__ == '__main__':
    main()
