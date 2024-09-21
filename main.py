try:
    a=int(input('Enter a number: '))
    print('Number is:',a)
except ValueError as v:
    print('Error is:',v)