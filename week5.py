try:
    # Create a new file "my_file.txt" in write mode
    with open('my_file.txt', 'w') as my_file:
        # Write at least three lines of text to the file, including a mix of strings and numbers
        my_file.write('Hello, World!\n')
        my_file.write('This is a line of text.\n')
        my_file.write('12345\n')

    # Read the contents of "my_file.txt" and display them on the console
    with open('my_file.txt', 'r') as my_file:
        print(my_file.read())

    # Open "my_file.txt" in append mode
    with open('my_file.txt', 'a') as my_file:
        # Append three additional lines of text to the existing content
        my_file.write('This is a new line of text.\n')
        my_file.write('This is another line of text.\n')
        my_file.write('67890\n')

    # Read the contents of "my_file.txt" and display them on the console
    with open('my_file.txt', 'r') as my_file:
        print(my_file.read())

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("Permission denied.")

except:
    print("An error occurred.")

finally:
    print("File handling completed.")