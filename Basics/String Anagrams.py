
def checking_anagrams(string1, string2):
    # Remove spaces and convert to lowercase
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    
    # Sort the characters of both strings
    return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    if checking_anagrams(str1, str2):
        print(f'"{str1}" and "{str2}" are anagrams.')
    else:
        print(f'"{str1}" and "{str2}" are not anagrams.')
