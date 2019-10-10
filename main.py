#!/usr/bin/env python3.6
from user import User
from credential import Credentials

#USER MODULE
#create user
def create_user(fname, lname, uname, phone, email, passw):
    new_user = User(fname, lname, uname, phone, email, passw)
    return new_user

#saving users
def user_create(user):
    user.user_create()

#show users
def user_show():
    return User.user_show()

#passcode generator
def passcode_generate():
    return User.passcode_generate()

#CREDENTIALS MODULE

#create credential new
def create_credential(apname, acname, psname):
    new_credential = Credentials(apname, acname, psname)
    return new_credential

##saving credentials
def credential_create(credentials):
    credentials.credential_create()

#remove a credential
def credential_remove(credentials):
    credentials.credential_remove()

#search for App
def search_name(credentials):
    return Credentials.search_name(credentials)

#Duplicate search
def search_duplicate(appname):
    return Credentials.search_duplicate(appname)

#show credentials
def credentials_show():
    return Credentials.credentials_show()

#Main App
def main():
    print("Hello! This is PasswordVault bot application.\n Use these short codes: \n new - create an account using your own password \n ran - create an account using a randomly generated  password \n esc - exit the application")
    short_code = input().lower()
    while True:

        if short_code == 'new':
            print("Use your own passcode to generate your account")
            print("."*60)

            print("First Name "+" "*5 +"_"*30)
            f_name = input()

            print("Last Name "+" "*5 + "_"*30)
            l_name = input()

            print("User Name " + " "*5 + "_"*30)
            u_name = input()

            print("Phone Number " + " "*5 + "_"*30)
            p_number = input()

            print("Email " + " "*5 + "_"*30)
            e_address = input()

            print("Password " + " "*5 + "_"*30)
            p_word = input()

            #def to save acc
            user_create(create_user(f_name, l_name, u_name,
                                  p_number, e_address, p_word))
            print('\n')
            print(f"{u_name} account has been successfully created!")
            print('\n')
            print(
                "Use shortcodes to continue: \n log - login into account \n esc - to exit")
            short_codetwo = input().lower()
            if short_codetwo == 'log':
                print("-"*10)
                print("LogIn")
                print("-"*10)
                print("Input your Username then input Passcode")

                print("Username")
                user_namein = input()

                print("Passcode")
                pass_wordin = input()

                #validation of acc
                if user_namein == u_name and pass_wordin == p_word:
                    print("Success!!. \n Use shortcodes to continue: \n new - create a new credential \n show - display your credentials \n find - to find a credential by inputing the name \n del - to delete a credential \n esc - exit the application")
                    short_codethree = input().lower()
                    if short_codethree == 'new':
                        print("-"*10)
                        print("Create new credentials.")
                        print("-"*10)

                        print("App Name")
                        appli_name = input()

                        print("Account Name")
                        acc_name = input()

                        print("Passcode")
                        pass_name = input()

                        #def new credential
                        credential_create(create_credential(appli_name, acc_name, pass_name))
                        print('\n')
                        print("-"*10)
                        print(f"New Credential for {appli_name} created.")
                        print('\n')
                        print("-"*10)
                        continue

                    elif short_codethree == 'show':
                        if credentials_show():
                            print("The list of all your contacts below:")
                            print('\n')

                            for credentials in credentials_show():
                                print(
                                    f"{credentials.appli_name} {credentials.acc_name} {credentials.pass_name}")
                                print('\n')
                        else:
                            print('\n')
                            print(
                                "You do not seem to have any credentials saved yet.")
                            print('\n')
                    elif short_codethree == 'find':
                        print(
                            "Enter the App Name you are looking for.")

                        search_applicationname = input()
                        if search_duplicate(search_applicationname):
                            search_credential = search_name(
                                search_applicationname)
                            print(
                                f"{search_applicationname.appli_name} {search_applicationname.acc_name} {search_applicationname.pass_name}")
                        else:
                            print("Oops fatal error: non-existant.")
                else:
                    print("Try again.")

            elif short_codetwo == 'esc':
                print("Come back soon")
                break
            else:
                print("Try again"+"."*10)

        elif short_code == 'ran':
            print("To create an account with random password")
            print("-"*10)

            print("First Name " + " "*5 + "_"*30)
            f_name = input()

            print("Last Name " + " "*5 + "_"*30)
            l_name = input()

            print("User Name " + " "*5 + "_"*30)
            u_name = input()

            print("Phone Number " + " "*5 + "_"*30)
            p_number = input()

            print("Email " + " "*5 + "_"*30)
            e_address = input()

            print("Password " + " "*5 + "_"*30)
            p_word = input()
            

            #def save acc
            user_create(create_user(f_name, l_name, u_name,p_number, e_address, p_word))
            print('\n')
            print(f"{u_name} has been created!")
            print('\n')
            print(
                "Use the shortcodes to navigate: \n log - login into account \n esc - to exit the application")
            short_codetwo = input().lower()
            if short_codetwo == 'log':
                print("-"*10)
                print("LogIn")
                print("-"*10)
                print("Enter your Username and Passcode")

                print("UserName")
                user_namein = input()

                print("Passcode")
                pass_wordin = input()

                #validate acc
                if user_namein == u_name and pass_wordin == p_word:
                    print("Correct username and password.\n To proceed use the following shortcodes: \n new - To generate a new credential \n show - To show credentials \n find - to Search a credential by inputing the App name \n del - To remove a credential \n esc - To exit the application")
                    short_codethree = input().lower()
                    if short_codethree == 'new':
                        print("-"*10)
                        print("Follow instructions.")
                        print("-"*10)

                        print("Application Name")
                        appli_name = input()

                        print("Account Name")
                        acc_name = input()

                        print("Passcode")
                        pass_name = input()

                        #create credentials
                        credential_create(create_credential(appli_name, acc_name, pass_name))
                        print('\n')
                        print("-"*10)
                        print(f"New Credential for {appli_name} created.")
                        print('\n')
                        print("-"*10)
                        continue

                    elif short_codethree == 'show':
                        if credentials_show():
                            print("Showing lists of contacts....")
                            print('\n')

                            for credentials in credentials_show():
                                print(
                                    f"{credentials.appli_name} {credentials.acc_name} {credentials.pass_name}")
                                print('\n')
                        else:
                            print('\n')
                            print(
                                "Non-existant credentials.")
                            print('\n')
                    elif short_codethree == 'find':
                        print(
                            "Type in App name.")

                        search_applicationname = input()
                        if search_duplicate(search_applicationname):
                            search_credential = search_name(
                                search_applicationname)
                            print(
                                f"{search_applicationname.appli_name} {search_applicationname.acc_name} {search_applicationname.pass_name}")
                        else:
                            print("That credential doesnot exist.")
                else:
                    print("Fatal error. Try Again.")

            elif short_codetwo == 'esc':
                print("Come back soon!")
                break
            else:
                print("Make  use of the shortcodes")

        elif short_code == "esc":
            print("Come back soon!")
            break
        else:
            print("Make  use of the shortcodes")


if __name__ == '__main__':

    main()
