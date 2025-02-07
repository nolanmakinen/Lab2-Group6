# Nolan Makinen
# Princess Okerulu
# reading_list.py
# 2025-02-04
# A program that can store, delete and search information about a reading list.

import csv
import os

CSV_FILENAME = 'books.csv'

# Function to add a book to the reading list
def add_book(title, author, year):
    # Check for missing fields
    if not title.strip() or not author.strip() or not year.strip():
        print("Error: Title, Author, and Year cannot be empty.")
        return

    # Validate year is an integer
    try:
        int_year = int(year)
    except ValueError:
        print("Error: Year must be a valid year.")
        return

    # Check if file exists; if not, write header
    file_exists = os.path.isfile(CSV_FILENAME)

    # Check for duplicate book before adding
    if file_exists:
        try:
            with open(CSV_FILENAME, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    if row and row[0].lower() == title.lower() and row[1].lower() == author.lower():
                        print("Error: This book already exists in the reading list.")
                        return
        except OSError as e:
            print(f"Error: Could not read from file '{CSV_FILENAME}'.\n{e}")
            return

    try:
        with open(CSV_FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            # If file didn't exist before, write a header first
            if not file_exists:
                writer.writerow(["Title", "Author", "Year"])
            writer.writerow([title, author, int_year])
        print(f'Book "{title}" added successfully.')
    except OSError as e:
        print(f"Error: Could not write to file '{CSV_FILENAME}'.\n{e}")

# Function to delete a book from the reading list
def delete_book(title):
    if not title.strip():
        print("Error: Title cannot be empty.")
        return

    # If the file doesn't exist, there's nothing to delete
    if not os.path.isfile(CSV_FILENAME):
        print(f"Error: File '{CSV_FILENAME}' does not exist. Nothing to delete.")
        return

    books = []
    found = False

    try:
        # Read existing books, excluding the one to be deleted
        with open(CSV_FILENAME, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header:  # If there's a header, keep it
                books.append(header)

            for row in reader:
                # Compare case-insensitively for the title
                if row[0].lower() != title.lower():
                    books.append(row)
                else:
                    found = True
    except OSError as e:
        print(f"Error: Could not read from file '{CSV_FILENAME}'.\n{e}")
        return

    if found:
        # Write the updated list back to the CSV file
        try:
            with open(CSV_FILENAME, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(books)
            print(f'Book "{title}" deleted successfully.')
        except OSError as e:
            print(f"Error: Could not write to file '{CSV_FILENAME}'.\n{e}")
    else:
        print(f'Book "{title}" not found in the list.')

# Function to list all books
def list_books():
    # If file doesn't exist or is empty, print a message
    if not os.path.isfile(CSV_FILENAME):
        print(f"No books found (file '{CSV_FILENAME}' does not exist).")
        return

    try:
        with open(CSV_FILENAME, mode='r') as file:
            reader = csv.reader(file)
            # Attempt to read the header
            header = next(reader, None)
            # If there's no header or no data, then there are no books
            if not header:
                print("No books found in the list.")
                return

            # If file only has a header row but no data
            data_found = False
            for row in reader:
                data_found = True
                print(f'Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
            if not data_found:
                print("No books found in the list.")

    except OSError as e:
        print(f"Error: Could not read from file '{CSV_FILENAME}'.\n{e}")

# Function to search for a book by title
def search_book(title):
    if not title.strip():
        print("Error: Title cannot be empty.")
        return

    # If file doesn't exist, we have nothing to search
    if not os.path.isfile(CSV_FILENAME):
        print(f"No books found (file '{CSV_FILENAME}' does not exist).")
        return

    try:
        with open(CSV_FILENAME, mode='r') as file:
            reader = csv.reader(file)
            # Skip the header
            next(reader, None)
            for row in reader:
                if row and row[0].lower() == title.lower():
                    print(f'Found: Title: {row[0]}, Author: {row[1]}, Year: {row[2]}')
                    return
        print('Book not found.')
    except OSError as e:
        print(f"Error: Could not read from file '{CSV_FILENAME}'.\n{e}")

# Menu loop
def menu():
    while True:
        print("\n1. Add Book\n2. List Books\n3. Search Book\n4. Delete Book\n5. Quit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter year of publication: ")
            add_book(title, author, year)
        elif choice == '2':
            list_books()
        elif choice == '3':
            title = input("Enter book title to search: ")
            search_book(title)
        elif choice == '4':
            title = input("Enter book title to delete: ")
            delete_book(title)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()
else:
    print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    menu()