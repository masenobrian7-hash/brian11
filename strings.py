"""
NAME: MASENO BRIAN
DATE: 20-02-2026
REG NO : AIIM/01440/2024

Description: 1.reversing a string using two methods
             2. counting character frequency in a string
             
"""

#reversing a string using slicing
def reverse_slicing(text):
    return text[::-1]  #means start from the end and move backwards

#reversing a string using a loop
def reverse_loop(text): #means go through each character in the string and add it to the front of the reversed_text variable
    reversed_text = ""
    for char in text: #this slowly builds the reversed version of the string by adding each character to the front of the reversed_text variable
        reversed_text = char + reversed_text
    return reversed_text

#counting character frequency in a string
def count_frequency(text): #means go through each character in the string and count its occurrences
    frequency = {}
    frequency = {}
    for char in text: # if character already exists in the frequency dictionary add 1.
        if char in frequency:
            frequency[char] += 1
        else:                    #otherwise, initialize the count for that character to 1.
            frequency[char] = 1
    return frequency



#MAIN PROGRAM

def main():
    # ask use for input
    user_text = input("Enter a string: ")
    print ("Reversed string (slicing):", reverse_slicing(user_text))
    print ("Reversed string (loop):", reverse_loop(user_text))
    print ("Character frequency:", count_frequency(user_text))

# ask if the user wants case sensitivity

choice = input("do you want case sensitivity? (Y/N):")
case_sensitive = choice.upper() == "Y"
if case_sensitive:
    user_text = input("Enter a string: ")
    main()
else:
    user_text = input("Enter a string: ")
    user_text = user_text.lower() # convert the input to lowercase to ignore case sensitivity
    print ("Reversed string (slicing):", reverse_slicing(user_text))
    print ("Reversed string (loop):", reverse_loop(user_text))
    print ("Character frequency:", count_frequency(user_text))

# count characters using the users choice of case sensitivity
freq = count_frequency(user_text)
print("character frequency:", freq)

#sort alphabetically
sort_choice = input("Do you want to sort alphabetically? (Y/N): ")
if sort_choice.upper() == "Y":
    sorted_freq = dict(sorted(freq.items())) # sort the frequency dictionary alphabetically by key (character)
    print("Sorted character frequency:", sorted_freq)

# table header
print("\nCharacter | Frequency")
for char, freq in freq.items():
    print(f"{char}         | {freq}")

# total characters
print("\nTotal characters:" , len(user_text))

#run the main program
main()

