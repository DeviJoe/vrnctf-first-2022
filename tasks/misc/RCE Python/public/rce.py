from subprocess import call

print("Enter your name:")

user_name = input()
call("echo " + user_name, shell=True)
