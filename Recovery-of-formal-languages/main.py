import string
import math

alfa_valid = string.ascii_lowercase

def get_file(file):
  return open(file).read()

counterwhile = 0 

while counterwhile < 3:
  ready_list = []
  counterwhile = counterwhile + 1
  option_count = []
  file = get_file(f"test{counterwhile}.txt").split("\n")
  parentheses_validator = False
  checker = []

  for i in file:
    checker.append("1")
    a = i.split(" ")
    new = []
    left_parentheses_count = 0
    for m in a:
      for n in m:
        x = "("
        xe = ")"
        if n == x:
          left_parentheses_count = left_parentheses_count + 1
    right_parentheses_count = 0
    list_number_validator = False
    for l in a:
      for t in l:
        for o in t:
          if o.isdigit():
            list_number_validator = True


    for m in a:
      for n in m:
        x = "("
        xe = ")"
        if n == xe:
          right_parentheses_count = right_parentheses_count + 1
    if right_parentheses_count == left_parentheses_count:
      print(" ")
    else:
      print(" ")
      parentheses_validator = True
    for x in a:
      item = x
      for y in ['\n', '\t', '(', ')']:
        item = item.replace(y, "")
      new.append(item)
    a = new
    remove_interrog = False
    for interrog in a:
      if interrog == '?':
        remove_interrog = True
    ready_list_b = []


    a = [x for x in a if x != '?']


    buffer_option_count = False
    operation_validator = False

    for q in a:
      if q == 'op1' or q == 'op2':
        operation_validator = True
        option_count.append(a[1])
        option_count = [x for x in option_count if x != 'op1']
        option_count = [x for x in option_count if x != 'op2']
        buffer_option_count = True


    buffer = 0
    if operation_validator == True:
      for j in a:
        if j in ['*', '+', '-', '/']:
          buffer = j
      if buffer == '*':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = first_term * second_term
        print(
          '{} * {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)
        ready_list.append(ready_calculation)

      if buffer == '+':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = first_term + second_term
        print(
          '{} + {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)
      if buffer == '-':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = first_term - second_term
        print(
          '{} - {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)
      if buffer == '/':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = first_term / second_term
        print(
          '{} / {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)

    print("line {}".format(len(checker)), "lexemes: ", f" {i} ")

    if remove_interrog == True:
      for interrog in a:
        if interrog == '*':
          a = [x for x in a if x != '?']
          a = [x for x in a if x != '*']
          first_term = int(a[0])
          second = int(ready_list[0])
          print('{} / {} ='.format(float(option_count[0]), float(option_count[1])), ' %.3f' % (first_term * second))

    if buffer_option_count == True:
      a = [x for x in a if x != 'op1']
      a = [x for x in a if x != 'op2']
      a = [x for x in a if x != '']
      buffer = a[0]
      if buffer == '*':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = first_term * second_term
        print(
          '{} * {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)
      if buffer == '+':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = first_term + second_term
        print(
          '{} + {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)
      if buffer == '-':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = first_term - second_term
        print(
          '{} - {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)
      if buffer == '/':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = (first_term / second_term)
        print(
          '{} / {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)

      if buffer == '+':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = first_term + second_term
        print(
          '{} + {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)
      if buffer == '-':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = first_term - second_term
        print(
          '{} - {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)
      if buffer == '/':
        first_term = float(option_count[0])
        second_term = float(option_count[1])
        ready_calculation = (first_term / second_term)
        print(
          '{} / {} ='.format(float(option_count[0]), float(option_count[1])),
          ' %.3f' % ready_calculation)

    if len(a) == 2 and a[0] == 'sin':
      angle = int(a[1])
      sine = math.sin(math.radians(angle))
      print("sine of {} is {}".format(angle, sine))
      print("line {}".format(len(checker)), "syntax: valid")


    elif len(a) == 2 and a[0] == 'cos':
      angle = int(a[1])
      cosine = math.cos(math.radians(angle))
      print("cosine of {} is {}".format(angle, cosine))
    elif len(a) == 3 and a[0] == 'exp':
      base = int(a[1])
      exponent = int(a[2])
      print(a[1], "raised to", a[2], "is", base ** exponent)
    elif len(a) == 3 and a[0] == 'rot':
      root = math.sqrt(int(a[1]))
      print("the square root is", root)


    elif len(a) > 3 and operation_validator == False:
      new_list = []
      for g in a:
        element = g
        a = list(string.ascii_lowercase)
        for p in a:
          element = element.replace(p, "")
        new_list.append(element)

      for x in new_list.copy():
        if x == '':
          new_list.remove(x)
      parentheses_validator = False
      list_count = []
      for i in new_list:
        list_count.append(i)
      if list_count[2] == '+':
        first_term = float(list_count[0])
        second_term = float(list_count[1])
        print(
          '{} + {} ='.format(float(list_count[0]), float(list_count[1])),
          ' %.3f' % (first_term + second_term))

      if list_count[2] == '-':
        first_term = float(list_count[0])
        second_term = float(list_count[1])
        print(
          '{} - {} ='.format(float(list_count[0]), float(list_count[1])),
          ' %.3f' % (first_term - second_term))
      if list_count[2] == '*':
        first_term = float(list_count[0])
        second_term = float(list_count[1])
        print(
          '{} * {} ='.format(float(list_count[0]), float(list_count[1])),
          ' %.3f' % (first_term * second_term))
      if list_count[2] == '/':
        first_term = float(list_count[0])
        second_term = float(list_count[1])
        print(
          '{} / {} ='.format(float(list_count[0]), float(list_count[1])),
          ' %.3f' % (first_term / second_term))

  print("--------------")

for i in ready_list:
  print(f" {i} ")