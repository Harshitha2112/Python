def remove_duplicates(num:list)->list:
    new_list=[]
    if not isinstance(num,list):
        raise TypeError("Input must be a list of numbers.")
    if not num:
          raise ValueError("Input list cannot be empty.")
    
    for i in num:
        if i not in new_list:
            new_list.append(i)
    return new_list

if __name__=="__main__":
      num=input("Enter a list of numbers separated by spaces: ").split()
      num_list=[int(i) for i in num]
      try:
        result=remove_duplicates(num_list)
      except (TypeError, ValueError) as e:
          print(f"Error: {e}")
      except Exception as e:
          print(f"An unexpected error occurred: {e}")
      else:
          print("Duplicates removed successfully:",result)