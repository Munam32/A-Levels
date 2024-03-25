design="x-----------------Bus Ticketing System-----------------x"
design_2="------------------------------------------------------"
total_seats=45
cost=5.00
reservations=0
print(design)
print("Total Seats Available:",total_seats,"  ""Total Reservations:","0")
print("Each Ticket Cost: $",cost)
for count in range(0,100,1):
    print(design_2)
    tickets=int(input("Enter Number Of Tickets You Want To Purchase: "))
    print(design_2)
    if(tickets<=0):
        print("Type Again")
        continue
    else:
        if (total_seats <= 0):
            print("Reservations Complete")
            break
        reservations = reservations + tickets
        total_seats = total_seats - tickets
        if(tickets<=10):
            print("Total Seats Available:",total_seats,"  Total Reservations:",reservations)
            print("No Free Seat...",end=" ")
            print("Your bill: $",cost*tickets)
        elif(tickets<=20):
            print("Total Seats Available:", total_seats, "  Total Reservations:", reservations)
            print("1 free seat...", end=" ")
            print("Your bill: $", cost*(tickets-1))
        elif(tickets<=30):
            print("Total Seats Available:", total_seats, "  Total Reservations:", reservations)
            print("2 free seats...", end=" ")
            print("Your bill: $",cost*(tickets-2))
        else:
            if(tickets<=45):
                print("Total Seats Available:", total_seats, "  Total Reservations:", reservations)
                print("3 free seats...", end=" ")
                print("Your bill: $", cost * (tickets - 3))
    print(design_2)
    cancel=input("Enter * to terminate: ")
    if(cancel=="*"):
        break
























