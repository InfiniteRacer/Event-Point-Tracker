team1 = []
team2 = []
team3 = []
team4 = []
team5 = []
indiv = []
allteamscores = []

global nameofcomp

print("Welcome to the scoring system.")
print("")
print("ALL ANSWERS IN LOWER CASE - DONT PUT SPACES AT FRONT OR THE BACK.")
print("")
print("To enter a answer, type the word(s) or number. Then, click enter.")
print("")
nameofcomp=input("What is the name of the competition? ")
print("")
startprogramme=input("Start the scoring system for " +nameofcomp+ "? ('yes' or 'no') ")
print("")

def addteam1():
   
    global teamname1
    global team1
   
    print("Team selected. ")
    teamname1=input("Team name? ")
    teamname1teammate1=input("Team mate 1 name? ")
    teamname1teammate2=input("Team mate 2 name? ")
    teamname1teammate3=input("Team mate 3 name? ")
    teamname1teammate4=input("Team mate 4 name? ")
    teamname1teammate5=input("Team mate 5 name? ")
    print("Team name is " +teamname1+ ". Welcome to the tournament")
    print("Team mates are: ")
    print(teamname1teammate1)
    print(teamname1teammate2)
    print(teamname1teammate3)
    print(teamname1teammate4)
    print(teamname1teammate5)
   
    team1.append(teamname1teammate1)
    team1.append(teamname1teammate2)
    team1.append(teamname1teammate3)
    team1.append(teamname1teammate4)
    team1.append(teamname1teammate5)
   
    print("")
    print("")
    MainMenu()
   
def addteam2():
   
    global teamname2
    global team2
   
    print("Team selected. ")
    teamname2=input("Team name? ")
    teamname2teammate1=input("Team mate 1 name? ")
    teamname2teammate2=input("Team mate 2 name? ")
    teamname2teammate3=input("Team mate 3 name? ")
    teamname2teammate4=input("Team mate 4 name? ")
    teamname2teammate5=input("Team mate 5 name? ")
    print("Team name is " +teamname2+ ". Welcome to the tournament")
    print("Team mates are: ")
    print(teamname2teammate1)
    print(teamname2teammate2)
    print(teamname2teammate3)
    print(teamname2teammate4)
    print(teamname2teammate5)
   
    team2.append(teamname2teammate1)
    team2.append(teamname2teammate2)
    team2.append(teamname2teammate3)
    team2.append(teamname2teammate4)
    team2.append(teamname2teammate5)

    print("")
    print("")
    MainMenu()
   
def addteam3():
   
    global teamname3
    global team3
   
    print("Team selected. ")
    teamname3=input("Team name? ")
    teamname3teammate1=input("Team mate 1 name? ")
    teamname3teammate2=input("Team mate 2 name? ")
    teamname3teammate3=input("Team mate 3 name? ")
    teamname3teammate4=input("Team mate 4 name? ")
    teamname3teammate5=input("Team mate 5 name? ")
    print("Team name is " +teamname3+ ". Welcome to the tournament")
    print("Team mates are: ")
    print(teamname3teammate1)
    print(teamname3teammate2)
    print(teamname3teammate3)
    print(teamname3teammate4)
    print(teamname3teammate5)
   
    team3.append(teamname3teammate1)
    team3.append(teamname3teammate2)
    team3.append(teamname3teammate3)
    team3.append(teamname3teammate4)
    team3.append(teamname3teammate5)
   
    print("")
    print("")
    MainMenu()
   
def addteam4():
   
    global teamname4
    global team4
   
    print("Team selected. ")
    teamname4=input("Team name? ")
    teamname4teammate1=input("Team mate 1 name? ")
    teamname4teammate2=input("Team mate 2 name? ")
    teamname4teammate3=input("Team mate 3 name? ")
    teamname4teammate4=input("Team mate 4 name? ")
    teamname4teammate5=input("Team mate 5 name? ")
    print("Team name is " +teamname4+ ". Welcome to the tournament")
    print("Team mates are: ")
    print(teamname4teammate1)
    print(teamname4teammate2)
    print(teamname4teammate3)
    print(teamname4teammate4)
    print(teamname4teammate5)
   
    team4.append(teamname4teammate1)
    team4.append(teamname4teammate2)
    team4.append(teamname4teammate3)
    team4.append(teamname4teammate4)
    team4.append(teamname4teammate5)
   
    print("")
    print("")
    MainMenu()

def addteam5():
   
    global teamname5
    global team5
   
    print("Team selected. ")
    teamname5=input("Team name? ")
    teamname5teammate1=input("Team mate 1 name? ")
    teamname5teammate2=input("Team mate 2 name? ")
    teamname5teammate3=input("Team mate 3 name? ")
    teamname5teammate4=input("Team mate 4 name? ")
    teamname5teammate5=input("Team mate 5 name? ")
    print("Team name is " +teamname5+ ". Welcome to the tournament")
    print("Team mates are: ")
    print(teamname5teammate1)
    print(teamname5teammate2)
    print(teamname5teammate3)
    print(teamname5teammate4)
    print(teamname5teammate5)
   
    team5.append(teamname5teammate1)
    team5.append(teamname5teammate2)
    team5.append(teamname5teammate3)
    team5.append(teamname5teammate4)
    team5.append(teamname5teammate5)
   
    print("")
    print("")
    MainMenu()
   
def addindivs():
   
    global indiv1
    global indiv2
    global indiv3
    global indiv4
    global indiv5
    global indiv6
    global indiv7
    global indiv8
    global indiv9
    global indiv10
    global indiv11
    global indiv12
    global indiv13
    global indiv14
    global indiv15
    global indiv16
    global indiv17
    global indiv18
    global indiv19
    global indiv20
   
    indiv1=input("Name of person 1? ")
    indiv2=input("Name of person 2? ")
    indiv3=input("Name of person 3? ")
    indiv4=input("Name of person 4? ")
    indiv5=input("Name of person 5? ")
    indiv6=input("Name of person 6? ")
    indiv7=input("Name of person 7? ")
    indiv8=input("Name of person 8? ")
    indiv9=input("Name of person 9? ")
    indiv10=input("Name of person 10? ")
    indiv11=input("Name of person 11? ")
    indiv12=input("Name of person 12? ")
    indiv13=input("Name of person 13? ")
    indiv14=input("Name of person 14? ")
    indiv15=input("Name of person 15? ")
    indiv16=input("Name of person 16? ")
    indiv17=input("Name of person 17? ")
    indiv18=input("Name of person 18? ")
    indiv19=input("Name of person 19? ")
    indiv20=input("Name of person 20? ")
   
#     indiv.append(indiv1)
#     indiv.append(indiv2)
#     indiv.append(indiv3)
#     indiv.append(indiv4)
#     indiv.append(indiv5)
#     indiv.append(indiv6)
#     indiv.append(indiv7)
#     indiv.append(indiv8)
#     indiv.append(indiv9)
#     indiv.append(indiv10)
#     indiv.append(indiv11)
#     indiv.append(indiv12)
#     indiv.append(indiv13)
#     indiv.append(indiv14)
#     indiv.append(indiv15)
#     indiv.append(indiv16)
#     indiv.append(indiv17)
#     indiv.append(indiv18)
#     indiv.append(indiv19)
#     indiv.append(indiv20)
   
    print("")
    print("")
    print("Indiv sign up complete. Continue by using the menu below.")
    print("")
    print("")
    MainMenu()
   
def addgames():
   
    global game1name
    global game2name
    global game3name
    global game4name
    global game5name
    
    global game1nametype
    global game2nametype
    global game3nametype
    global game4nametype
    global game5nametype
   
    global game1TEAMname
    global game2TEAMname
    global game3TEAMname
    global game4TEAMname
    global game5TEAMname
    
    global game1TEAMnametype
    global game2TEAMnametype
    global game3TEAMnametype
    global game4TEAMnametype
    global game5TEAMnametype
   
    print("")
    print("Indiv only games:")
    print("")
   
    game1name=input("Name of game 1? ")
    game1nametype=input("Is " +game1name+ " academic or sport? ")
    game2name=input("Name of game 2? ")
    game2nametype=input("Is " +game2name+ " academic or sport? ")
    game3name=input("Name of game 3? ")
    game3nametype=input("Is " +game3name+ " academic or sport? ")
    game4name=input("Name of game 4? ")
    game4nametype=input("Is " +game4name+ " academic or sport? ")
    game5name=input("Name of game 5? ")
    game5nametype=input("Is " +game5name+ " academic or sport? ")
   
    print("")
    print("Team only games:")
    print("")
   
    game1TEAMname=input("Name of game 1? ")
    game1TEAMnametype=input("Is " +game1TEAMname+ " academic or sport? ")
    game2TEAMname=input("Name of game 2? ")
    game2TEAMnametype=input("Is " +game2TEAMname+ " academic or sport? ")
    game3TEAMname=input("Name of game 3? ")
    game3TEAMnametype=input("Is " +game3TEAMname+ " academic or sport? ")
    game4TEAMname=input("Name of game 4? ")
    game4TEAMnametype=input("Is " +game4TEAMname+ " academic or sport? ")
    game5TEAMname=input("Name of game 5? ")
    game5TEAMnametype=input("Is " +game5TEAMname+ " academic or sport? ")
   
    print("")
    print("")
    print("Game set up complete. Continue by using the menu below.")
    print("")
    print("")
    MainMenu()

def teamgamescoresubmit():
   
    global team1GAME1score
    global team2GAME1score
    global team3GAME1score
    global team4GAME1score
    global team5GAME1score
   
    global team1GAME2score
    global team2GAME2score
    global team3GAME2score
    global team4GAME2score
    global team5GAME2score
   
    global team1GAME3score
    global team2GAME3score
    global team3GAME3score
    global team4GAME3score
    global team5GAME3score
   
    global team1GAME4score
    global team2GAME4score
    global team3GAME4score
    global team4GAME4score
    global team5GAME4score
   
    global team1GAME5score
    global team2GAME5score
    global team3GAME5score
    global team4GAME5score
    global team5GAME5score
   
    print("Game 1 score ONLY - " +game1TEAMname)
    team1GAME1score=input("Judges, please enter the score for team " +teamname1+ ": ")
    team2GAME1score=input("Judges, please enter the score for team " +teamname2+ ": ")
    team3GAME1score=input("Judges, please enter the score for team " +teamname3+ ": ")
    team4GAME1score=input("Judges, please enter the score for team " +teamname4+ ": ")
    team5GAME1score=input("Judges, please enter the score for team " +teamname5+ ": ")
   
    print("Game 2 score ONLY - " +game2TEAMname)
    team1GAME2score=input("Judges, please enter the score for team " +teamname1+ ": ")
    team2GAME2score=input("Judges, please enter the score for team " +teamname2+ ": ")
    team3GAME2score=input("Judges, please enter the score for team " +teamname3+ ": ")
    team4GAME2score=input("Judges, please enter the score for team " +teamname4+ ": ")
    team5GAME2score=input("Judges, please enter the score for team " +teamname5+ ": ")
   
    print("Game 3 score ONLY - " +game3TEAMname)
    team1GAME3score=input("Judges, please enter the score for team " +teamname1+ ": ")
    team2GAME3score=input("Judges, please enter the score for team " +teamname2+ ": ")
    team3GAME3score=input("Judges, please enter the score for team " +teamname3+ ": ")
    team4GAME3score=input("Judges, please enter the score for team " +teamname4+ ": ")
    team5GAME3score=input("Judges, please enter the score for team " +teamname5+ ": ")
   
    print("Game 4 score ONLY - " +game4TEAMname)
    team1GAME4score=input("Judges, please enter the score for team " +teamname1+ ": ")
    team2GAME4score=input("Judges, please enter the score for team " +teamname2+ ": ")
    team3GAME4score=input("Judges, please enter the score for team " +teamname3+ ": ")
    team4GAME4score=input("Judges, please enter the score for team " +teamname4+ ": ")
    team5GAME4score=input("Judges, please enter the score for team " +teamname5+ ": ")
   
    print("Game 5 score ONLY - " +game5TEAMname)
    team1GAME5score=input("Judges, please enter the score for team " +teamname1+ ": ")
    team2GAME5score=input("Judges, please enter the score for team " +teamname2+ ": ")
    team3GAME5score=input("Judges, please enter the score for team " +teamname3+ ": ")
    team4GAME5score=input("Judges, please enter the score for team " +teamname4+ ": ")
    team5GAME5score=input("Judges, please enter the score for team " +teamname5+ ": ")
   
    print("")
    print("")
    print("Game scores entered. Continue by using the menu below.")
    print("")
    print("")
    MainMenu()

def indivgamescoresubmit():
   
    global indiv1GAME1score
    global indiv2GAME1score
    global indiv3GAME1score
    global indiv4GAME1score
    global indiv5GAME1score
    global indiv6GAME1score
    global indiv7GAME1score
    global indiv8GAME1score
    global indiv9GAME1score
    global indiv10GAME1score
    global indiv11GAME1score
    global indiv12GAME1score
    global indiv13GAME1score
    global indiv14GAME1score
    global indiv15GAME1score
    global indiv16GAME1score
    global indiv17GAME1score
    global indiv18GAME1score
    global indiv19GAME1score
    global indiv20GAME1score
   
    global indiv1GAME2score
    global indiv2GAME2score
    global indiv3GAME2score
    global indiv4GAME2score
    global indiv5GAME2score
    global indiv6GAME2score
    global indiv7GAME2score
    global indiv8GAME2score
    global indiv9GAME2score
    global indiv10GAME2score
    global indiv11GAME2score
    global indiv12GAME2score
    global indiv13GAME2score
    global indiv14GAME2score
    global indiv15GAME2score
    global indiv16GAME2score
    global indiv17GAME2score
    global indiv18GAME2score
    global indiv19GAME2score
    global indiv20GAME2score
   
    global indiv1GAME3score
    global indiv2GAME3score
    global indiv3GAME3score
    global indiv4GAME3score
    global indiv5GAME3score
    global indiv6GAME3score
    global indiv7GAME3score
    global indiv8GAME3score
    global indiv9GAME3score
    global indiv10GAME3score
    global indiv11GAME3score
    global indiv12GAME3score
    global indiv13GAME3score
    global indiv14GAME3score
    global indiv15GAME3score
    global indiv16GAME3score
    global indiv17GAME3score
    global indiv18GAME3score
    global indiv19GAME3score
    global indiv20GAME3score
   
    global indiv1GAME4score
    global indiv2GAME4score
    global indiv3GAME4score
    global indiv4GAME4score
    global indiv5GAME4score
    global indiv6GAME4score
    global indiv7GAME4score
    global indiv8GAME4score
    global indiv9GAME4score
    global indiv10GAME4score
    global indiv11GAME4score
    global indiv12GAME4score
    global indiv13GAME4score
    global indiv14GAME4score
    global indiv15GAME4score
    global indiv16GAME4score
    global indiv17GAME4score
    global indiv18GAME4score
    global indiv19GAME4score
    global indiv20GAME4score
   
    global indiv1GAME5score
    global indiv2GAME5score
    global indiv3GAME5score
    global indiv4GAME5score
    global indiv5GAME5score
    global indiv6GAME5score
    global indiv7GAME5score
    global indiv8GAME5score
    global indiv9GAME5score
    global indiv10GAME5score
    global indiv11GAME5score
    global indiv12GAME5score
    global indiv13GAME5score
    global indiv14GAME5score
    global indiv15GAME5score
    global indiv16GAME5score
    global indiv17GAME5score
    global indiv18GAME5score
    global indiv19GAME5score
    global indiv20GAME5score
   
    print("Game 1 score ONLY - " +game1name)
    indiv1GAME1score=input("Judges, please enter the score for " +indiv1+ ": ")
    indiv2GAME1score=input("Judges, please enter the score for " +indiv2+ ": ")
    indiv3GAME1score=input("Judges, please enter the score for " +indiv3+ ": ")
    indiv4GAME1score=input("Judges, please enter the score for " +indiv4+ ": ")
    indiv5GAME1score=input("Judges, please enter the score for " +indiv5+ ": ")
    indiv6GAME1score=input("Judges, please enter the score for " +indiv6+ ": ")
    indiv7GAME1score=input("Judges, please enter the score for " +indiv7+ ": ")
    indiv8GAME1score=input("Judges, please enter the score for " +indiv8+ ": ")
    indiv9GAME1score=input("Judges, please enter the score for " +indiv9+ ": ")
    indiv10GAME1score=input("Judges, please enter the score for " +indiv10+ ": ")
    indiv11GAME1score=input("Judges, please enter the score for " +indiv11+ ": ")
    indiv12GAME1score=input("Judges, please enter the score for " +indiv12+ ": ")
    indiv13GAME1score=input("Judges, please enter the score for " +indiv13+ ": ")
    indiv14GAME1score=input("Judges, please enter the score for " +indiv14+ ": ")
    indiv15GAME1score=input("Judges, please enter the score for " +indiv15+ ": ")
    indiv16GAME1score=input("Judges, please enter the score for " +indiv16+ ": ")
    indiv17GAME1score=input("Judges, please enter the score for " +indiv17+ ": ")
    indiv18GAME1score=input("Judges, please enter the score for " +indiv18+ ": ")
    indiv19GAME1score=input("Judges, please enter the score for " +indiv19+ ": ")
    indiv20GAME1score=input("Judges, please enter the score for " +indiv20+ ": ")
   
    print("Game 2 score ONLY - " +game2name)
    indiv1GAME2score=input("Judges, please enter the score for " +indiv1+ ": ")
    indiv2GAME2score=input("Judges, please enter the score for " +indiv2+ ": ")
    indiv3GAME2score=input("Judges, please enter the score for " +indiv3+ ": ")
    indiv4GAME2score=input("Judges, please enter the score for " +indiv4+ ": ")
    indiv5GAME2score=input("Judges, please enter the score for " +indiv5+ ": ")
    indiv6GAME2score=input("Judges, please enter the score for " +indiv6+ ": ")
    indiv7GAME2score=input("Judges, please enter the score for " +indiv7+ ": ")
    indiv8GAME2score=input("Judges, please enter the score for " +indiv8+ ": ")
    indiv9GAME2score=input("Judges, please enter the score for " +indiv9+ ": ")
    indiv10GAME2score=input("Judges, please enter the score for " +indiv10+ ": ")
    indiv11GAME2score=input("Judges, please enter the score for " +indiv11+ ": ")
    indiv12GAME2score=input("Judges, please enter the score for " +indiv12+ ": ")
    indiv13GAME2score=input("Judges, please enter the score for " +indiv13+ ": ")
    indiv14GAME2score=input("Judges, please enter the score for " +indiv14+ ": ")
    indiv15GAME2score=input("Judges, please enter the score for " +indiv15+ ": ")
    indiv16GAME2score=input("Judges, please enter the score for " +indiv16+ ": ")
    indiv17GAME2score=input("Judges, please enter the score for " +indiv17+ ": ")
    indiv18GAME2score=input("Judges, please enter the score for " +indiv18+ ": ")
    indiv19GAME2score=input("Judges, please enter the score for " +indiv19+ ": ")
    indiv20GAME2score=input("Judges, please enter the score for " +indiv20+ ": ")
   
    print("Game 3 score ONLY - " +game3name)
    indiv1GAME3score=input("Judges, please enter the score for " +indiv1+ ": ")
    indiv2GAME3score=input("Judges, please enter the score for " +indiv2+ ": ")
    indiv3GAME3score=input("Judges, please enter the score for " +indiv3+ ": ")
    indiv4GAME3score=input("Judges, please enter the score for " +indiv4+ ": ")
    indiv5GAME3score=input("Judges, please enter the score for " +indiv5+ ": ")
    indiv6GAME3score=input("Judges, please enter the score for " +indiv6+ ": ")
    indiv7GAME3score=input("Judges, please enter the score for " +indiv7+ ": ")
    indiv8GAME3score=input("Judges, please enter the score for " +indiv8+ ": ")
    indiv9GAME3score=input("Judges, please enter the score for " +indiv9+ ": ")
    indiv10GAME3score=input("Judges, please enter the score for " +indiv10+ ": ")
    indiv11GAME3score=input("Judges, please enter the score for " +indiv11+ ": ")
    indiv12GAME3score=input("Judges, please enter the score for " +indiv12+ ": ")
    indiv13GAME3score=input("Judges, please enter the score for " +indiv13+ ": ")
    indiv14GAME3score=input("Judges, please enter the score for " +indiv14+ ": ")
    indiv15GAME3score=input("Judges, please enter the score for " +indiv15+ ": ")
    indiv16GAME3score=input("Judges, please enter the score for " +indiv16+ ": ")
    indiv17GAME3score=input("Judges, please enter the score for " +indiv17+ ": ")
    indiv18GAME3score=input("Judges, please enter the score for " +indiv18+ ": ")
    indiv19GAME3score=input("Judges, please enter the score for " +indiv19+ ": ")
    indiv20GAME3score=input("Judges, please enter the score for " +indiv20+ ": ")
   
    print("Game 4 score ONLY - " +game4name)
    indiv1GAME4score=input("Judges, please enter the score for " +indiv1+ ": ")
    indiv2GAME4score=input("Judges, please enter the score for " +indiv2+ ": ")
    indiv3GAME4score=input("Judges, please enter the score for " +indiv3+ ": ")
    indiv4GAME4score=input("Judges, please enter the score for " +indiv4+ ": ")
    indiv5GAME4score=input("Judges, please enter the score for " +indiv5+ ": ")
    indiv6GAME4score=input("Judges, please enter the score for " +indiv6+ ": ")
    indiv7GAME4score=input("Judges, please enter the score for " +indiv7+ ": ")
    indiv8GAME4score=input("Judges, please enter the score for " +indiv8+ ": ")
    indiv9GAME4score=input("Judges, please enter the score for " +indiv9+ ": ")
    indiv10GAME4score=input("Judges, please enter the score for " +indiv10+ ": ")
    indiv11GAME4score=input("Judges, please enter the score for " +indiv11+ ": ")
    indiv12GAME4score=input("Judges, please enter the score for " +indiv12+ ": ")
    indiv13GAME4score=input("Judges, please enter the score for " +indiv13+ ": ")
    indiv14GAME4score=input("Judges, please enter the score for " +indiv14+ ": ")
    indiv15GAME4score=input("Judges, please enter the score for " +indiv15+ ": ")
    indiv16GAME4score=input("Judges, please enter the score for " +indiv16+ ": ")
    indiv17GAME4score=input("Judges, please enter the score for " +indiv17+ ": ")
    indiv18GAME4score=input("Judges, please enter the score for " +indiv18+ ": ")
    indiv19GAME4score=input("Judges, please enter the score for " +indiv19+ ": ")
    indiv20GAME4score=input("Judges, please enter the score for " +indiv20+ ": ")
   
    print("Game 5 score ONLY - " +game5name)
    indiv1GAME5score=input("Judges, please enter the score for " +indiv1+ ": ")
    indiv2GAME5score=input("Judges, please enter the score for " +indiv2+ ": ")
    indiv3GAME5score=input("Judges, please enter the score for " +indiv3+ ": ")
    indiv4GAME5score=input("Judges, please enter the score for " +indiv4+ ": ")
    indiv5GAME5score=input("Judges, please enter the score for " +indiv5+ ": ")
    indiv6GAME5score=input("Judges, please enter the score for " +indiv6+ ": ")
    indiv7GAME5score=input("Judges, please enter the score for " +indiv7+ ": ")
    indiv8GAME5score=input("Judges, please enter the score for " +indiv8+ ": ")
    indiv9GAME5score=input("Judges, please enter the score for " +indiv9+ ": ")
    indiv10GAME5score=input("Judges, please enter the score for " +indiv10+ ": ")
    indiv11GAME5score=input("Judges, please enter the score for " +indiv11+ ": ")
    indiv12GAME5score=input("Judges, please enter the score for " +indiv12+ ": ")
    indiv13GAME5score=input("Judges, please enter the score for " +indiv13+ ": ")
    indiv14GAME5score=input("Judges, please enter the score for " +indiv14+ ": ")
    indiv15GAME5score=input("Judges, please enter the score for " +indiv15+ ": ")
    indiv16GAME5score=input("Judges, please enter the score for " +indiv16+ ": ")
    indiv17GAME5score=input("Judges, please enter the score for " +indiv17+ ": ")
    indiv18GAME5score=input("Judges, please enter the score for " +indiv18+ ": ")
    indiv19GAME5score=input("Judges, please enter the score for " +indiv19+ ": ")
    indiv20GAME5score=input("Judges, please enter the score for " +indiv20+ ": ")
   
    print("")
    print("")
    print("Game scores entered. Continue by using the menu below.")
    print("")
    print("")
    MainMenu()
   
def gametypesubmit():
   
    print("Press '1' to submit scores for INDIV games.")
    print("Press '2' to submit scores for TEAM games.")
   
    gametypesubmitquestion=input("Type your option choice and press enter: ")
    gametypesubmitquestion = int(gametypesubmitquestion)
   
    if gametypesubmitquestion == 1:
        indivgamescoresubmit()
    elif gametypesubmitquestion == 2:
        teamgamescoresubmit()
       
def winnersectionselect():
   
    print("Press '1' to find the winner out of teams.")
    print("Press '2' to find the winner out of indivs.")
    print("Press '3' to go back to the menu.")
   
    winnersectionselectoption=input("Type your option choice and press enter: ")
    winnersectionselectoption = int(winnersectionselectoption)
   
    if winnersectionselectoption == 1:
        winnersectionteam()
    elif winnersectionselectoption == 2:
        winnersectionindiv()
    elif winnersectionselectoption == 3:
        MainMenu()
       
def winnersectionteam():
   
    global finalteam1score
    global finalteam2score
    global finalteam3score
    global finalteam4score
    global finalteam5score
    global allteamscoresMAX
   
    finalteam1score = int(team1GAME1score) + int(team1GAME2score) + int(team1GAME3score) + int(team1GAME4score) + int(team1GAME5score)
    print("Final score for " +teamname1+ " is:")
    print(finalteam1score)
    
    finalteam2score = int(team2GAME1score) + int(team2GAME2score) + int(team2GAME3score) + int(team2GAME4score) + int(team2GAME5score)
    print("Final score for " +teamname2+ " is:")
    print(finalteam2score)
    
    finalteam3score = int(team3GAME1score) + int(team3GAME2score) + int(team3GAME3score) + int(team3GAME4score) + int(team3GAME5score)
    print("Final score for " +teamname3+ " is:")
    print(finalteam3score)
    
    finalteam4score = int(team4GAME1score) + int(team4GAME2score) + int(team4GAME3score) + int(team4GAME4score) + int(team4GAME5score)
    print("Final score for " +teamname4+ " is:")
    print(finalteam4score)
    
    finalteam5score = int(team5GAME5score) + int(team5GAME2score) + int(team5GAME3score) + int(team5GAME4score) + int(team5GAME5score)
    print("Final score for " +teamname5+ " is:")
    print(finalteam5score)
    
    allteamscores.append(finalteam1score)
    allteamscores.append(finalteam2score)
    allteamscores.append(finalteam3score)
    allteamscores.append(finalteam4score)
    allteamscores.append(finalteam5score)
    
    print("")
    print("")
    print("")
    
    print("Out of all teams, the winner is: ")
    
    print("")
    
#     allteamscoresMAX = max(allteamscores)
#     print(allteamscoresMAX)
#     
#     winnersectionoverallgoback()
    
def winnersectionindiv():

    global finalindiv1score
    global finalindiv2score
    global finalindiv3score
    global finalindiv4score
    global finalindiv5score
    global finalindiv6score
    global finalindiv7score
    global finalindiv8score
    global finalindiv9score
    global finalindiv10score
    global finalindiv11score
    global finalindiv12score
    global finalindiv13score
    global finalindiv14score
    global finalindiv15score
    global finalindiv16score
    global finalindiv17score
    global finalindiv18score
    global finalindiv19score
    global finalindiv20score

    finalindiv1score = int(indiv1GAME1score) + int(indiv1GAME2score) + int(indiv1GAME3score) + int(indiv1GAME4score) + int(indiv1GAME5score)
    print("Final score for " +indiv1+ " is:")
    print(finalindivm1score)
    
    finalindiv1score = int(indiv2GAME1score) + int(indiv2GAME2score) + int(indiv2GAME3score) + int(indiv2GAME4score) + int(indiv2GAME5score)
    print("Final score for " +indiv2+ " is:")
    print(finalindiv2score)
    
    finalindiv1score = int(indiv3GAME1score) + int(indiv3GAME2score) + int(indiv3GAME3score) + int(indiv3GAME4score) + int(indiv3GAME5score)
    print("Final score for " +indiv3+ " is:")
    print(finalindiv3score)
    
    finalindiv1score = int(indiv4GAME1score) + int(indiv4GAME2score) + int(indiv4GAME3score) + int(indiv4GAME4score) + int(indiv4GAME5score)
    print("Final score for " +indiv4+ " is:")
    print(finalindiv4score)
    
    finalindiv1score = int(indiv5GAME1score) + int(indiv5GAME2score) + int(indiv5GAME3score) + int(indiv5GAME4score) + int(indiv5GAME5score)
    print("Final score for " +indiv5+ " is:")
    print(finalindiv5score)
    
    finalindiv1score = int(indiv6GAME1score) + int(indiv6GAME2score) + int(indiv6GAME3score) + int(indiv6GAME4score) + int(indiv6GAME5score)
    print("Final score for " +indiv6+ " is:")
    print(finalindiv6score)
    
    finalindiv1score = int(indiv7GAME1score) + int(indiv7GAME2score) + int(indiv7GAME3score) + int(indiv7GAME4score) + int(indiv7GAME5score)
    print("Final score for " +indiv7+ " is:")
    print(finalindiv7score)
    
    finalindiv1score = int(indiv8GAME1score) + int(indiv8GAME2score) + int(indiv8GAME3score) + int(indiv8GAME4score) + int(indiv8GAME5score)
    print("Final score for " +indiv8+ " is:")
    print(finalindiv8score)
    
    finalindiv1score = int(indiv9GAME1score) + int(indiv9GAME2score) + int(indiv9GAME3score) + int(indiv9GAME4score) + int(indiv9GAME5score)
    print("Final score for " +indiv9+ " is:")
    print(finalindiv9score)
    
    finalindiv1score = int(indiv10GAME1score) + int(indiv10GAME2score) + int(indiv10GAME3score) + int(indiv10GAME4score) + int(indiv10GAME5score)
    print("Final score for " +indiv10+ " is:")
    print(finalindiv10score)
   
    finalindiv1score = int(indiv11GAME1score) + int(indiv11GAME2score) + int(indiv11GAME3score) + int(indiv11GAME4score) + int(indiv11GAME5score)
    print("Final score for " +indiv11+ " is:")
    print(finalindiv11score)
    
    finalindiv1score = int(indiv12GAME1score) + int(indiv12GAME2score) + int(indiv12GAME3score) + int(indiv12GAME4score) + int(indiv12GAME5score)
    print("Final score for " +indiv12+ " is:")
    print(finalindiv12score)
    
    finalindiv1score = int(indiv13GAME1score) + int(indiv13GAME2score) + int(indiv13GAME3score) + int(indiv13GAME4score) + int(indiv13GAME5score)
    print("Final score for " +indiv13+ " is:")
    print(finalindiv13score)
    
    finalindiv1score = int(indiv14GAME1score) + int(indiv14GAME2score) + int(indiv14GAME3score) + int(indiv14GAME4score) + int(indiv14GAME5score)
    print("Final score for " +indiv14+ " is:")
    print(finalindiv14score)
    
    finalindiv1score = int(indiv15GAME1score) + int(indiv15GAME2score) + int(indiv15GAME3score) + int(indiv15GAME4score) + int(indiv15GAME5score)
    print("Final score for " +indiv15+ " is:")
    print(finalindiv15score)
    
    finalindiv1score = int(indiv16GAME1score) + int(indiv16GAME2score) + int(indiv16GAME3score) + int(indiv16GAME4score) + int(indiv16GAME5score)
    print("Final score for " +indiv16+ " is:")
    print(finalindiv16score)
    
    finalindiv1score = int(indiv17GAME1score) + int(indiv17GAME2score) + int(indiv17GAME3score) + int(indiv17GAME4score) + int(indiv17GAME5score)
    print("Final score for " +indiv17+ " is:")
    print(finalindiv17score)
    
    finalindiv1score = int(indiv18GAME1score) + int(indiv18GAME2score) + int(indiv18GAME3score) + int(indiv18GAME4score) + int(indiv18GAME5score)
    print("Final score for " +indiv18+ " is:")
    print(finalindiv18score)
    
    finalindiv1score = int(indiv19GAME1score) + int(indiv19GAME2score) + int(indiv19GAME3score) + int(indiv19GAME4score) + int(indiv19GAME5score)
    print("Final score for " +indiv19+ " is:")
    print(finalindiv19score)
    
    finalindiv1score = int(indiv20GAME1score) + int(indiv20GAME2score) + int(indiv20GAME3score) + int(indiv20GAME4score) + int(indiv20GAME5score)
    print("Final score for " +indiv20+ " is:")
    print(finalindiv20score)
    
    allindivscores.append(finalindiv1score)
    allindivscores.append(finalindiv2score)
    allindivscores.append(finalindiv3score)
    allindivscores.append(finalindiv4score)
    allindivscores.append(finalindiv5score)
    allindivscores.append(finalindiv6score)
    allindivscores.append(finalindiv7score)
    allindivscores.append(finalindiv8score)
    allindivscores.append(finalindiv9score)
    allindivscores.append(finalindiv10score)
    allindivscores.append(finalindiv11score)
    allindivscores.append(finalindiv12score)
    allindivscores.append(finalindiv13score)
    allindivscores.append(finalindiv14score)
    allindivscores.append(finalindiv15score)
    allindivscores.append(finalindiv16score)
    allindivscores.append(finalindiv17score)
    allindivscores.append(finalindiv18score)
    allindivscores.append(finalindiv19score)
    allindivscores.append(finalindiv20score)
    
    print("")
    print("")
    print("")
    
    print("Out of all the indiv players, the winner is: ")
    
    print("")
    
#     allindivscoresMAX = max(allindivscores)
#     print(allindivscoresMAX)
#     
#     winnersectionoverallgoback()
    
def winnersectionoverallgoback():
   
    print("Press '1' to find out the other section winners.")
    print("Press '2' to stop program OR go back to main menu.")
   
    winnersectionselectoptiongobackoption=input("Type your option choice and press enter: ")
    winnersectionselectoptiongobackoption = int(winnersectionselectoptiongobackoption)
   
    if winnersectionselectoptiongobackoption == 1:
        winnersectionselect()
    elif winnersectionselectoptiongobackoption == 2:
        exitoptionoff()
        
def exitoptionoff():
    
    print("Press '1' to go to main menu.")
    print("Press '2' to stop program - ALL PROGRESS SO FAR WILL BE LOST.")
   
    winnersectionselectoptiongobackoption=input("Type your option choice and press enter: ")
    winnersectionselectoptiongobackoption = int(winnersectionselectoptiongobackoption)
   
    if winnersectionselectoptiongobackoption == 1:
        MainMenu()
    elif winnersectionselectoptiongobackoption == 2:
        exitoptionoffconfirm()
        
def exitoptionoffconfirm():

    print("Press '1' to go to main menu and stop exit program.")
    print("Press '2' to confirm stopping the program. - ALL PROGRESS SO FAR WILL BE LOST.")
   
    winnersectionselectoptiongobackoption=input("Type your option choice and press enter: ")
    winnersectionselectoptiongobackoption = int(winnersectionselectoptiongobackoption)
   
    if winnersectionselectoptiongobackoption == 1:
        MainMenu()
    elif winnersectionselectoptiongobackoption == 2:
        exit

def MainMenu():
   
    print("Press '1' to add Team 1.")
    print("Press '2' to add Team 2.")
    print("Press '3' to add Team 3.")
    print("Press '4' to add Team 4.")
    print("Press '5' to add Team 5.")
    print("Press '6' to add ALL indiv's at once.")
    print("Press '7' to add ALL games.")
    print("Press '8' to start entering score's for the games. ONLY USE THIS OPTION ONCE FILLED EVERYTHING ELSE.")
    print("Press '9' to find the winner. ONLY USE THIS AFTER USING EVERY OTHER OPTION POSSIBLE ON THE MAIN MENU.")
    print("Press '10' to exit and close the program.")

    menuchoice=input("Type your option choice and press enter: ")
    menuchoice = int(menuchoice)


    if menuchoice == 1:
        addteam1()
    elif menuchoice == 2:
        addteam2()
    elif menuchoice == 3:
        addteam3()
    elif menuchoice == 4:
        addteam4()
    elif menuchoice == 5:
        addteam5()
    elif menuchoice == 6:
        addindivs()
    elif menuchoice == 7:
        addgames()
    elif menuchoice == 8:
        gametypesubmit()
    elif menuchoice == 9:
        winnersectionselect()
    elif menuchoice == 10:
        exitoptionoff()

if startprogramme == 'yes':
    print("Welcome " +nameofcomp+ "!")
    print("")
    MainMenu()
elif startprogramme == 'no':
    print("Scoring system stopped.")
    print("")
    
    exit