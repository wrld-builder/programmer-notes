import abc


def foo1(): print('foo1 foo1() call')
foo1_var = foo1
foo1_var()

def sum_(a, b): return a + b
sum_var = sum_
print('sum_', sum_var(1, 2))

def do_operation(a, b, operation): return operation(a, b)
print('do_operation', do_operation(1, 2, sum_))

def select_operation(operation_code):
    if operation_code == 'sum': return sum_
print('select_operation', select_operation('sum')(1, 2))

foo2 = lambda: print('foo2 foo2() call')
foo2()

sum_ = lambda a, b: a * b
print('[lambda] sum_', sum_(2, 5))

print('[last_arg=lambda] do_operation', do_operation(10, 10, lambda x, z: x / z))

name = 'Bob'
def say_hello1():
    name = 'Mikhail'
    print(f'say_hello1 Hello, {name}')
say_hello1()
print('print', name)

def say_hello2():
    global name
    name = 'Mikhail'
    print(f'say_hello1 Hello, {name}')
say_hello2()
print('print', name)

def outer1():
    var = 10

    def inner():
        var = 30
        print('inner', var)

    inner()
    print('outer1', var)
outer1()

def outer2():
    var = 10

    def inner():
        nonlocal var
        var = 30
        print('inner', var)

    inner()
    print('outer2', var)
outer2()

def outer3():         # closure
    n = 0           # lexical env

    def inner():
        nonlocal n
        n += 10
        print('outer3->inner', n)
    return inner
outer3_local = outer3()
outer3_local()
outer3_local()

def square(): return lambda m: 2 ** m
a = square()
print('[lambda]<-inner->print', a(2))
print('[lambda]<-inner->print', a(5))

def pretty_print(input_func):
    def output_func():
        print('*' * 20)
        input_func()
        print('*' * 20)
    return output_func

@pretty_print
def say_hello_decorator():
    print('say_hello_decorator Hello decorator!')
say_hello_decorator()

###################################################################

def check_age(func):
    def output_func(*args):
        if args[0] <= 0: print('Wrong age!')
        else: func(*args)
    return output_func


bob_age = 0
@check_age
def set_age_to_bob(age: int):
    global bob_age
    bob_age = age
    print('set_age_to_bob Age setted to Bob! His age:', bob_age)
set_age_to_bob(500)
set_age_to_bob(-10)

###################################################################

def my_abs(func):
    def output_func(*args):
        result = func(*args)

        if result < 0: return result * -1
        return result
    return output_func

@my_abs
def something_operation(a, b): return a + b
print('something_operation', something_operation(-111, 22))
print('something_operation', something_operation(10, 22))

###################################################################

class Person:
    def __init__(self, name_):
        self.name = name_
        print(f'__init__ Created person with name: {self.name}')

    def __del__(self):
        print(f'__del__ Deleted person with name: {self.name}')

    def __repr__(self):
        return f'Person {self.name}'

bob = Person('Bob')
bob.name = 'Tom'      # name changed, no encapsulation
print(bob)
del bob
print()

###################################################################

class PersonUpgrade:
    def __init__(self, name_):
        self.__name = name_
        print(f'__init__ Created personUpgrade with name: {self.__name}')

    def __del__(self):
        print(f'__del__ Deleted personUpgrade with name: {self.__name}')

    def __repr__(self):
        return f'Person {self.__name}'

mike = PersonUpgrade('Mike')
mike.__name = 'Tom'      # name not changed, encapsulation works [dynamic attribute created]

mike.___killer = 'Killer text'      # new attributes created
print(mike)
print(mike.___killer)

del mike

###################################################################

class Employee:
    def __init__(self, name_):
        self.name = name_

    def work(self):
        print(f'{Employee.__name__} {self.name} is working...')

class Student:
    def __init__(self, name_):
        self.name = name_

    def study(self):
        print(f'{Student.__name__} {self.name} is studying...')

class StudentWorker(Employee, Student):
    def work(self):
        super().work()
        print('Company name: ATlas')


studentMikhail = StudentWorker('Mikhail')
studentMikhail.work() ; print()
studentMikhail.study() ; print()

###################################################################

def act(obj):
    if isinstance(obj, Student):
        obj.study()
    if isinstance(obj, Employee):
        obj.work()
act(studentMikhail)

###################################################################

class Animal(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def act(): pass

class Cat(Animal):
    @staticmethod
    def act():
        print('Meow!!!')

class Dog(Animal):
    @staticmethod
    def act():
        print('Bark!!!')

Cat.act()
Dog.act()

###################################################################

class Shape(abc.ABC):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @abc.abstractmethod
    def square(self): pass

    def print_metrics(self): print(f'a: {self._a} ; b: {self._b}')

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__(a, b)

    def square(self):
        return self._a * self._b

rect = Rectangle(2, 3)
rect.print_metrics()
print(f'Square rect.: {rect.square()}')

###################################################################

class PersonAgeException(Exception):
    def __init__(self, age):
        self.__age = age

    def __repr__(self):
        return f'Age must be > 0 exception expected: {self.__age!r}'  # not work based by Exception, repr() call. semantic focus

    def __str__(self):
        return f'Age must be > 0 exception expected: {self.__age}'

age = -5
if age <= 0:
    try:
        raise PersonAgeException(age)
    except PersonAgeException:
        print(repr(PersonAgeException(age)))

###################################################################

a = '[1, 2, 3, 4, 5]'
a = eval(a)        # convert to object from str
a.append(6)
print(a)

###################################################################

a = list([1, 2, 3])
b = [1, 2, 3]
if a == b: print('a == b [list]')
if a is b: print('a is b [list objects]')
if a is not b: print('a is not b [list objects]')

###################################################################

a = tuple((1, 2, 3))
b = (1, 2, 3)
if a == b: print('a == b [tuple]')
if a is b: print('a is b [tuple objects]')
if a is not b: print('a is not b [tuple objects]')

###################################################################

a = tuple((1, 2, 3))
b = (1, 2, 3)
if a == b: print('a == b [tuple]')
if a is b: print('a is b [tuple objects]')
if a is not b: print('a is not b [tuple objects]')

###################################################################

a = range(1, 5)
b = range(1, 5)
if a == b: print('a == b [range]')
if a is b: print('a is b [range objects]')
if a is not b: print('a is not b [range objects]')

###################################################################

a = {1, 2, 3}
b = {1, 2, 3}
if a == b: print('a == b [set]')
if a is b: print('a is b [set objects]')
if a is not b: print('a is not b [set objects]')

###################################################################

numbers = [-1, 1, 2, 2, 3, 2, 3, 2, -10, -23]
print([num for num in numbers if num < 0])

###################################################################

x, y = 1, 2
print('x:', x, 'y:', y)

x, y = (5, 6)
print('x:', x, 'y:', y)

person = ('Tom', 38, 'Atlas INC', 'Delaware', 'USA')
name, _, company, *other = person
print(name, company, *other, sep=' | ')

###################################################################

num1 = [1, 2, 3]
num2 = [4, 5, 6]
num = [*num1, *num2]
print(num)

###################################################################

def fun(*args):
    return [i for i in args]

print('fun', fun(1, 2, 3))

###################################################################

def fun2(**kwargs):
    return [(key, val) for key, val in kwargs.items()]
print('fun2', fun2(hello='world', i='am'))

###################################################################

def sum__(*args):       # my fast wrapper
    return sum(args)

numbers_to_sum = (1, 2, 3, 4, 6)
print(sum__(*numbers_to_sum))


###################################################################

def sum(num1, num2, *nums):
    result = num1 + num2
    for n in nums:
        result += n
    return result


print(sum(1, 2, 3))  # 6
print(sum(1, 2, 3, 4))  # 10

###################################################################

def print_hello_multi_lang(lang):
    match lang:
        case 'rus' as code:
            print('Привет', code)
        case 'en' | "american english" | "british english" | "english":
            print('Hello')
        case _:
            print('Undefined lang')

print_hello_multi_lang('rus')
print_hello_multi_lang('british english')
print_hello_multi_lang('sss')
