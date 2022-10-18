import datetime
import Print
import main


# User UI Method
def userUI():
    """
    Function that creates and controls the UI for the user to interface with the program.

    Big-O: O(1)
    """

    # Initial menu display for the program. (main menu)
    print(
        "***************************************\n"
        "1. Print All Package Status and Total Mileage\n"
        "2. Get a Single Package Status with ID\n"
        "3. Get Package Status with a Time\n"
        "4. Get a Single Package Status with a Time\n"
        "5. Exit the Program\n"
        "***************************************\n"
    )

    # User input variable (user_input) used for initial selection.
    user_input = input(">>> ")

    try:

        # --------------------------------------------------------------------------------------------------------------

        # When the user selects the 1st option in the main menu.
        if user_input == "1":
            Print.printAllPackages(main.package_hash_table)
            print("\n___TOTAL DISTANCE___")
            print("\t%i MILES" % int(
                main.truck_1.getDistance() + main.truck_1.getDistance() + main.truck_1.getDistance()))

            # --------------------------------------------------------------------------------------------------------------

        # When the user selects the 2nd option in the main menu.
        elif user_input == "2":

            # Menu options are shown in the log.
            print("Please input the package ID you would like to select:\n"
                  "\tInput B to go Back\n"
                  "\tInput X to Exit\n")

            # User selection put to a lowercase for continuity no matter what case.
            user_input = input(">>> ").lower()
            if user_input.isdigit():
                Print.printPackageWithId(int(user_input), main.package_hash_table)
            else:
                if user_input == "b":
                    userUI()
                elif user_input == "x":
                    exit()

        # --------------------------------------------------------------------------------------------------------------

        # When the user selects the 3rd option in the main menu.
        elif user_input == "3":

            # Menu options are shown in the log.
            print("Please input the time you would like to view (In Military Time - hh:mm):\n"
                  "\tInput B to go Back\n"
                  "\tInput X to Exit\n")

            # This grabs the user input for either the package ID or the other menu options.
            user_input = input(">>>  ".lower())

            if user_input.isalpha():
                # If the user inputs the letter b.
                if user_input == "b":
                    # Restart the method back at the top level.
                    userUI()

                # If the user inputs the letter x.
                elif user_input == "x":
                    # Exit the program.
                    exit()
            else:
                # Gets the user input for the time they want to see the status of the package.

                # Splits up the input for the time into hours (hh) and minutes (mm).
                colon = user_input.find(":")
                hh = user_input[0:colon]
                mm = user_input[colon + 1:]

                # Checks to see if the time is the appropriate range and size
                if (len(hh) > 2 or len(mm) > 2) or (int(hh) > 24 or int(mm) >= 60):
                    print("Please Input a Correct Time.\n\n")
                    userUI()
                else:
                    time_input = datetime.timedelta(hours=(float(hh)), minutes=(float(mm)))
                    Print.printAllPackageWithTime(time_input, main.package_hash_table)

        # --------------------------------------------------------------------------------------------------------------

        # When the user selects the 4th option in the main menu.
        elif user_input == "4":
            # Menu options are shown in the log.
            print("Please input the package ID you would like to select followed by the time:\n"
                  "\tInput B to go Back\n"
                  "\tInput X to Exit\n")

            # This grabs the user input for either the package ID or the other menu options.
            user_input_package = input("Package ID (From 1 to 40) or Other Menu Options >>> ").lower()

            # If the user inputs the letter b.
            if user_input_package == "b":
                # Restart the method back at the top level.
                userUI()

            # If the user inputs the letter x.
            elif user_input_package == "x":
                # Exit the program.
                exit()

            # Gets the user input for the time they want to see the status of the package.
            user_input_time = input("Time (In Military Time - hh:mm) >>> ")

            # Splits up the input for the time into hours (hh) and minutes (mm).
            colon = user_input_time.find(":")
            hh = user_input_time[0:colon]
            mm = user_input_time[colon + 1:]

            if (len(hh) > 2 or len(mm) > 2) or (int(hh) > 24 or int(mm) >= 60):
                print("Please input correct time.")
            else:
                time_input = datetime.timedelta(hours=(float(hh)), minutes=(float(mm)))
                print(time_input)
                if int(user_input_package) > 40 or int(user_input_package) < 0:
                    print("Please input correct package ID.")
                else:
                    Print.printPackageWithIdAndTime(int(user_input_package), time_input, main.package_hash_table)

        # --------------------------------------------------------------------------------------------------------------

        # When the user selects the 5th option in the main menu.
        elif user_input == "5":

            # The program exits.
            exit()

        # --------------------------------------------------------------------------------------------------------------
        else:

            # If there is an error in any of the selection it raises an exception.
            raise Exception("Number selected out of range!")
    except Exception:
        # When an invalid selection exception is made this is output and the method is rerun.
        print("\nPlease select a number or letter listed.\n")
        userUI()


userUI()
