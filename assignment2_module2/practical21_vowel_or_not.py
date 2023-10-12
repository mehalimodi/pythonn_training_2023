character = input("Enter a character: ")   
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  
  
if character in vowels:    # Check whether the input is a vowel or not 
    print(f"The character '{character}' is a vowel!")  
else:  
    print(f"The character '{character}' is a consonant!")  