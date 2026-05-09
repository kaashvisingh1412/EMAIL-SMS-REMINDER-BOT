import time

print("======================================")
print("      EMAIL/SMS REMINDER BOT")
print("======================================\n")

while True:

    print("1. Set a Reminder")
    print("2. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("\nEnter your name: ")

        reminder = input("Enter your reminder message: ")

        seconds = input("Enter reminder time in seconds: ")

        if not seconds.isdigit():
            print("\nInvalid input! Please enter numbers only.\n")
            continue

        seconds = int(seconds)

        print("\n======================================")
        print("Reminder Details")
        print("======================================")
        print("Name:", name)
        print("Message:", reminder)
        print("Reminder Time:", seconds, "seconds")
        print("======================================\n")

        print("Reminder has been set successfully!")
        print("Waiting for reminder time...\n")

        time.sleep(seconds)

        print("======================================")
        print("          REMINDER ALERT")
        print("======================================")
        print("Hello", name + "!")
        print("Reminder Message:", reminder)
        print("======================================\n")

        another = input("Do you want to set another reminder? (yes/no): ").lower()

        if another == "no":
            print("\nThank you for using Reminder Bot!")
            break

        elif another != "yes":
            print("\nInvalid choice. Program closed.")
            break

    elif choice == "2":
        print("\nProgram exited successfully.")
        break

    else:
        print("\nInvalid choice! Please try again.\n")
