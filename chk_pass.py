import re

in_chk_pass = input("Enter your password: ")


def check_password(in_chk_pass):
    my_pass = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    chk_pass = re.compile(my_pass)
    validation_res = "valid" if chk_pass.fullmatch(in_chk_pass) else "not valid"
    print(in_chk_pass, validation_res)


check_password(in_chk_pass)