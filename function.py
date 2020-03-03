# def test():
#     print("Hello Function")
#
# test()

#  function return  value

# def users():
#     return "I am users"
#
#
# print(users())

# function accept value

# def users(name, age=0):
#     print(name, age)
#
#
# users('ram', 20)

# def users(*names, **data):
#     print(names)
#     print(data)
#
#
# users('ram', 'sita', name='sita', age=20, phone=98987)

# data = lambda x, y: x + y
#
# print(data(10, 20))


# x = 20
#
# def test():
#     global x
#     x = x + 20
#     print(x)
#
#
# test()

# def users():
#     def name(name):
#         return "Hello name "+name
#
#     return name
#
#
# x = users()
# print(x('am'))

# def my_resp(data, tm):
#     x = 0
#     while x <= tm:
#         print(data)
#         x += 1
#
#
# my_resp('ram', 10)

# data = []


# def add_emp(num):
#     x = 1
#     while x <= num:
#         name = input('Enter name: ')
#         data.append(name)
#         x += 1
#
#
# num_of_emp = int(input('Enter emp number: '))
# add_emp(num_of_emp)
# for emp in data:
#     print(f'your name is {emp}')

# def users(*name, **data):
#     print(name)
#     print(data)
#
#
# users('ram', 'sita', 'gita', name='sophia', age=20, phone=98987)
#
# def users():
#     """ Hello users function """
#     return "Hello function "
#
#
# print(users.__doc__)


# print(print.__doc__)

# print(help(list))
# print(list.__doc__)

data = lambda x, y: x + y

print(data(10, 20))

print("update message")
