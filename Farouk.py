# Simple Greeting App
def main():
    print("Welcome to the Super Basic Python App!")
    print("-------------------------------------")
    
    # Get user input
    name = input("What's your name? ")
    
    # Greet the user
    print(f"\nHello, {name}! Thanks for trying this basic app.")
    print("This app doesn't do much, but it's a starting point!")
    
    # Simple interaction
    favorite_color = input("\nWhat's your favorite color? ")
    print(f"{favorite_color} is a great color!")

if __name__ == "__main__":
    main()
