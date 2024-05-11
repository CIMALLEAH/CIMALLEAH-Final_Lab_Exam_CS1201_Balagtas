def main():
    print ("Welcome to the Dice Roll Game ")
    print ("1. Register")
    print ("2. Login")
    print ("3. Exit")

    while True:
        try:
            choice = input ("Enter your choice: ")

            if choice == '1':
                pass

            elif choice == '2':
                pass

            elif choice == '3':
                break

            else:
                raise ValueError
        
        except ValueError as e:
            print (f"Invalid choice. Please try again.{e}")

if __name__ == "__main__":
    main()
