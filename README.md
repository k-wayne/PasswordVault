# PasswordVault
Application that manages our passwords through vault  technique and  generates new passwords for the user to use in different log in scenarios.

## Description
PasswordVault is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviours that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./main.py** | Choose an option: new-Create Account, log-Log In, esc-Exit |
| Display prompt for creating an account | **Enter: new** | Enter your first name, last name and password |
| Exit application | **Enter: esc** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Techs Used:
* python3.6
* pip
* pyperclip


## Running the Application
* To run the application, in your terminal:

        $ chmod +x main.py
        $ ./main.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 test_credential.py
        $ python3.6 user_test.py
        
## Technologies Used
* Python3.6
* IDE

## License
Licensed under the [MIT License](LICENSE)

[k-wayne]
2019  <https://github.com/k-wayne/PasswordVault>
