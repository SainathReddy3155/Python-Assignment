
import re
import datetime
class Sainath_Assignment:
    #intializing initial method
    def __init__(self):
        print("starting application")
        self.loginattempts=0
        self.username=""
        self.password=""
        self.confirmpassword=""
        self.dob=""
        self.mobile=""
        user_input=input(" 1. Signup\n 2. Login \n 3. Exit application \n Please select an option : ")
        print(user_input)
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.login()
        elif user_input=="3":
            print("Thanks for using application")
            self.__init__()
        else:
            print("Invalid option please select a proper option")
            self.__init__()
    
    def signup(self):
        user_username=input(" Enter username : ")
        mobile_num=int(input(" Please enter Mobile Number \n "))
        #regex for mobile , password,dob
        mobile_regex=re.compile("[6-9]{1}[0-9]{9}$")
        password_regex=re.compile("[a-zA-Z0-9[@#$%*&()!^]")
        dob_regex=re.compile("(0[1-9]|[1-2][0-9]|3[0-1])[-\/](0[1-9]|1[0-2])[-\/](19|20)\d{2}$")
        if len(str(mobile_num))==10 and mobile_regex.match(str(mobile_num)):
            password=input(" Please enter password : \n ")
            if len(password)>=8 and password_regex.match(password):
                confirm_password=input("Confirm your password : ")
                #checking password and confirm password are same or not
                if password==confirm_password:
                    dob_input=input("Enter your date of birth : ")
                    if dob_regex.match(dob_input):
                        #finding year in dob
                        year_regex="\d{4}$"
                        year=re.findall(year_regex, dob_input)[0]
                        #getting present year 
                        current_year=datetime.datetime.now().year
                        age=int(current_year)-int(year)
                        if age>18:
                            self.username=user_username
                            self.password=password
                            self.dob=dob_input
                            self.mobile=mobile_num
                            print("Registered successfully")
                            self.login()
                        else:
                            print("Age is less then 18")
                            self.signup()
                    else:
                        print("invalid date of birth")
                        self.signup()
                else:
                    print("Password's doesn't match")
                    self.signup()
            else:
                print("Password should contain 8 characters,special character and a number")
                self.signup()        
        else:
            print("Invalid number")
            self.signup()
            
    def login(self):
        print("Welcome to Login page ")
        user_name=input("Enter your username : ")
        user_password=input("Enter your password : ")
        if user_name==self.username and user_password==self.password:
            if self.loginattempts<=3:
                self.loginattempts+=1
                flag=True
                while flag:
                    print("Welcome to home page {} ".format(self.username))
                    after_login_options=input("1. Press 1 to change your password \n2. Signout\n")       
                    if after_login_options=='1':
                        result=self.change_password()
                        print(result)
                    elif after_login_options=='2':
                        print("Successfully logout Thanks for using application")
                        flag=False
                        self.login()
                    else:
                        print("Please select valid options")           
            else:
                print("You have excceded login attempts ")
                self.login()
        else:
            print("Invalid credentials")
            self.login()
            
    def change_password(self):
        password_regex=re.compile("[a-zA-Z0-9[@#$%*&()!^]")
        user_password=input("Enter your new password : ")
        if user_password!=self.password:
            if len(user_password)>=8 and password_regex.match(user_password):
                self.password=user_password
                return "Password updated successfully"
            else:
                return "Password should contain 8 characters,special character and a number"
        else:
            return "Old password cannot be same as new password"
        
#declaring obj for class
obj=Sainath_Assignment()
obj
