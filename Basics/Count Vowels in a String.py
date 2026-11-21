def count_vowels(string:str)->int:
          #validate input is a string
          if not isinstance(string,str):
                                raise TypeError("Input must be a string")
          #string should not be empty
          if not string:
                                raise ValueError("Input string cannot be empty")
          else:
                         #convert string into lower case and remove spaces
                         string = string.lower().strip()
                         #count the number of vowels in the string
                         vowels = "aeiou"
                         count = 0
                         for char in string:
                              if char in vowels:
                                  count += 1
                         return count


if __name__ == "__main__":
          try:
                    string = input("enter a string to count the number of vowels: ")
                    vowel_count = count_vowels(string)
                    print(f"The number of vowels in the string is: {vowel_count}")
          except (TypeError,ValueError) as e:
                    print(e)
          except Exception as e:
                    print("Something went wrong",e)