import os

def main():
    while True:
        print("\nSimple File Manager")
        print("1. List Files")
        print("2. Create Directory")
        print("3. Delete File")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_files()
        elif choice == "2":
            create_directory()
        elif choice == "3":
            delete_file()
        elif choice == "4":
            print("Exiting the file manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def list_files():
    print("\nList of files in the current directory:")
    files = os.listdir('.')
    for file in files:
        print(file)

def create_directory():
    directory_name = input("\nEnter the name of the new directory: ")
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Error: Directory '{directory_name}' already exists.")

def delete_file():
    file_name = input("\nEnter the name of the file to delete: ")
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except PermissionError:
        print(f"Error: Permission denied. Cannot delete '{file_name}'.")

if __name__ == '__main__':
    main()
