from colorama import Fore, Style, init,Back

# Initialize Colorama
init()

# Print colored text
print(Fore.RED + "hi" )
print("hello")

print(Fore.BLUE + "hi" , Style.RESET_ALL)

print(Back.BLUE + "hi" , Style.RESET_ALL)
