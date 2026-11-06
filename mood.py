name=input("Hi! Please enter your name:")
mood=input("How is your mood Today??Happy/sad/annoyed/tired:")
energy=int(input("Enter Your energy level of today(1-10):"))
if energy<=3:
    print("Warning! Energy level low. Eat or drink something you like, rest and drink water.")
    show="Warning! Energy level low. Eat or drink something you like, rest and drink water."

if energy<=5:
    print("That's low. Keep yourself hydrated and maybe do something you like, or rest.")
    show="That's low. Keep yourself hydrated and maybe do something you like, or rest."
else:
    print("Usually normal! Keep your energy balanced, just like right now. Dont let it fall and if it does, dont panic and take rest!")
    show="Usually normal! Keep your energy balanced, just like right now. Dont let it fall and if it does, dont panic and take rest!"

if mood=="happy":
    print("happy:Amazing!Enjoy the rest of your day as well!!")
    advice="Amazing!Enjoy the rest of your day as well!!"
elif mood=="sad":
    print("sad:Try sharing something with someone that might make you feel better and do something you like.")
    advice="sad:Try sharing something with someone that might make you feel better and do something you like."
elif mood=="annoyed":
    print("annoyed:Try to think and do something that you like to or would love to.")
    advice="annoyed:Try to think and do something that you like to or would love to."
elif mood=="tired":
    print("tired:Take rest and drink lots of water.")
    advice="tired:Take rest and drink lots of water."

import datetime
time=datetime.datetime.now()

print("\nSummary:")
print("Name:",name)
print("date and time:",time)
print("Energy level-",energy,":",show)
print("Mood-",mood,":",advice)
