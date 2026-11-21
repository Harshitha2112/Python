def finding_second_largest_number(nums:list[int])->int:
          #validate input is a list
          if not isinstance(nums,list):
                    raise TypeError("Input must be a list of numbers.")
          
          #validate if the list is empty
          if not nums:
                    raise ValueError("Input list cannot be empty.")
          
          #validate that all elements in the list are integers
          if any(not isinstance(current_num,int) for current_num in nums):
                  raise TypeError("All elements in the list must be integers.")
          
          #validate if the list has atleast 2 elements
          if len(nums)<2:
                    raise ValueError("Input list must have atleast 2 elements.")
          else:
                    largest = second_largest = float('-inf')
          for number in nums:
                    if number > largest:
                              second_largest = largest
                              largest = number
                    elif largest > number > second_largest:
                              second_largest = number
          return second_largest

if __name__=="__main__":
        numbers=input("Enter a list of numbers separated by spaces: ")
        numbers_list = [int(num) for num in numbers.split() ] 
        print(f"The second largest number is: {finding_second_largest_number(numbers_list)}")