def max_and_min(numbers:list)-> tuple:
          """
          This function takes a list of numbers as input and returns a tuple containing the maximum and minimum values from the list.
          
          Parameters:
          numbers (list): A list of numbers.
          
          Returns:
          tuple: A tuple containing the maximum and minimum values.
          """
          if not isinstance(numbers,list):
                  raise TypeError("Input must be a list.")
          
          if not numbers:
                    raise ValueError("The list is empty.")
          
          max_value = numbers[0]
          min_value = numbers[0]
          
          for num in numbers:
                  if num>max_value:
                          max_value=num
                  if num<min_value:
                          min_value=num                    

          return (max_value, min_value)


if __name__ == "__main__":
          try:
                    numbers = input("Enter a list of numbers separated by spaces: ")
                    number_list = [float(num) for num in numbers.split()]
                    
                    max_min_tuple = max_and_min(number_list)
                    print(f"The maximum value is: {max_min_tuple[0]}")
                    print(f"The minimum value is: {max_min_tuple[1]}")
          except ValueError as ve:
                    print(f"ValueError: {ve}")
          except TypeError as te:
                    print(f"TypeError: {te}")
          except Exception as e:
                    print(f"An error occurred: {e}")