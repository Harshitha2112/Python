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
    result=remove_duplicates(num_list)
    print(f"the list after removing duplicates is {result}")