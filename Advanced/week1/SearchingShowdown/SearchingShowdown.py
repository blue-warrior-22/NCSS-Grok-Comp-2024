def linear_search(num):
  # perform linear search on num and return number_or_guesses taken
  lin_guess = 1
  while True:
    if lin_guess == num:
      return lin_guess
    lin_guess+=1

def binary_search(num):
  # perform binary search on num and return number_or_guesses taken
  min_num = 1
  max_num = 100
  # get the middle value and round to an integer
  middle = round((max_num + min_num) / 2)
  bin_guess=1
  while True:
    if num > middle:
        min_num = middle + 1
    elif num < middle:
        max_num = middle - 1
    else:
      if bin_guess == 1:
        return bin_guess
      else: return bin_guess - 1
    middle = round((max_num + min_num) / 2)
    bin_guess+=1

def calculate_winner():
    # calculate the % of times each search wins and the overall winner!
    binary_count = 0
    linear_count = 0
    equal = 0
    for i in range(1,101):
      a=binary_search(i)
      b=linear_search(i)
      if a>b:
        linear_count+=1
      elif b>a:
        binary_count+=1
      else:
        equal+=1
    # return counts for binary, linear and equal to main program
    return binary_count, linear_count, equal

if __name__ == '__main__':
  # print all your output and results beneath this line
  print("Search showdown")
  print("---------------")
  print()
  # call calculate_winner here
  binary_result, linear_result, equal = calculate_winner()
  # print results
  print(f"Binary search was quickest {binary_result}% of the time.")
  print(f"Linear search was quickest {linear_result}% of the time.")
  print(f"Both searches took the same number of guesses {equal}% of the time.")
  print()
  if binary_result > linear_result:
    print("Binary search wins!!!!")
  elif binary_result < linear_result:
    print("Linear search wins!!!!")
  else:print("It's a tie!!!!")
