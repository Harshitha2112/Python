def is_palindrome(string:str)->bool:
        #validate input is a string
        if not isinstance(string,str):
                          raise TypeError("Input must be a string")
        #string should not be empty
        if not string:
                          raise ValueError("Input string cannot be empty")
        else:
                     #convert string into lower case and remove spaces
                     string = string.lower().strip()
                     #check whether the string is palindrome or not
                     reversed_string = ""
                     for i in string:
                        reversed_string = i + reversed_string
                     return string == reversed_string
                              
                     
if __name__ == "__main__":
          try:
                    string = input("enter a word to check whether it is palindrome or not: ")
                    if is_palindrome(string):
                              print(f"{string} is a palindrome")
                    else:
                             print(f"{string} is not a palindrome")
          except (TypeError,ValueError) as e:
                    print(e)
          except Exception as e:
                    print("Something went wrong",e)
                    