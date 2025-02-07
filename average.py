length = len(number_list)
def calc_average(number_list):
average = total / length
number_list = [int(x) for x in input("Enter a few numbers (seperated by a space): ").split() if x != " "]  # This will just make a list with whatever the use inputs. Don't worry about it
total = sum(number_list)
print(average)
return average
average = calc_average(number_list)
