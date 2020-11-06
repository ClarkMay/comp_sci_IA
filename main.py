from tkinter import *

#Global Variables
global points
points = 0
global assists
assists = 0
global rebounds
rebounds = 0
global steals
steals = 0
global fouls
fouls = 0
global fieldGoalsMade
fieldGoalsMade = 0
global fieldGoalsShot
fieldGoalsShot = 0
global fieldGoalPercentage
fieldGoalPercentage = 0
global fieldGoalPercentageRounded
fieldGoalPercentageRounded = 0
global threePointersMade
threePointersMade = 0
global threePointersShot
threePointersShot = 0
global roundedThreePointFieldGoalPercentage
roundedThreePointFieldGoalPercentage = 0
global freeThrowsMade
freeThrowsMade = 0
global freeThrowsTaken
freeThrowsTaken = 0
global freeThrowPercentageRounded
freeThrowPercentageRounded = 0
global playerStatistics
playerStatistics = [[]]
global buttonPress
buttonPress=False
global k
k = 1
global playerCount
playerCount = 0

master = Tk()
newWindow = Tk()

master.title("Bearkats Stat Tracker")
master.geometry("1920x1080")
master.configure(background="gray30")

def gameWindow():
    multiGuiGenerator()
    teamScores()
    master.deiconify() #Makes Game Window Reappear
    newWindow.destroy()

playerList = [] #Empty Player List

def mainWindow():
    master.withdraw() #Hides Root Window That Is Created
    newWindow.title("New Window")
    newWindow.geometry("480x270")
    newWindow.configure(background="gray30")
    global k
    if buttonPress == True: #Changes Player Name & Label Numbers
        k += 1
        str(k)
        players = playerInput.get()
        playerList.append(players) #adds players into the List
    playerInput.delete(0, 'end') #clears Entry Box
    Button(newWindow, text='Insert Player ' + str(k), bg="black", command=buttonPressTrue, fg="white", highlightbackground="gray90", activebackground="deep sky blue").place(x=130, y=60, height=33, width=150)
    Label(newWindow, text='Player ' + str(k) + " Name", bg="black", fg="white", highlightbackground="gray90").place(x=5, y=15, height=35, width=110)

playerInput = Entry(newWindow) #Input Box
playerInput.place(x=5, y=60, height=30, width=110)

def buttonPressTrue():
    global buttonPress
    buttonPress = True
    mainWindow()

Button(newWindow, text='Start Game', bg="black", command=gameWindow, fg="white", highlightbackground="gray90", activebackground="deep sky blue").place(x=130, y=120, height=33, width=150)

# playerStatistics
            #playerStatistics = [["Clark", 0, 5],
            #                    ["Bob", 0, 5]]

#Columns For Each Person
#Create Class
#Global Array
#class Players:
 #   def __init__(self, name, assists, rebounds):
  #      self.name = name
   #     self.assists = assists
    #    self.rebounds = rebounds

#p1 = Players("Clark", 0, 0)
#p2 = Players("Brooks", 7, 0)
#print(p1.assists)

#Player Statistics
def addAssist():
    global assists
    assists += 1
    str(assists)
    #str(assists) #convert to string so that I can use as text
    multiGuiGenerator() #redraws the Gui so that it can update in realtime

def addAssist1(column, row):
    global assists
    playerStatistics[column][row] = playerStatistics[column][row] + 1
    assists += 1
    str(assists) #convert to string so that I can use as text
    multiGuiGenerator() #redraws the Gui so that it can update in realtime

def subtractAssist():
    global assists
    assists -= 1
    multiGuiGenerator()

def addRebound():
    global rebounds
    rebounds += 1
    str(rebounds)
    multiGuiGenerator()

def subtractRebounds():
    global rebounds
    rebounds -= 1
    multiGuiGenerator()

def addSteals():
    global steals
    steals += 1
    str(steals)
    multiGuiGenerator()

def subtractSteals():
    global steals
    steals -= 1
    multiGuiGenerator()

def addFouls():
    global fouls
    fouls += 1
    str(fouls)
    multiGuiGenerator()

def subtractFouls():
    global fouls
    fouls -= 1
    multiGuiGenerator()

def fieldGoalMade():
    global points
    global fieldGoalsMade
    global fieldGoalsShot
    points += 2
    str(points)
    fieldGoalsMade += 1
    fieldGoalsShot += 1
    fieldGoalConverter()

def fieldGoalConverter():
    global fieldGoalsMade
    global fieldGoalsShot
    global fieldGoalPercentage
    global fieldGoalPercentageRounded
    fieldGoalPercentage = fieldGoalsMade/fieldGoalsShot
    fieldGoalPercentage *= 100
    fieldGoalPercentageRounded = round(fieldGoalPercentage, 2) #rounds FG Percentage to just 2 decimal places
    str(fieldGoalPercentage)
    multiGuiGenerator()

def threePointFieldGoalConverter():
    global threePointersMade
    global threePointersShot
    global fieldGoalPercentage
    global fieldGoalPercentageRounded
    global roundedThreePointFieldGoalPercentage
    threePointFieldGoalPercentage = threePointersMade/threePointersShot
    threePointFieldGoalPercentage *= 100
    roundedThreePointFieldGoalPercentage = round(threePointFieldGoalPercentage, 2)
    str(roundedThreePointFieldGoalPercentage)
    fieldGoalConverter()

def fieldGoalMissed():
    global fieldGoalsShot
    fieldGoalsShot += 1
    fieldGoalConverter()

def threePointerMade():
    global fieldGoalsMade
    global fieldGoalsShot
    global threePointersMade
    global threePointersShot
    global points
    points += 3
    threePointersMade += 1
    threePointersShot += 1
    fieldGoalsShot += 1
    fieldGoalsMade += 1
    threePointFieldGoalConverter()

def threePointerMissed():
    global threePointersShot
    global fieldGoalsShot
    fieldGoalsShot += 1
    threePointersShot += 1
    threePointFieldGoalConverter()

def freeThrowConverter():
    global freeThrowsMade
    global freeThrowsTaken
    global freeThrowPercentageRounded
    freeThrowPercentage = freeThrowsMade/freeThrowsTaken
    freeThrowPercentageRounded = round(freeThrowPercentage, 2)
    freeThrowPercentageRounded *= 100
    str(freeThrowPercentage)
    multiGuiGenerator()

def freeThrowMade():
    global points
    global freeThrowsMade
    global freeThrowsTaken
    points += 1
    freeThrowsMade += 1
    freeThrowsTaken += 1
    freeThrowConverter()

def freeThrowMissed():
    global freeThrowsTaken
    freeThrowsTaken += 1
    freeThrowConverter()

#def playerColumns():
    Label(master, text="Player Name", bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="solid",activebackground="deep sky blue").place(x = 5, y = 5, height = 30, width = 150)
    Label(master, text='Points: ' + str(points), anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 40, height = 30, width = 150)
    Label(master, text="Assists: " + str(assists), anchor = 'w', bg="white", fg="black", highlightbackground="gray90",borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 70, height = 30, width = 150)
    Button(master, text='+', bg="white", command=addAssist, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 115, y = 75, height = 15, width = 15) #Add Assists
    Button(master, text='-', bg="white", command=subtractAssist, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 130, y = 75, height = 15, width = 15) #Subtract Assists
    Label(master, text='Rebounds: ' + str(rebounds),anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 100, height = 30, width = 150)
    Button(master, text='+', bg="white", command=addRebound, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 115, y = 105, height = 15, width = 15) #Add Rebounds
    Button(master, text='-', bg="white", command=subtractRebounds, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 130, y = 105, height = 15, width = 15) #Subtract Rebounds
    Label(master, text='Steals: ' + str(steals), anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 130, height = 30, width = 150)
    Button(master, text='+', bg="white", command=addSteals, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 115, y = 135, height = 15, width = 15) #Add Steals
    Button(master, text='-', bg="white", command=subtractSteals, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 130, y = 135, height = 15, width = 15) #Subtract Steals
    Label(master, text='Fouls: ' + str(fouls), anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 160, height = 30, width = 150)
    Button(master, text='+', bg="white", command=addFouls, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 115, y = 165, height = 15, width = 15) #Add Foul
    Button(master, text='-', bg="white", command=subtractFouls, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 130, y = 165, height = 15, width = 15) #Subtract Fouls
    Label(master, text='Field Goal Percent: ' + str(fieldGoalPercentageRounded) + "%", anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 190, height = 30, width = 150)
    Label(master, text='3 Point FG Percent: ' + str(roundedThreePointFieldGoalPercentage) + "%", anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 220, height = 30, width = 150)
    Label(master, text='Free Throw Percent: ' + str(freeThrowPercentageRounded) + "%", anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 250, height = 30, width = 150)
    Button(master, text='FG Made', command=fieldGoalMade, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 280, height = 50, width =75)
    Button(master, text='FG Missed', command=fieldGoalMissed, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 80, y = 280, height = 50, width =75)
    Button(master, text='3PT Made', command=threePointerMade, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 330, height = 50, width =75)
    Button(master, text='3PT Missed', command=threePointerMissed, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 80, y = 330, height = 50, width =75)
    Button(master, text='FT Made', command=freeThrowMade, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5, y = 380, height = 50, width =75)
    Button(master, text='FT Missed', comman=freeThrowMissed, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 80, y = 380, height = 50, width =75)

def teamScores():
    Label(master, text="Bearkats: 0", bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="solid",
          activebackground="deep sky blue").place(x=880, y=5, height=30, width=150)
    Label(master, text="Visitors: 0", bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="solid",
          activebackground="deep sky blue").place(x=880, y=34, height=30, width=150)
    Button(master, text='+', bg="white", command=addAssist, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 995, y = 42, height = 15, width = 15) #Add Assists
    Button(master, text='-', bg="white", command=addAssist, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 1010, y = 42, height = 15, width = 15) #Add Assists

def multiGuiGenerator():
    playerCount = len(playerList)
    xCoordinate = 0
    yCoordinate = 150
    for j in range(0,playerCount):
        xCoordinate += 175 #Seperates each column
        Label(master, text=playerList[j], bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="solid",activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 5 + yCoordinate, height = 30, width = 150)
        Label(master, text='Points: ' + str(points), anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 40 + yCoordinate, height = 30, width = 150)
        Label(master, text="Assists: " + str(assists), anchor = 'w', bg="white", fg="black", highlightbackground="gray90",borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 70 + yCoordinate, height = 30, width = 150)
        Button(master, text='+', bg="white", command= addAssist, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 115 + xCoordinate, y = 75 + yCoordinate, height = 15, width = 15) #Add Assists
        Button(master, text='-', bg="white", command=subtractAssist, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 130 + xCoordinate, y = 75 + yCoordinate, height = 15, width = 15) #Subtract Assists
        Label(master, text='Rebounds: ' + str(rebounds),anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 100 + yCoordinate, height = 30, width = 150)
        Button(master, text='+', bg="white", command=addRebound, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 115 + xCoordinate, y = 105 + yCoordinate, height = 15, width = 15) #Add Rebounds
        Button(master, text='-', bg="white", command=subtractRebounds, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 130 + xCoordinate, y = 105 + yCoordinate, height = 15, width = 15) #Subtract Rebounds
        Label(master, text='Steals: ' + str(steals), anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 130 + yCoordinate, height = 30, width = 150)
        Button(master, text='+', bg="white", command=addSteals, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 115 + xCoordinate, y = 135 + yCoordinate, height = 15, width = 15) #Add Steals
        Button(master, text='-', bg="white", command=subtractSteals, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 130 + xCoordinate, y = 135 + yCoordinate, height = 15, width = 15) #Subtract Steals
        Label(master, text='Fouls: ' + str(fouls), anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 160 + yCoordinate, height = 30, width = 150)
        Button(master, text='+', bg="white", command=addFouls, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 115 + xCoordinate, y = 165 + yCoordinate, height = 15, width = 15) #Add Foul
        Button(master, text='-', bg="white", command=subtractFouls, fg="black", borderwidth=2, relief="raised", highlightbackground="gray90", activebackground="deep sky blue").place(x = 130 + xCoordinate, y = 165 + yCoordinate, height = 15, width = 15) #Subtract Fouls
        Label(master, text='Field Goal Percent: ' + str(fieldGoalPercentageRounded) + "%", anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 190 + yCoordinate, height = 30, width = 150)
        Label(master, text='3 Point FG Percent: ' + str(roundedThreePointFieldGoalPercentage) + "%", anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 220 + yCoordinate, height = 30, width = 150)
        Label(master, text='Free Throw Percent: ' + str(freeThrowPercentageRounded) + "%", anchor = 'w', bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 250 + yCoordinate, height = 30, width = 150)
        Button(master, text='FG Made', command=fieldGoalMade, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 280 + yCoordinate, height = 50, width =75)
        Button(master, text='FG Missed', command=fieldGoalMissed, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 80 + xCoordinate, y = 280 + yCoordinate, height = 50, width =75)
        Button(master, text='3PT Made', command=threePointerMade, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 330 + yCoordinate, height = 50, width =75)
        Button(master, text='3PT Missed', command=threePointerMissed, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 80 + xCoordinate, y = 330 + yCoordinate, height = 50, width =75)
        Button(master, text='FT Made', command=freeThrowMade, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 5 + xCoordinate, y = 380 + yCoordinate, height = 50, width =75)
        Button(master, text='FT Missed', comman=freeThrowMissed, bg="white", fg="black", highlightbackground="gray90", borderwidth=2, relief="raised", activebackground="deep sky blue").place(x = 80 + xCoordinate, y = 380 + yCoordinate, height = 50, width =75)

mainWindow()

master.mainloop()