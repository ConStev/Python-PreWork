# # Question 1:
# # Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 

def hello_name(user_name):
  print(f""" "hello_{user_name}!" """)


print(hello_name("USERNAME"))

# # Question 2:
# # Write a python function, first_odds that prints the odd numbers from 1-100 
# # and returns nothing:

def first_odds():
  print(list(range(1,100,2)))

first_odds()

# # # Question 3:
# # # Please write a Python function, max_num_in_list to return the max number
# # # of a given list. 

def max_num_in_list(a_list):
  print(max(a_list))

numbers = (1,2,3,4,5)

max_num_in_list(numbers)

# # # Question 4:
# # # Write a function to return if the given year is a leap year. 
# # #A leap year is divisible by 4, but not divisible by 100,
# # # unless it is also divisible by 400. The return should be a boolean Type
# # # (true/false)

def is_leap_year(a_year):
  if a_year % 4 == 0:
    return True
  if a_year % 100 == 0:
    return False
  if a_year % 400 == 0:
    return True
  else:
    return False

print(is_leap_year(2000))
print(is_leap_year(1992))
print(is_leap_year(1515))

# # Question 5:
# # Write a function to check to see if all numbers in list are consecutive numbers.
# # For example, [2,3,4,5,6,7] are consecutive numbers, but[1,2,4,5] are not
# # consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
  if sorted(a_list) == list(range(min(a_list), max(a_list)+1)):
    return True
  else:
    return False
  

list1 = (2,3,4,5,6,7)
list2 = (1,2,4,5)

print(is_consecutive(list1))
print(is_consecutive(list2))
