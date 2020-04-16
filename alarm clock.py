import winsound, time, os, platform

def sound(p):
    for i in range(10):
        winsound.MessageBeep(-1)
        time.sleep(1)


def when_sound(p):
    time.sleep(p)
    sound(p)


def input_no(n):
    if (n == 1):
        x = int(input('Enter hours : '))
        when_sound(60*60*x)
    elif (n==2):
        x = int(input('Enter minutes : '))
        when_sound(60*x)
    elif (n == 3):
        x = int(input('Enter seconds : '))
        when_sound(x)
    elif (n == 4) :
        hours = int(input('Enter Hours : '))
        min = int(input('Enter minutes : '))
        sec = int(input('Enter seconds : '))
        when_sound((hours*60*60)+(min*60)+(sec))




def main():
    print("enter time after which alarm should ring: press 1)for hours 2)for minutes 3)for seconds 4)for combination")
    n = int(input(":"))
    input_no(n)

main()