a = 666

print(F'Hello {a}')
print(f'Hello {a}')

########################################################

q = 5
fruit = 'bananas'
cost = 15.67
print('Cost of {} {} is {}$'.format(
    q, fruit, cost
))

########################################################

print(F'Sum of [1..10] is: {sum([i for i in range(10)])}')

########################################################

print(f'Handled value: {{666}} is {a}')

########################################################

print('Cost of {2} {0} is {1}$'.format(
    fruit, cost, q
))

########################################################

print('{0}{1}{2}.{3}.{3}.{0}'.format(         # loclahost!
    1, 2, 7, 0
))

########################################################

print('This is stackoferflow string: {} {}'.format(
    'a', 'b', 'c', 'd', 'e'
))

########################################################

try:
    print('Switching error: {1} {} {3}'.format(
        0, 1, 2, 3, 4
    ))
except ValueError:
    print('Switching error! {1} {} {3}')

########################################################

print('Cost of {q} {fruit} is {cost}$'.format(
    q=q, cost=cost, fruit=fruit
))
