def count_characters(string):
          char_count={}
          if not isinstance(string,str):
                    raise TypeError("Input must be a string.")
          if not string:
                    raise ValueError("Input string cannot be empty.")
          
          for char in string:
                    if char in char_count:
                       char_count[char]+=1
                    else:
                          char_count[char]=1
          print(char_count)

if __name__=="__main__":
          user_input=input("Enter a string: ")
          try:
            count_characters(user_input)
          except (TypeError, ValueError) as e:
            print(f"Error: {e}")
          except Exception as e:
            print(f"An unexpected error occurred: {e}")