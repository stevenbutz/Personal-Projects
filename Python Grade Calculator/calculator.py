

#All the weighted categories for my math class

originalWeights = [.14,.14,.14,.14,.14,.3]   #   [HW,QUIZ,EX1,EX2,EX3,FINAL]:

# homeworkWeight = .14
# quizWeight = .14
# exam1Weight = .14
# exam2Weight = .14
# exam3Weight = .14
# finalExamWeight = .30


#Array to add inputed scores to 
originalScores = []


# How much information you have to adjust scale
onlyThings = int(input("How many exams have you done 1-4? "))+2

#total to add percents to 
total = 0

i = 0# Used by the while loop to ask questions for inputs

while i < onlyThings: # loop with many if statements for questions about grades based on how many exams are done
    if i == 0:
        homeworkScore = input("What is your Homeowrk score? ")
        originalScores.append(homeworkScore)
    if i == 1:
        quizScore = input("What is your Quiz score? ")
        originalScores.append(quizScore)
    if i == 2:
        exam1Score = input("What is your Exam 1 score? ")
        originalScores.append(exam1Score)
    if i== 3:
        exam2Score = input("What is your Exam 2 score? ")
        originalScores.append(exam2Score)
    if i == 4:
        exam3Score = input("What is your Exam 3 score? ")
        originalScores.append(exam3Score)
    if i == 5:
        finalExamScore = input("What is your Final Exam score? ")
        originalScores.append(finalExamScore)
    i +=1
    

def newWeightsAndPercents(weight, score, howManyDone):
    newWeight = weight/(howManyDone*weight)
    # print("new weight: "+str(newWeight))
    return float(score) * newWeight

j = 0 # second while loop to calculate total 
while j < onlyThings:
    total += newWeightsAndPercents(originalWeights[j],float(originalScores[j]),onlyThings)
    j+=1




print("Your grade is: "+str(total))