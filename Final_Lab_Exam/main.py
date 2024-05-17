from Utils.user_manager import UserManager

def main():
    user_manager = UserManager()

    while True:
        try:
            print ("="*60)
            print ("\t       Welcome to the Dice Roll Game!")
            print ("="*60)
            print ("\n       1. Register")
            print ("       2. Login")
            print ("       3. Exit")
            
            choice = input ("\n  Enter your choice: ")
            print("="*60)

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