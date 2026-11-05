passenger=input("Enter Name here:")
flightcompany="Air Bharat"
ticketprice=20790
totalpassengers=int(input("Number of tickets booked:"))
ticketsavailable=True
destination="Vietnam"
print("Your name:",passenger)
print("Flight booked:",flightcompany,"Airbus 3019")
print("ticket price:",ticketprice)
print("Travelling to:",destination)
print("Number of seats in flight:",totalpassengers)
print("Are more tickets available?:",ticketsavailable)
print(type(passenger))
print(type(flightcompany))
print(type(ticketprice))
print(type(totalpassengers))
print(type(ticketsavailable))
totalearning=ticketprice * totalpassengers
discount=1200
print("Your total price is",totalearning)
print("Congrats!You get a discount of",discount*totalpassengers,"On the whole!")
print("You have to pay",totalearning-discount*totalpassengers)
oneticketwith50increasedanddividedby10=(ticketprice+50)/10
print("One ticket if its price is increased by 50 and then divided by 50",oneticketwith50increasedanddividedby10)

FinalDetails="You are goinng to"+destination
print(FinalDetails)
print("Is ticket price more than 25,000?",ticketprice>25,00)
print("Are number of passengers more than 3?",totalpassengers>3)
print("Name is more than 5 letters long",len(passenger)>5)
print("If we swap the money with 200 less")
print("Before swapping Original=20790 and new=",ticketprice-200)
Original=ticketprice
new=ticketprice-200
swap=Original
Original=new
new=swap
print("Now we can say that Original=",Original,"and new=",new)