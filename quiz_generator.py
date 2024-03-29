#! python3
#This program generates 35 shuffled quizzes with each quiz containing 29 questions on states and capitals
#and the options of each question in different quizzes are also shuffled 
#It also generates the anser keys for the same
import random

stateCapitals = {
    'Karnataka':'Bengaluru',
    'Kerala':'Thiruvananthapuram',
    'Tamil Nadu':'Chennai',
    'Maharashtra':'Mumbai',
    'West Bengal':'Kolkata',
    'Uttar Pradesh':'Lucknow',
    'Goa':'Panaji',
    'Telangana':'Hyderabad',
    'Andhra Pradesh':'Amaravati',
    'Arunachal Pradesh':'Itanagar',
    'Assam':'Dispur',
    'Bihar':'Patna',
    'Chattisgarh':'Raipur',
    'Gujarat':'Gandhinagar',
    'Haryana':'Chandigarh',
    'Himachal Pradesh':'Shimla',
    'Jammu and Kashmir':'Srinagar',
    'Jharkhand':'Ranchi',
    'Madhya Pradesh':'Bhopal',
    'Manipur':'Imphal',
    'Meghalaya':'Shillong',
    'Mizoram':'Aizawl',
    'Nagaland':'Kohima',
    'Odisha':'Bhubaneshwar',
    'Punjab':'Chandigarh',
    'Rajasthan':'Jaipur',
    'Sikkim':'Gangtok',
    'Tripura':'Agartala',
    'Uttarakhand':'Dehradun',
}

for quizNum in range(35):
    quizFile = open('States_n_capitals_quiz%s.txt' %(quizNum+1),'w')
    answerFile = open('States_n_capitals_answers%s.txt' %(quizNum+1),'w')

    quizFile.write('Name:\nRoll No:\n')
    quizFile.write(' '*20+'States and Capitals Quiz (Form %s)\n\n' %(quizNum+1))

    states=list(stateCapitals.keys())
    random.shuffle(states)

    for questionNum in range(29):
        correctAnswer = stateCapitals[states[questionNum]]
        wrongAnswers = list(stateCapitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        #write the questions and answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' %(questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('  %s. %s\n' %('abcd'[i], answerOptions[i]))
        quizFile.write('\n')

        #write correct answers to answer key file
        answerFile.write('%s. %s\n' %(questionNum+1, 'abcd'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerFile.close()
 


