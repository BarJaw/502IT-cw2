class System():
    @staticmethod
    def main():
        while True:
            System.view_menu()
    
    @staticmethod
    def view_menu():
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("\033[94mChoose an option: \033[0m")

        if choice == "1":
            auth_system.register()
        elif choice == "2":
            auth_system.login()
        elif choice == "3":
            exit(1)
        else:
            print("\033[91m=== Invalid choice. Please choose again\033[0m")

    


if __name__ == '__main__':
    System.main()
    
    