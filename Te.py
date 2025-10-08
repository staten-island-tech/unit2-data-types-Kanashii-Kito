def parking_spacesAnyDay(x, y):
    y_Car_OccupiedSpace = 0
    y_Empty_notOccupied_Space = 0
    for car in x:
        if car == "C":
            y_Car_OccupiedSpace += 1
        elif car == ".":
            y_Empty_notOccupied_Space += 1
    




    t_Car_OccupiedSpace = 0
    t_Empty_notOccupied_Space = 0
    for car in y:
        if car == "C":
            t_Car_OccupiedSpace += 1
        elif car == ".":
            t_Empty_notOccupied_Space += 1
    
    print(y_Car_OccupiedSpace, y_Empty_notOccupied_Space)
    print(t_Car_OccupiedSpace, t_Empty_notOccupied_Space)

    parking_spacesAnyDay("CCC..", "C.C.C.")

    print(str(y_Car_OccupiedSpace-t_Car_OccupiedSpace))

