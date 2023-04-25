# Digital Companion Software Live Demonstration (S.J.G.R. 1.0)

# Code needed for plotting
import os
import numpy as np
import matplotlib.pyplot as plt
import random 
# Welcome part
def welcome():
    #Welcome message
    def welcome_message():
        print("Welcome to S.J.G.R. 1.0!")
    # Welcom Menu options
    def welcome_menu():
        print("Which menu would you like to view?")
        print("1. Health Menu")
        print("2. To Do List Menu")
        print("3. To Exit")
    welcome_message()
    welcome_menu()
# Health Menu 
def health(): #Done
    def health_menu():
        print("Which would you like to view?")
        print("1. Heart Rate")
        print("2. Oxygen Level Tracker")
        print("3. Sleep Cycle Tracker")
        print("4. Body Temperature")
        print("5. To Do List Menu")
        print("6. To Exit")
    def heart_rate(): 
       #Data
        BPM = []
        time = ["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]

        #entering data into list
        for i in range(0, 25):
            BPM.append(random.randint(70, 110))
        x = np.array(time)
        y = np.array(BPM)
        plt.figure()
        plt.plot(x,y)
        plt.title('Heart Rate Tracker')
        plt.xlabel('Time')
        plt.ylabel('Beats Per Minute')
        plt.show()
    def oxygen_level():
        #Data
        bloodOxygenLevels = []
        time = ["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]

        #entering data into list
        for i in range(0, 25):
            bloodOxygenLevels.append(random.randint(95, 100))
        x = np.array(time)
        y = np.array(bloodOxygenLevels)
        plt.figure()
        plt.plot(x,y)
        plt.title('Blood Oxygen Rate Tracker')
        plt.xlabel('Time')
        plt.ylabel('Levels (%)')
        plt.show() 
    def sleep_cycle(): 
        # Data
        hoursData = [6, 7, 8, 3, 10, 7, 5]
        days = ["Sun.","Mon.", "Tues.", "Wed.", "Thur.", "Fri.", "Sat."]
        sleepGoalDaily = 8
        sleepAverageDaily = 0

        #Calculating the data
        for i in hoursData:
            sleepAverageDaily += i
        sleepAverageDaily /= len(hoursData)
        x = np.array([0,1,2,3,4,5,6])
        y = np.array(hoursData)

        # Plotting the data for daily sleep
        plt.figure()
        plt.xticks(x, days)
        plt.plot(x, y)
        plt.text(0, 9.7, ('Daily Sleep Goal:', sleepGoalDaily), fontsize = 8, color = 'b')
        plt.text(0, 10, ('Average Hours of Sleep:', (round(sleepAverageDaily,1))), fontsize = 8, color = 'b')
        if sleepAverageDaily >= sleepGoalDaily:
            plt.text(0, 9.4, "Daily Sleep Goal was met", fontsize = 8, color = 'b')
        else:
            plt.text(0, 9.4, "(Daily Sleep Goal was not met)", fontsize = 8, color = 'b')
        plt.title('Daily Sleep Cycle Tracker')
        plt.xlabel('Days')
        plt.ylabel('Hours')
        plt.show()
    def body_temperature(): 
        #Data
        temperature = []
        time = ["0:00", "1:00", "2:00", "3:00", "4:00", "5:00", "6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00", "24:00"]

        #entering data into list
        for i in range(0, 25):
            temperature.append(random.randint(97, 99))

        x = np.array(time)
        y = np.array(temperature)
        plt.figure()
        plt.plot(x,y)
        plt.title('Body Temperature Tracker')
        plt.xlabel('Time')
        plt.ylabel('Temperature (F)')
        plt.show()

    health_menu()
    health_menu_option = int(input(""))
    if (health_menu_option == 1):
        heart_rate()
    elif(health_menu_option == 2):
        oxygen_level()
    elif(health_menu_option == 3):
        sleep_cycle()
    elif(health_menu_option == 4):
        body_temperature()
    elif(health_menu_option == 5):
        to_do_list()
    elif(health_menu_option == 6):
        quit_program()
# To Do List Menu
def to_do_list():
    path = "C://Users//thecl//Downloads//DigitalCompanionGroup//Task//"
    path_list = os.listdir(path)
    def to_do_list_menu():
        print("1. Add a new task")
        print("2. Add a new list")
        print("3. View lists")
        print("4. Health Menu")
        print("5. To Exit")
    def add_new_task():
        print("Existing lists:")
        for i in path_list:
            print(i)
        inp = input("\nWhat is the name of the task you would like to add?")
        inp2 = input("\nWhich list would you like to add it to?")
        f = open((path + inp2 + ".txt"), "a")
        f.write("\n")
        f.write(inp)
        f.close()
    def add_new_list():
        path = "C://Users//thecl//Downloads//DigitalCompanionGroup//Task//"
        inp = input("What would you like to name your new list?")
        f = open((path + inp + ".txt"), "x")   
    def view_list():
        path = "C://Users//thecl//Downloads//DigitalCompanionGroup//Task//"
        path_list = os.listdir(path)
        print("Task lists:")
        for i in path_list:
            print(i)
        print("Would you like to view items in the list? (Y for Yes, N for No)")
        list_item_view = input("")
        if list_item_view == ('y' or 'Y'):
            print("Which list would you like to view?")
            list_view = input()
            viewing = open((path + list_view + ".txt"), "r")
            print(viewing.read())
        elif list_item_view == ('n' or 'N'):
            pass

    to_do_list_menu()
    to_do_list_menu_option = int(input(""))
    if(to_do_list_menu_option == 1):
        add_new_task()
    elif(to_do_list_menu_option == 2):
        add_new_list()
    elif(to_do_list_menu_option == 3):
        view_list()
    elif(to_do_list_menu_option == 4):
        health()
    elif(to_do_list_menu_option == 5):
        quit_program()
# Exiting out of the program
def quit_program():
    print("\nGoodbye!")
    exit()
#Main method
def main():
    while(1):
        welcome()
        welcome_option = int(input())
        if(welcome_option == 1): # if Health Menu option is selected
            health()
        elif(welcome_option == 2): #if To Do List Menu option is selected
            to_do_list()
        elif (welcome_option == 3):
            quit_program()
if __name__ == "__main__":
    main()