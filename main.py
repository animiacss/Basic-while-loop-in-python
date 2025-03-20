attemps = 0

while attemps < 3:
   stored_login = "LuizAnimia"
   stored_password = "humbledXD"
   
   tryed_login = str(input("login:"))
   tryed_password = str(input("password:"))
   
   if tryed_login == stored_login and tryed_password == tryed_password :
      print("You're now logged in your account.")
      break
   else :
      attemps += 1
      print("Login or password incorrect, you has",3 - attemps , "attemps left")

print("This account now is blocked")
