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
def question_asker(question, weight, issue):
    global economic, diplomatic, civil, societal, neutral, mininum, maximum
    # Ask the question
    print(question)
    answer = mininum - 1
    # Keep on asking for a value until the value fits in the range of mininum-maximum.
    while answer < mininum or answer > maximum:
        answer = int(input("On a scale of 1-7, 1 being strongly disagree, 4 being neutral, and \
7 being strongly agree, what is your opinion on this question?\n"))
    # The points are calculated depending on how strong the position is and whether the view is disagree, agree, or neutral.
    points = (weight * (answer - neutral))
    '''Issues:
       1. Economic
       2. Diplomatic
       3. Civil
       4. Societal'''
    if issue is 1:
        economic += points
    if issue is 2:
        diplomatic += points
    if issue is 3:
        civil += points
    if issue is 4:
        societal += points


# This is the main function.
def main():
    # Intialize the program.
    initialization()
    # This is a list of questions to be asked.
    questions = ["People should not be discriminated against based on intrinsic qualities in any capacity.",
                 "Progress should be pursued, even at the expense of tradition",
                 "Cultural values should be preserved and nurtured for future generations",
                 "Government is run by people with unchecked power",
                 "A large portion of people are unable to make good decisions for themselves",
                 "Unrestricted markets will result in everyone becoming wealthier.",
                 "A citizen's primary concern is with his/her nation and then the world.",
                 "National governments must be kept in check by the global community by any means necessary.",
                 "There is minimal physical and mental difference between people of different races.",
                 "We are heading to a better world.",
                 "New change should be implemented slowly",
                 "Victimless crimes should not be illegal.",
                 "Maintaining order is more important than preserving all freedoms.",
                 "The international community does not have an understanding of my country's politics.",
                 "All countries should be held to the same legal standard and follow international law.",
                 "The state has no right to have any say in any voluntary exchanges, unless they are a part of said exchanges.",
                 "From each according to his ability, to each according to his needs",
                 "Transhumanism and human augmentation are good things.",
                 "Rampant consumerism, degeneracy and selfishness is all too common in society.",
                 "The freedom to succeed is the freedom to fail.",
                 "It is the government's job to ensure the populace's wellbeing through any means necessary and to any extent.",
                 "I am proud to be born in my country",
                 "Everyone is a citizen of the world and should act accordingly.",
                 "The ‘invisible hand’ is a better market operator than the government controlling the economy",
                 "People of all groups should be well represented"]
    # These are weights regarding the above questions.
    weights = [1, -1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1, -1, -1, 1]
    # These are the specific issues the questions are related to.
    issues = [1, 4, 4, 3, 3, 1, 2, 2, 1, 4, 4, 3, 3, 4, 4, 1, 1, 4, 4, 3, 3, 2, 2, 1, 1]
    # This for loop asks all the questions.
    for i in range(0, len(questions)):
        question_asker(questions[i], weights[i], issues[i])


# The main function is called to execute the program.
main()
