def is_prime_number(number):
          #validate input an integer
          if not isinstance(number,int):
                  raise TypeError("input must be an integer")
          #number should be atleast 2
          if number<2:
                  raise ValueError("prime numbers are greater than or equal to 2")
          for i in range(2,int(number**0.5)+1):
                  if number % i == 0:
                          return False
                          break
          else:
                    return True


if __name__ == "__main__":
        try:
                #taking input from the user
                lower_limit=input("enter the lower limit of the range: ")
                upper_limit=input("enter the upper limit of the range: ")
                #validate and convert input to integer
                if not lower_limit.strip().isdigit() or not upper_limit.strip().isdigit():
                        raise TypeError("Input must be digits(no letters,string,float)")
                lower=int(lower_limit)
                upper=int(upper_limit)
                #calling the function
                prime_numbers = []
                for num in range(lower, upper + 1):
                        if is_prime_number(num):
                                prime_numbers.append(num)
                print(f"Prime numbers between {lower} and {upper} are: {prime_numbers}")
        except (TypeError,ValueError) as e:
                print(e)
        except Exception as e:
                print("Something went wrong",e)


