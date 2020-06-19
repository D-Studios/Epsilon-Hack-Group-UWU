#SQL is used in this project
import mysql.connector

'''
8values
Economic   Diplomatic   Civil       Societal
equality   nation       liberty     tradition   + positive
market     world        authority   progress    - negative
'''

# Higher values of economic means for more equality, lower values of economic means market favorable.
economic = 0
# Higher values of diplomatic means more favorable to nation, lower values of diplomatic means more favorable to world.
diplomatic = 0
# Higher values of civil means more favorable to governmental authority, lower values of civil means more favorable to civil liberties.
civil = 0
# Higher values of societal means more favorable towards tradition, lower values of societal means more favorable to progress.
societal = 0
# What value is considered neutral in a range.
neutral = 0
# How strongly can a person disagree.
mininum = 0
# How strongly can a person agree.
maximum = 0
#This is the user's social security number.
ssn=0

#MySQL start up
mydb = mysql.connector.connect(
  host="35.247.48.245",
  user="root",
  password=""
)

mycursor = mydb.cursor()

#This function is for creating a new database and a new table. This is used for debugging purposes.
def create_sql():
    mycursor.execute("CREATE DATABASE Survey")
    mycursor.execute("CREATE TABLE Responses (id INT AUTO_INCREMENT PRIMARY KEY, "
                 "Social Security Number INT, "
                 "Economic Points (<50pts favors market, >50pts favors equality, =50 points favors none) INT,"
                 "Diplomatic Points (<50pts favors world, >50pts favors nation, =50 points favors none) INT,"
                 "Civil Points (<50pts favors authority, >50pts favors liberty, =50 points favors none),"
                 "Societal Points (<50pts favors progress, >50pts favors tradition, =50 points favors none) INT)")

#This function is used for altering the contents of the database and table created in MySQL.
def alter_sql():
    mycursor.execute("ALTER TABLE Responses ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# Initalization starts everything at neutrality
def initialization():
    global economic, diplomatic, civil, societal, neutral, mininum, maximum
    # In a range of 0-100, 50 is neutral.
    economic = 50
    diplomatic = 50
    civil = 50
    societal = 50
    # Mininum is strongly disagree, while maximum is strongly agree.
    mininum = 1
    maximum = 7
    neutral = (mininum + maximum) / 2

# The user enters their Social Security Number and the program makes sure that this is entered correctly.
def user_indentification():
    global ssn
    while True:
        try:
            ssn = int(input("Enter your social security: "))
            sql = "SELECT * FROM Responses WHERE Social Security Number = (%d) ", (ssn)
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            if len(myresult)>0:
                print("You have already done this survey before!")
                continue
            break
        except:
            print("Invalid input.")
#This function debugs the values for some variables.
def debug():
    global economic, diplomatic, civil, societal
    print("Economic: "+str(economic))
    print("Diplomatic: "+str(diplomatic))
    print("Civil: "+str(civil))
    print("Societal: "+str(societal))

# This function asks questions and gives points to appropiate categories
def question_asker(question, issue, weight=1):
    global economic, diplomatic, civil, societal, neutral, mininum, maximum
    # Ask the question
    print(question)
    answer = mininum - 1
    # Keep on asking for a value until the value fits in the range of mininum-maximum.
    while answer < mininum or answer > maximum:
        try:
            answer = int(input("On a scale of 1-7, 1 being strongly disagree, 4 being neutral, and \
7 being strongly agree, what is your opinion on this question?\n"))
        except:
            pass
    # The points are calculated depending on how strong the position is.
    if answer<neutral:
        points=-pow(2, abs(answer-neutral)-1)*weight
    elif answer==neutral:
        points=0
    else:
        points=pow(2, abs(answer-neutral)-1)*weight
    '''Issues:
       1. Economic
       2. Diplomatic
       3. Civil
       4. Societal'''
    if issue is "equality":
        economic += points
    if issue is "market":
        economic-=points
    if issue is "nation":
        diplomatic+=points
    if issue is "world":
        diplomatic-=points
    if issue is "liberty":
        civil+=points
    if issue is "authority":
        civil-=points
    if issue is "tradition":
        societal+=points
    if issue is "progress":
        societal-=points
    #The values for economic, diplomatic, civil, and societal are clamped.
    economic=clamp(economic)
    diplomatic=clamp(diplomatic)
    civil=clamp(civil)
    societal=clamp(societal)
    #This function will be used to find the values of economic, diplomatic, civil, and societal.
    debug()

#This function clamps values to be within a range.
def clamp(val, min=0, max=100):
    if val<min:
        return min
    elif val>max:
        return max
    else:
        return val

#This function will insert into the database values.
def add_to_database():
    global economic, diplomatic, civil, societal,ssn
    sql = "INSERT INTO Responses " \
          "(Social Security Number, " \
          "Economic Points (<50pts favors market, >50pts favors equality, =50 points favors none)," \
          "Diplomatic Points (<50pts favors world, >50pts favors nation, =50 points favors none)," \
          "Civil Points (<50pts favors authority, >50pts favors liberty, =50 points favors none)," \
          "Societal Points (<50pts favors progress, >50pts favors tradition, =50 points favors none)) " \
          "VALUES (%d, %d, %d, %d, %d )"
    val = (ssn, economic, diplomatic, civil, societal)
    mycursor.execute(sql, val)

    mydb.commit()


#This function will purge the database. Call it to delete everything. This function is only for debugging purposes.
def delete_sql(createNew=True):
    sql = "DROP TABLE IF EXISTS Reponses"
    mycursor.execute(sql)
    if(createNew):
        create_sql()

# This is the main function.
def main():
    # Intialize the program.
    initialization()
    user_indentification()
    '''
    economic   diplomatic  civil       societal
    equality   nation      liberty     tradition
    market     world       authority   progress    
    '''
    #List Of Questions With Categories
    questions={
        "People should not be discriminated against based on intrinsic qualities in any capacity." : "equality",
        "Progress should be pursued, even at the expense of tradition" : "progress",
        "Cultural values should be preserved and nurtured for future generations" : "tradition",
        "Government is run by people with unchecked power" : "liberty",
        "A large portion of people are unable to make good decisions for themselves" : "authority",
        "Unrestricted markets will result in everyone becoming wealthier." : "market",
        "A citizen's primary concern is with his/her nation and then the world." : "nation",
        "National governments must be kept in check by the global community by any means necessary." : "world",
        "There is minimal physical and mental difference between people of different races." : "equality",
        "We are heading to a better world." : "progress",
        "New change should be implemented slowly" : "tradition",
        "Victimless crimes should not be illegal." : "liberty",
        "Maintaining order is more important than preserving all freedoms." :  "authority",
        "The international community does not have an understanding of my country's politics." : "world",
        "All countries should be held to the same legal standard and follow international law.": "world",
        "The state has no right to have any say in any voluntary exchanges, unless they are a part of said exchanges." : "market",
        "From each according to his ability, to each according to his needs" : "equality",
        "Transhumanism and human augmentation are good things." :  "progress",
        "Rampant consumerism, degeneracy and selfishness is all too common in society." : "tradition",
        "The freedom to succeed is the freedom to fail." : "liberty",
        "It is the government's job to ensure the populace's wellbeing through any means necessary and to any extent." : "authority",
        "I am proud to be born in my country" : "nation",
        "Everyone is a citizen of the world and should act accordingly." : "world",
        "The ‘invisible hand’ is a better market operator than the government controlling the economy" : "market",
        "People of all groups should be well represented" : "equality",
        "Scientific thought should be pursued at all costs" : "progress",
        "Scientific thought is not the end all be all. It is wrong at times." : "tradition",
        "The only person who I trust to look out for myself is me." : "liberty",
        "The government should have supreme power on policy during times of crisis." : "authority",
        "I should follow my country even when they take paths I disagree with." : "nation",
        "The world should progress to a one world government of sorts." : "world"
    }
    #Asking Questions Using The Question_Asker Function.
    for question in questions:
        question_asker(question, questions[question])
    add_to_database()
# The main function is called to execute the program.
main()
