#this is the main command line interface for the euromillions predictor

import fake_euromillions
import euromillions_counter



while True:
    print("main command line interface for euromillions predictor")
    print("1. Simulate random EuroMillions draws")
    print("2. Analyze past EuroMillions results")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        fake_euromillions.run_simulation()
    elif choice == '2':
        euromillions_counter.main()
    else:
        print("Invalid choice. Please enter 1 or 2.")


