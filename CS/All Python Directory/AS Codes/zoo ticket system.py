design="-------------------------------------------------------------------------------------------"
arr=[500,500,500,500,500,500,500]
def out():
    print(design)
    print("                                    Menu             ")
    print(design)
    print("1- Monday ","2- Tuesday ","3- Wednesday ","4- Thursday ","5- Friday ","6- Saturday ","7- Sunday")
    print("Enter * when Entering tickets to return to main menu")
    print(design)

for count in range(0,100,1):
    out()

    if(arr[0]==0 and arr[1]==0 and arr[2]==0 and arr[3]==0 and arr[4]==0 and arr[5]==0 and arr[6]==0):
        print("All Days Are Booked")
        print(design)
        break
    else:
        print("Tickets → Monday:",arr[0]," Tuesday:",arr[1]," Wednesday:",arr[2]," Thursday:",arr[3]," Friday:",arr[4]," Saturday:",arr[5]," Sunday:",arr[6])
        print(design)
        day=input("Enter Number Of Day: ")
        print(design)
                                                                                        # Main Code
        if(day=="1"):
            if(arr[0]==0):
                print("Select Another Day, This Day is Booked")

            else:
                print("---------------------Monday---------------------")
                tickets=input("Enter Number Of Tickets You Want To Purchase: ")
                if(tickets=="*"):
                    continue
                else:
                    if (int(tickets) > arr[0]):
                        print(design)
                        print("Re Enter tickets")
                        continue
                    else:
                        arr[0]=arr[0]-int(tickets)
                        print("Available Reservations:",arr[0])
                        continue



        else:
            if(day=="2"):
                if (arr[1] == 0):
                    print("Select Another Day, This Day is Booked")
                    continue
                else:
                    print("---------------------Tuesday---------------------")
                    tickets = input("Enter Number Of Tickets You Want To Purchase: ")
                    if (tickets == "*"):
                        continue
                    else:
                        if (int(tickets) > arr[1]):
                            print(design)
                            print("Re Enter tickets")
                            continue
                        else:
                            arr[1] = arr[1] - int(tickets)
                            print("Available Reservations:", arr[1])
                            continue
            else:
                if (day == "3"):
                    if (arr[2] == 0):
                        print("Select Another Day, This Day is Booked")
                        continue
                    else:
                        print("---------------------Wednesday---------------------")
                        tickets =input("Enter Number Of Tickets You Want To Purchase: ")
                        if (tickets == "*"):
                            continue
                        else:
                            if (int(tickets) > arr[2]):
                                print(design)
                                print("Re Enter tickets")
                                continue
                            else:
                                arr[2] = arr[2] - int(tickets)
                                print("Available Reservations:", arr[2])
                                continue
                else:
                    if (day == "4"):
                        if (arr[3] == 0):
                            print("Select Another Day, This Day is Booked")
                            continue
                        else:
                            print("---------------------Thursday---------------------")
                            tickets =input("Enter Number Of Tickets You Want To Purchase: ")
                            if (tickets == "*"):
                                continue
                            else:
                                if (int(tickets) > arr[3]):
                                    print(design)
                                    print("Re Enter tickets")
                                    continue
                                else:
                                    arr[3] = arr[3] - int(tickets)
                                    print("Available Reservations:", arr[3])
                                    continue
                    else:
                        if (day == "5"):
                            if (arr[4] == 0):
                                print("Select Another Day, This Day is Booked")
                                continue
                            else:
                                print("---------------------Friday---------------------")
                                tickets = input("Enter Number Of Tickets You Want To Purchase: ")
                                if (tickets == "*"):
                                    continue
                                else:
                                    if (int(tickets) > arr[4]):
                                        print(design)
                                        print("Re Enter tickets")
                                        continue
                                    else:
                                        arr[4] = arr[4] - int(tickets)
                                        print("Available Reservations:", arr[4])
                                        continue
                        else:
                            if (day == "6"):
                                if (arr[5] == 0):
                                    print("Select Another Day, This Day is Booked")
                                    continue
                                else:
                                    print("---------------------Saturday---------------------")
                                    tickets = input("Enter Number Of Tickets You Want To Purchase: ")
                                    if (tickets == "*"):
                                        continue
                                    else:
                                        if (int(tickets) > arr[5]):
                                            print(design)
                                            print("Re Enter tickets")
                                            continue
                                        else:
                                            arr[5] = arr[5] - int(tickets)
                                            print("Available Reservations:", arr[5])
                                            continue
                            else:
                                if (day == "7"):
                                    if (arr[6] == 0):
                                        print("Select Another Day, This Day is Booked")
                                        continue
                                    else:
                                        print("---------------------Sunday---------------------")
                                        tickets = input("Enter Number Of Tickets You Want To Purchase: ")
                                        if (tickets == "*"):
                                            continue
                                        else:
                                            if (int(tickets) > arr[6]):
                                                print(design)
                                                print("Re Enter tickets")
                                                continue
                                            else:
                                                arr[6] = arr[6] - int(tickets)
                                                print("Available Reservations:", arr[6])
                                                continue
                                else:
                                    print("Re-enter Number Of Days")
                                    continue

