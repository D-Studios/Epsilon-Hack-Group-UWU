
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
    points = (weight * (answer - neutral))
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

# This is the main function.
def main():
    # Intialize the program.
    initialization()
    '''
    equality   nation   liberty     tradition
    market     world    authority   progress    
    '''
    #Questions are asked and are appropiated labeled based on category.
    question_asker("People should not be discriminated against based on intrinsic qualities in any capacity.", "equality")
    question_asker("Progress should be pursued, even at the expense of tradition", "progress")
    question_asker("Cultural values should be preserved and nurtured for future generations", "tradition")
    question_asker("Government is run by people with unchecked power", "liberty")
    question_asker("A large portion of people are unable to make good decisions for themselves", "authority")
    question_asker("Unrestricted markets will result in everyone becoming wealthier.", "market")
    question_asker("A citizen's primary concern is with his/her nation and then the world.", "nation")
    question_asker("National governments must be kept in check by the global community by any means necessary.", "world")
    question_asker("There is minimal physical and mental difference between people of different races.", "equality")
    question_asker("We are heading to a better world.", "progress")
    question_asker("New change should be implemented slowly", "tradition")
    question_asker("Victimless crimes should not be illegal.", "liberty")
    question_asker("Maintaining order is more important than preserving all freedoms.", "authority")
    question_asker("The international community does not have an understanding of my country's politics.", "world")
    question_asker("All countries should be held to the same legal standard and follow international law.", "world")
    question_asker("The state has no right to have any say in any voluntary exchanges, unless they are a part of said exchanges.", "market")
    question_asker("From each according to his ability, to each according to his needs", "equality")
    question_asker("Transhumanism and human augmentation are good things.", "progress")
    question_asker("Rampant consumerism, degeneracy and selfishness is all too common in society.", "tradition")
    question_asker("The freedom to succeed is the freedom to fail.", "liberty")
    question_asker("It is the government's job to ensure the populace's wellbeing through any means necessary and to any extent.", "authority")
    question_asker("I am proud to be born in my country", "nation")
    question_asker("Everyone is a citizen of the world and should act accordingly.", "world")
    question_asker("The ‘invisible hand’ is a better market operator than the government controlling the economy", "market")
    question_asker("People of all groups should be well represented", "equality")
    question_asker("Scientific thought should be pursued at all costs", "progress")
    question_asker("Scientific thought is not the end all be all. It is wrong at times.", "tradition")
    question_asker("The only person who I trust to look out for myself is me.", "liberty")
    question_asker("The government should have supreme power on policy during times of crisis.", "authority")
    question_asker("I should follow my country even when they take paths I disagree with.", "nation")
    question_asker("The world should progress to a one world government of sorts.", "world")

# The main function is called to execute the program.
main()
