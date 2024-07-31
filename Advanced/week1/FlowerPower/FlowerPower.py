print("Iris flower classifier")
print("----------------------\n")

isRunning = True

while isRunning:
   length = float(input("Enter petal length: "))#Collects an input as a float
   width = float(input("Enter petal width: "))
   if length < 2.5:
        print("Iris classification is Setosa\n")
   elif length >= 2.5 and width <1.9:
      print("Iris classification is Versicolor\n")
   elif length >= 2.5 and width >= 1.9:
      print("Iris classification is Virginica\n")
   else:
      print("An Error Occured Please Try Again")
   while True:
    shouldContinue = input("Classify another? (y)es or (n)o: ")#checks wether the user wants to continue or quit the program
    if shouldContinue == "n":
      isRunning = False
      break
    elif shouldContinue == "y":
       break
    else:
      print("Please respond with either (y)es or (n)o.\n")
