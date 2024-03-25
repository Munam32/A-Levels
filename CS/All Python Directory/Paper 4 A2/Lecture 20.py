Array2D = [["Ahmed", "Ali", "Bano"],["Qasim", "Faisal", "Khalid"]]

for rows in range(2):
    for column in range(3):
        if Array2D[rows][column] == "Faisal":
            print("Faisal is present")
            break


