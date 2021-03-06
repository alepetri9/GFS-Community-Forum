#GFS COMMUNITY FORUM
#Maria, Alessandra, Amelia

def intro():
  print("WELCOME TO THE GFS COMMUNITY FORUM")
  print("")
  print("Here are your topic options:")
  print("1: mental health")
  print("2: injustice")

def othermental():
  print("")
  print("Here are more specific discussion areas:")
  print("")
  print("1: sleep")
  print("2: stress")
  print("")
  print("If you'd like to submit information in the general mental health forum, simply hit the 'enter' key")
  mentalchoice()
  
def mentalchoice():
  print("")
  d = input("Which conversation would you like to join? ")
  d = d.lower()
  if d == "1" or d == "sleep":
    sleep()
    return()
  if d == "2" or d == "stress":
    stress()
    return()
  if d == "":
    mentalhealth()
    return()
  else:
    print("That is not a valid choice.")
    mentalchoice()

def sleep():
  print("")
  print("SLEEP FORUM")
  print("")
  print("* all statements will remain anonymous")
  print("* future users will see your statment (just not who wrote it)")
  print("* TO ENSURE ANONYMITY, DO NOT INCLUDE YOUR NAME")
  print("")
  print("Write about anything relating to sleep issues: ")
  print("")
  a = input()
  print("")
  with open('sleep.txt', 'a+') as f:
    f.write(a + '\n')
  print("Here are some things other people have said:")
  with open('sleep.txt', 'r') as f:
    print(f.read())
  ending()

def stress():
  print("")
  print("STRESS FORUM")
  print("")
  print("* all statements will remain anonymous")
  print("* future users will see your statment (just not who wrote it)")
  print("* TO ENSURE ANONYMITY, DO NOT INCLUDE YOUR NAME")
  print("")
  print("Write about anything relating to stress: ")
  print("")
  b = input()
  print("")
  with open('stress.txt', 'a+') as f:
    f.write(b + '\n')
  print("Here are some things other people have said:")
  print("")
  with open('stress.txt', 'r') as f:
    print(f.read())
  ending()


def mentalhealth():
  print("")
  print("MENTAL HEALTH FORUM")
  print("")
  print("* all statements will remain anonymous")
  print("* future users will see your statment (just not who wrote it)")
  print("* TO ENSURE ANONYMITY, DO NOT INCLUDE YOUR NAME")
  print("")
  print("Write about anything relating to mental health: ")
  print("")
  c = input()
  c = c.lower()
  print("")
  with open('mentalhealth.txt', 'a+') as f:
    f.write(c + '\n')
  print("Here are some things other people have said:")
  print("")
  with open('mentalhealth.txt', 'r') as f:
    print(f.read())
  ending()


################################# 

def otherinjustice():
  print("")
  print("Here are more specific discussion areas:")
  print("1: Sexism")
  print("2: Homophobia")
  print("3: Racism")
  print("")
  print("If you'd like to submit information in the general injustice forum, simply hit the 'enter' key")
  injustchoice()

def injustchoice():
  print("")
  d = input("Which conversation would you like to join? ")
  d = d.lower()
  if d=="1" or d=="sexism":
    sexism()
    return()
  if d=="2" or d=="homophobia":
    homophobia()
    return()
  if d =="3" or d == "racism":
    racism()
    return()
  if d=="":
    injustice()
    return()
  else:
    print("That is not a valid response.")
    injustchoice()

def sexism():
  print("")
  print("SEXISM FORUM")
  print("")
  print("* all statements will remain anonymous")
  print("* future users will see your statment (just not who wrote it)")
  print("* TO ENSURE ANONYMITY, DO NOT INCLUDE YOUR NAME")
  print("")
  print("Write any of your feelings, experiences, or questions surrounding sexism: ")
  print("")
  d = input()
  print("")
  with open('sexism.txt', 'a+') as f:
    f.write(d + '\n')
  print("Here are some things other people have said:")
  print("")
  with open('sexism.txt', 'r') as f:
    print(f.read())
  ending()

  
def homophobia():
  print("")
  print("HOMOPHOBIA FORUM")
  print("")
  print("* all statements will remain anonymous")
  print("* future users will see your statment (just not who wrote it)")
  print("* TO ENSURE ANONYMITY, DO NOT INCLUDE YOUR NAME")
  print("")
  print("Write any of your feelings, experiences, or questions surrounding homophobia: ")
  print("")
  e = input()
  print("")
  with open('homophobia.txt', 'a+') as f:
    f.write(e + '\n')
  print("Here are some things other people have said:")
  print("")
  with open('homophobia.txt', 'r') as f:
    print(f.read())
  ending()


def racism():
  print("")
  print("RACISM FORUM")
  print("")
  print("* all statements will remain anonymous")
  print("* future users will see your statment (just not who wrote it)")
  print("* TO ENSURE ANONYMITY, DO NOT INCLUDE YOUR NAME")
  print("")
  print("Write any of your feelings, experiences, or questions surrounding racism: ")
  print("")
  g = input()
  print("")
  with open('racism.txt', 'a+') as f:
    f.write(g + '\n')
  print("Here are some things other people have said:")
  print("")
  with open('racism.txt', 'r') as f:
    print(f.read())
  ending()


def injustice():
  print("")
  print("INJUSTICE FORUM")
  print("")
  print("* all statements will remain anonymous")
  print("* future users will see your statment (just not who wrote it)")
  print("* TO ENSURE ANONYMITY, DO NOT INCLUDE YOUR NAME")
  print("")
  print("Write any of your feelings, experiences, or questions surrounding injustice.")
  print("")
  h = input()
  print("")
  with open('injustice.txt', 'a+') as f:
    f.write(h + '\n')
  print("Here are some things other people have said:")
  print("")
  with open('injustice.txt', 'r') as f:
    print(f.read())
  ending()


#######################################

def ending():
  print("")
  print("Thank you for your input. Always remember that you are never alone in your endeavors, and your voice deserves to be heard.")
  print("")
  ending2()
  
def ending2():
  print("Would you like to submit another statement? If so, type 'yes'. If not, just hit the 'enter' key.")
  print("")
  z = input()
  z = z.lower()
  if z == "yes":
    print("- - - - - - - - - - - - - - - - - - - - - - -")
    main()
  if z == "":
    print("")
    print("Ciao")
    return()
  else:
    print("That answer is invalid. Please try again.")
    ending2()
 
#######################################

def main():
  intro()
  choice = input("Which forum would you like to enter? ")
  choice = choice.lower()
  if choice == "1" or choice == "mental health":
    othermental() 
  if choice=="2" or choice== "injustice":
    otherinjustice()
  else:
    print("That's not a valid input")
    print("")
    main()



main()