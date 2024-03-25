design="-------------------------------------------"
times=int(input("How Many Times you want this program to run? : "))
times=times+1
for s in range(1,times,1):
    n1 = int(input("Enter Your First Number : "))
    n2 = int(input("Enter Your Second Number : "))
    n3 = int(input("Enter Your Third Number : "))
    n4 = int(input("Enter Your Fourth Number : "))
    n5 = int(input("Enter Your Fifth Number : "))
    if (n1 < n2):
        if (n1 < n3):
            if (n1 < n4):
                if (n1 < n5):
                    print("First Number:", n1, "is The Least")
                    print(design)
                else:
                    if (n5 < n2):
                        if (n5 < n3):
                            if (n5 < n4):
                                print("Fifth Number:", n5, "is The Least")
                                print(design)
                            else:
                                if (n4 < n3):
                                    if (n4 < n2):
                                        print("Fourth Number:", n4, "is The Least")
                                        print(design)
                                    else:
                                        if (n2 < n3):
                                            print("Second Number:", n2, "is The Least")
                                            print(design)
                                        else:
                                            print("Third Number:", n3, "is The Least")
                                            print(design)
                                else:
                                    if (n3 < n2):
                                        print("Third Number:", n3, "is The Least")
                                        print(design)
                                    else:
                                        print("Second Number:", n2, "is The Least")
                                        print(design)
                        else:
                            if (n3 < n2):
                                if (n3 < n4):
                                    print("Third Number:", n3, "is The Least")
                                    print(design)
                                else:
                                    if (n4 < n2):
                                        print("Fourth Number:", n4, "is The Least")
                                        print(design)
                                    else:
                                        print("Second Number:", n2, "is The Least")
                                        print(design)
                            else:
                                if (n2 < n4):
                                    print("Second Number:", n2, "is The Least")
                                    print(design)
                                else:
                                    print("Fourth Number:", n4, "is The Least")
                                    print(design)
                    else:
                        if (n2 < n3):
                            if (n2 < n4):
                                print("Second Number:", n2, "is The Least")
                                print(design)
                            else:
                                if (n4 < n3):
                                    print("Fourth Number:", n4, "is The Least")
                                    print(design)
                                else:
                                    print("Third Number:", n3, "is The Least")
                                    print(design)
                        else:
                            if (n3 < n4):
                                print("Third Number:", n3, "is The Least")
                                print(design)
                            else:
                                print("Fourth Number:", n4, "is The Least")
                                print(design)
            else:
                if (n4 < n2):
                    if (n4 < n3):
                        if (n4 < n5):
                            print("Fourth Number:", n4, "is The Least")
                            print(design)
                        else:
                            if (n5 < n2):
                                if (n5 < n3):
                                    print("Fifth Number:", n5, "is The Least")
                                    print(design)
                                else:
                                    if (n3 < n2):
                                        print("Third Number:", n3, "is The Least")
                                        print(design)
                                    else:
                                        print("Second Number:", n2, "is The Least")
                                        print(design)
                            else:
                                if (n2 < n3):
                                    print("Second Number:", n2, "is The Least")
                                    print(design)
                                else:
                                    print("Third Number:", n3, "is The Least")
                                    print(design)
                    else:
                        if (n3 < n2):
                            if (n3 < n5):
                                print("Third Number:", n3, "is The Least")
                                print(design)
                            else:
                                if (n5 < n2):
                                    print("Fifth Number:", n5, "is The Least")
                                    print(design)
                                else:
                                    print("second Number:", n2, "is The Least")
                                    print(design)
                        else:
                            if (n2 < n5):
                                print("Second Number:", n2, "is The Least")
                                print(design)
                            else:
                                print("Fifth Number:", n5, "is The Least")
                                print(design)
                else:
                    if (n2 < n3):
                        if (n2 < n5):
                            print("Second Number:", n2, "is The Least")
                            print(design)
                        else:
                            if (n3 < n5):
                                print("Third Number:", n3, "is The Least")
                                print(design)
                            else:
                                print("Fifth Number:", n5, "is The Least")
                                print(design)
                    else:
                        if (n3 < n5):
                            print("Third Number:", n3, "is The Least")
                            print(design)
                        else:
                            print("Fifth Number:", n5, "is The Least")
                            print(design)
        else:
            if (n3 < n2):
                if (n3 < n4):
                    if (n3 < n5):
                        print("Third Number:", n3, "is The Least")
                        print(design)
                    else:
                        if (n5 < n4):
                            if (n5 < n2):
                                print("Fifth Number:", n5, "is The Least")
                                print(design)
                            else:
                                if (n2 < n4):
                                    print("Second Number:", n2, "is The Least")
                                    print(design)
                                else:
                                    print("Fourth Number:", n4, "is The Least")
                                    print(design)
                        else:
                            if (n4 < n2):
                                print("Fourth Number:", n4, "is The Least")
                                print(design)
                            else:
                                print("Second Number:", n2, "is The Least")
                                print(design)
                else:
                    if (n4 < n2):
                        if (n4 < n5):
                            print("Fourth Number:", n4, "is The Least")
                            print(design)
                        else:
                            if (n5 < n2):
                                print("Fifth Number:", n5, "is The Least")
                                print(design)
                            else:
                                print("Second Number:", n2, "is The Least")
                                print(design)
                    else:
                        if (n2 < n5):
                            print("Second Number:", n2, "is The Least")
                            print(design)
                        else:
                            print("Fifth Number:", n5, "is The Least")
                            print(design)
    else:
        if (n2 < n3):
            if (n2 < n4):
                if (n2 < n5):
                    print("Second Number:", n2, "is The Least")
                    print(design)
                else:
                    if (n5 < n4):
                        if (n5 < n3):
                            print("Fifth Number:", n5, "is The Least")
                            print(design)
                        else:
                            if (n3 < n4):
                                print("Third Number:", n3, "is The Least")
                                print(design)
                            else:
                                print("Fourth Number:", n4, "is The Least")
                                print(design)
                    else:
                        if (n4 < n3):
                            print("Fourth Number:", n4, "is The Least")
                            print(design)
                        else:
                            print("Third Number:", n3, "is The Least")
                            print(design)
            else:
                if (n4 < n3):
                    if (n4 < n5):
                        print("Fourth Number:", n4, "is The Least")
                        print(design)
                    else:
                        if (n5 < n3):
                            print("Fifth Number:", n5, "is The Least")
                            print(design)
                        else:
                            print("Third Number:", n3, "is The Least")
                            print(design)
                else:
                    if (n3 < n5):
                        print("Third Number:", n3, "is The Least")
                        print(design)
                    else:
                        print("Fifth Number:", n5, "is The Least")
                        print(design)
        else:
            if (n3 < n4):
                if (n3 < n5):
                    print("Third Number:", n3, "is The Least")
                    print(design)
                else:
                    if (n5 < n4):
                        print("Fifth Number:", n5, "is The Least")
                        print(design)
                    else:
                        print("Fourth Number:", n4, "is The Least")
                        print(design)
            else:
                if (n4 < n5):
                    print("Fourth Number:", n4, "is The Least")
                    print(design)
                else:
                    print("Fifth Number:", n5, "is The Least")
                    print(design)








