password= "secret123"
userpass = input("enter password: ")
userattempt = 1 # First attempt already made

while userpass != password:
    digitcount = 0
    for char in userpass:
        if char.isdigit():
            digitcount = digitcount + 1
    if len(userpass) < 8:
        print("Error: The password is too short.")
    if digitcount == 0:
        print("Error: Need a digit.")
    else:
        print("Access denied")
    if userattempt > 2:
        print("Retry Alert: you entered wrong password more than 2 times.")

    userpass = input("enter password: ")
    userattempt = userattempt + 1

print("Access granted")



