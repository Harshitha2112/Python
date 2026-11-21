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
                user_input=input("enter a number")
                #validate and convert input to integer
                if not user_input.strip().isdigit():
                        raise TypeError("Input must be digit(no letters,string,float)")
                number=int(user_input)
                #calling the function
                if is_prime_number(number):
                        print(f"{number} is a prime number")
                else:
                        print(f"{number} is not a prime number")
        except (TypeError,ValueError) as e:
                print(e)
        except Exception as e:
                print("Something went wrong",e)


