def find_largest_number(numbers_list):
    largest=0
    # validate that input is a list
    if not isinstance(numbers_list,list):
        raise TypeError("Input must be a list of numbers.")
    #validate if the list is empty
    if not numbers_list:
          raise ValueError("Input list cannot be empty.")
    else: 
        for number in numbers_list:
                if number > largest:
                    largest = number
        return largest
        


if __name__ == "__main__":
    numbers=input("Enter a list of numbers separated by spaces: ")
    numbers_list=[int(num) for num in numbers.split()]
    largest = find_largest_number(numbers_list)
    print("The largest number in the list is:", largest)
    