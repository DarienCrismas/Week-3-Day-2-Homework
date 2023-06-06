#Exercise 2 - 
#Write a Python class which has two methods get_String and print_String. 
#get_String accept a string from the user and print_String print the string in upper case

class Exercise_2():
    def get_String(self):
        self.user_input = input("String please? ")
    def print_String(self):
        print(self.user_input.upper())

test = Exercise_2()
test.get_String()
test.print_String()