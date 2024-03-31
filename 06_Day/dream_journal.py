


import json

def add_dream_entry():
    date = input("Enter the date of the dream (YYYY-MM-DD): ")
    description = input("Describe your dream: ")
    tags = input("Enter tags (comma-separated): ").split(',')
    
    entry = {
        'date': date,
        'description': description,
        'tags': tags
    }
    
    # Save the entry to a file
    with open('dreams.json', 'a') as file:
        json.dump(entry, file)
        file.write('\n')

def view_dream_entries():
    with open('dreams.json', 'r') as file:
        for line in file:
            entry = json.loads(line)
            print(f"Date: {entry['date']}")
            print(f"Description: {entry['description']}")
            print(f"Tags: {', '.join(entry['tags'])}")
            print()

# Main program loop
while True:
    print("1. Add Dream Entry")
    print("2. View Dream Entries")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_dream_entry()
    elif choice == '2':
        view_dream_entries()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
