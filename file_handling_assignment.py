# file_handling_assignment.py

def file_creation():
    try:
        # Creating a new text file in write mode
        with open("my_file.txt", 'w') as file:
            file.write("This is line 1.\n")
            file.write("The number is 42.\n")
            file.write("This is the third line.\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def file_reading():
    try:
        # Reading the content of the file and displaying it
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("Reading the content of 'my_file.txt':\n")
            print(content)
    except FileNotFoundError:
        print("File not found. Please make sure 'my_file.txt' exists.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def file_appending():
    try:
        # Appending additional lines to the file
        with open("my_file.txt", 'a') as file:
            file.write("Appending line 4.\n")
            file.write("Appending the number 84.\n")
            file.write("Appending the final line.\n")
        print("Content appended successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")

def main():
    try:
        file_creation()
        file_reading()
        file_appending()
        # Reading the content again to display the appended lines
        file_reading()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File handling operations completed.")

if __name__ == "__main__":
    main()
