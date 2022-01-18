
import math
1 == 1
name = input('What is your name... ')
print('nice to meet you')
print(name )
age = int(input('How old are you? '))
print ('Realy you are only...')
print(age )
print('I am only a few minute days old')
number = float(input('what is 2 + 2? '))
if number == 4:
    print('correct')
else:
    print('incorrect')
a = float(input('what is 10 x 10? '))
if a == 100:
    print('GREAT JOB!!!!')
    b = float(input('what is 1 + 2? '))
    if b == 3:
        print('Keep GOING!')
        c = float(input('pick a number between 1 and 20. '))
        if 12 < c < 16:
            print('close enuff')
            print('it was 13')
            d = float(input('what is your age X 17? '))
            e = 17
            if d == age  * e:
               print('correct')

            else:
                print('incorrect')
        else:
            print('game over')    
    else:
        print('game over')
else:
    print('game over')




