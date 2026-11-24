def sum_of_digits(n:int) ->int:
          #validate input is an integer
          if not isinstance(n,int):
                  raise TypeError("input must be an integer")
          if n<0:
                  raise ValueError("input must be a positive integer")
          total=0
          while n>0:
                  number=n%10
                  total+=number
                  n=n//10
          return total


if __name__=="__main__":
        number=int(input("Enter a positive integer: "))
        result=sum_of_digits(number)
        print(f"the sum of digits of {number} is {result}")