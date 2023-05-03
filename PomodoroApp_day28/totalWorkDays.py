from datetime import date , datetime


def howManyReps(reps, work, Break):
    todaysDate = datetime.now()
    file = open("TotalWork.txt", 'a')
    file.write(f"Date {todaysDate} Total Work {reps} and each rep consists of {work} mintues work and {Break}"
               f"minutes break\n\n")
    file.close()
