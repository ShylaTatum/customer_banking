
# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = input("Enter savings balance: ")
    savings_interest = input("Enter interest rate as annual interest rate: ")
    savings_maturity = input("Enter the number of months the account will accumulate: ")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"After {savings_maturity} months, you will have earned {interest_earned:.2f}, and your new balance will be {updated_savings_balance:.2f}. ")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input("Enter CD starting balance: ")
    cd_interest = input("Enter CD interest rate as the annual interest rate: ")
    cd_maturity = input("Enter the numbers of months the account will accumulate: " )

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your account will earned {interest_earned:.2f} and be worth {updated_cd_balance:.2f} after {cd_maturity} months.")

if __name__ == "__main__":
    # Call the main function.
    main()