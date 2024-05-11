from Utils.user_manager import UserManager

def main():
    user_manager = UserManager()

    while True:
        try:
            print ("Welcome to the Dice Roll Game!")
            print (" 1. Register")
            print (" 2. Login")
            print (" 3. Exit")
            
            choice = input ("\nEnter your choice: ")

            if choice == '1':
                user_manager.register()

            elif choice == '2':
                user_manager.login()

            elif choice == '3':
                break

            else:
                raise ValueError
        
        except ValueError as e:
            print (f"\nInvalid choice. Please try again.{e}")

if __name__ == "__main__":
    main()