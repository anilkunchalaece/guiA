#Author : Kunchala Anil
#Date : 28 Aug 2016
#Email : anilkunchalaece@gmail.com

#Check the Automatic Button Genration Clearly - Ref guiAnilV3.py

#Import the Layout
from orgLayout import Ui_prepare2Pg
#import csv for TestData
import csv
#import the TestData
from testData import TestData
#import Ui_testCompleted from completed which is closing dialog Ui
from completed import Ui_testCompleted
#import the Login Dialog
from login import Ui_Login
#import the Terms and Condition Dialog
from terms import Ui_Terms

#Import the PyQt Core and Gui Libraries
from PyQt4 import QtCore, QtGui
import os  # to get the files path etc..
import shutil # to remove temporary directory after exam ending
import json #used for post request to send the Result Dict
import urllib2, urllib

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
"""
The Function of Buttons are as follows:

PREVIOUS BUTTON :
    it is used to move to i.e displays the previous Question

NEXT BUTTON :
    it is used to move to i.e displays the next question

SUBMIT BUTTON ;
    it is used to submit the Answer for the respective Question
    when user clicks the submit button, it changes the color to green
    
MARK FOR REVIEW :
    it is used to select the Respective question to review later. When User clicks this button
    respective button changes the color to red

END TEST :
    this is used to display the "resDict" which stores the Uid as key and user option as Value


Question Index is the anchor of total Program we use Question Index to Move to the Next and Previous Question

In Scroll area Buttons are created using the for loop.
Each button name i.e text is set as its Uid Number so we will make a dict "btn" and store the Uid as key and
and generated object as value. it is useful when we try to access the questions when corresponding button is clicked
in scroll area

TestData Object will generate a Few instanece Variable named as queDict,optADict,optBDict,
optCDict.optDDict and keys which holds the Question,optA,optB,optC,optD as Dictionaries where keys
is the key value for Each Dict variables


"""

class guiLogic(Ui_prepare2Pg):
    def __init__(self):
        self.questionIndex = 1 #variable to hold the questionIndex it is hero of our movie
        
  
        self.rows = 4 # it is used to hold the  max no of rows we want in scroll widget
        self.rowAddition = self.rows #this is just a copy of rows value which is used in Automatic generation of btn's in Scroll Area
        self.resultDict = { } # it holds the user selected Options
        self.selectedOption = 'n' # Default option
        self.x = 0 # x and y values supply as co-ordinates in grid layout in Scroll widget 
        self.y = 0
        self.btn = {} #this will hold the ScrollArea Btn's with name and Object as Key and Value Pairs
        self.addImagesForLegendBtns()
        
        
        # answered = 'a' 
        # notVisited = 'b'
        # answeredAndMarkedForReview= 'c'
        # notAnsweredBtn = 'd'
        # markedForReview = 'e'

        self.statusDict = {}
 
       

        #we are Creating login Class within the guiLogic Class since we need to access the Variables in the login Screen Class with in the guiLogic Class
        
        self.loginScreen = Ui_Login()
        self.loginScreen.setupUi(loginDialog)
        loginDialog.show()


        self.termsScreen = Ui_Terms()
        self.termsScreen.setupUi(termsDialog)
        #setup Login Screen
        self.setupLogin()

       
    def setupLogin(self):

        self.loginScreen.loginBtn.clicked.connect(self.loginFcn)


    def loginFcn(self):
        print "Login Btn is Clicked"
         
        self.userName = str(self.loginScreen.username_txt.text())
        _userPswd = str(self.loginScreen.pass_txt.text())
        self.userTId = str(self.loginScreen.tid_txt.text())

        print self.userName
        print _userPswd
        print self.userTId
        
       
        self.data = TestData(self.userTId,self.userName,_userPswd) # Create a TestData Object which supply necessary Ingredients
        self.data.maxQuestions = len(self.data.queDict)
        if self.data.maxQuestions == 0:
            print "I got Zero Questions"
            print "username || Password || Test Id is wrong"
            self.loginScreen.invalidLogin.setText("Invalid User name or Password")
        else :
            loginDialog.close() # Close the login Dialog
            termsDialog.show() #Show the Terms Dialog

        self.termsScreen.pushButton.clicked.connect(self.termsBtnFcn)
        
    def termsBtnFcn(self):
        print "Next Btn in Terms is Clicked"
        if self.termsScreen.checkBox.isChecked():
            termsDialog.close() #Close the Terms Dialog
            print "User Accepted Terms and Conditions"
            self.addScrollArea() #add scroll area when object is called
            self.setupLogic()#start the logic.. (I dont find a Good name for that method)
            #we are Getting the time as Str in Minutes. So Convert it into seconds and make type Int
            self.timerValue = int(self.data.testTime)*60

            MainWindow.show() # Open the MainWindow
            self.startTimer() # Start the timer Only After showing MainWindow

            ui.examTitle.setHtml('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Roboto'; font-size:12pt; font-weight:200; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'MS Shell Dlg 2'; font-size:26pt; font-weight:400; color:#aa5500;">''' + self.data.testName + '''</span></p></body></html>''')
            newLogic.retranslateUi(newLogic.questionIndex)
        else:
            print "Please accept Terms and Conditions"
            self.termsScreen.termsLabel.setText('Please check the terms accepted checkbox')
        
    def addImagesForLegendBtns(self):
        ui.answerdBtn.setStyleSheet("QPushButton{ background-image: url(btnImages/answeredBtnImg.png); }")
        ui.notVisited.setStyleSheet("QPushButton{ background-image: url(btnImages/notVisitedImg.png); }")
        ui.answeredAndMarkedForReview.setStyleSheet("QPushButton{ background-image: url(btnImages/answeredAndMarkedForReviewImg.png); }")
        ui.notAnswerdBtn.setStyleSheet("QPushButton{ background-image: url(btnImages/unansweredImg.png); }")
        ui.markedForReview.setStyleSheet("QPushButton{ background-image: url(btnImages/markredForReviewImg.png); }")

    def addScrollArea(self):
        for key in range (len(self.data.keyDict)):
            self.btnKey = str(key+1) #added 1 to key since for loop starts from '0' and Question Index starts from 1
            self.btn[self.btnKey] = QtGui.QPushButton(ui.scrollAreaWidgetContents) # generate pushbutton object and add that object to dictionary for future Reference
            self.btn[self.btnKey].setMaximumSize(QtCore.QSize(40, 40))
            self.btn[self.btnKey].setMinimumSize(QtCore.QSize(40,40))
            self.btn[self.btnKey].setStyleSheet("QPushButton{ background-image: url(btnImages/notVisitedImg.png); }")#Mark All Questions as UnVisited
            self.btnText = str(key+1) #set the text as key value which is used as reference to Respectiv Question
            self.btn[self.btnKey].setText(self.btnText) #Add the test to the btn
            #self.btn[self.btnKey].setCheckable(True)
            #self.btn.setMaximumSize(QtCore.QSize(100, 70))
            self.btn[self.btnKey].toggle()
            self.btn[self.btnKey].clicked.connect(self.scrollFcn) #Add the event handler to the Btn.. all the Btns in Scroll area are assigned to same Callback Function i.e scrollFcn
        #Take some time and look at this Logic.. it eats more time for me
            if key < self.rows:
                if key == 0:
                    self.y = 0
                    self.x = 0
                else:
                    self.y = self.y + 1

            else:
                self.x = self.x+1
                self.y = 0
                self.rows = self.rows + self.rowAddition #Particularly this line
#           print "x" + str(self.x)
#            print "y" + str(self.y)
#            print "key" + str(key)
#            print "self.rows" + str(self.rows)
            
            ui.gridLayout.addWidget(self.btn[self.btnKey],self.x,self.y) # Add the Button to Widget
#            print self.btn[self.btnKey]

    def scrollFcn(self):
        print "Scroll Btn Clicked"
        print MainWindow.sender().text() #this will grab the Pushbutton Reference Object From Mainwindow which is used to access the Btn Data
        #when the scroll Btn is Pressed with Reference Key Id call retranslateUi with key function
        self.questionIndex = int(MainWindow.sender().text())# from the Object get the Text of Function which is Same as Uid of Question

        self.statusDict[self.questionIndex] = 'd'

        self.retranslateUi(self.questionIndex) # Display the respscted QUestion using Question Index
        self.showPreviosOption(self.questionIndex)
        
        

    def showPreviosOption(self,QIndex):
        #TO Highlight the user Selected Option If user Comes back - Check Issue : https://github.com/anilkunchalaece/pyQtGuiImproved/issues/1
        checked = self.resultDict.get(QIndex,False)
        if checked:
            print checked
            if checked == 'A':
                ui.optARadioButton.setChecked(True)
            elif checked == 'B':
                ui.optBRadioButton.setChecked(True)
            elif checked == 'C':
                ui.optCRadioButton.setChecked(True)
            elif checked == 'D':
                ui.optDRadioButton.setChecked(True)
                
                

    def updateLcd(self):
        ##http://stackoverflow.com/questions/775049/python-time-seconds-to-hms
        # this function increments the self.timerValue variable which is converted to hh:mm:ss 
        _m, _s = divmod(self.timerValue, 60)
        _h, _m = divmod(_m, 60)

        if _m < 10:
            _m = '0'+str(_m)
        if _h < 10 :
            _h = '0'+str(_h)
        if _s < 10:
            _s = '0'+str(_s)
        
        timeValue = str(_h) + ':' + str(_m)+':'+str(_s)

        ui.timeRemaining.setHtml('''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Roboto'; font-size:12pt; font-weight:200; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-family:'MS Shell Dlg 2'; font-weight:600; color:#0055ff;">TIME REMAINING : ''' + timeValue + '''</span></p></body></html>''')

        self.timerValue = self.timerValue - 1

        if self.timerValue == 0:
           #when time is Completed we are hiding the mainwindow and Showing the Dialog Button
            self.closeExam()
#Exam Closing Fucntion
    def closeExam(self):
        MainWindow.hide()
        exitDialog.show()
             

    def startTimer(self):
        #Start the timer at the Begining of the Test
        #for every 1 sec call the updateLcd Function 
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateLcd)
        self.timer.start(1000) 
    
    def setupLogic(self):
        #Assign the Duties for Buttons
        ui.reviewAndNextBtn.clicked.connect(self.reviewAndNextFcn)
        ui.clrResponseBtn.clicked.connect(self.clrResponseFcn)
        ui.saveAndNextBtn.clicked.connect(self.saveAndNextFcn)
        ui.submitBtn.clicked.connect(self.submitFcn)
        
      
    def reviewAndNextFcn(self):
       
        print "Review and Next Btn is Clicked"

        if ui.optARadioButton.isChecked():
            print "Option A is Selected"
            self.selectedOption = 'A'
        elif ui.optBRadioButton.isChecked():
            print "Option Bis Selected"
            self.selectedOption = 'B'
        elif ui.optCRadioButton.isChecked():
            print "Option C is Selected"
            self.selectedOption = 'C'
        elif ui.optDRadioButton.isChecked():
            print"Option D is Selected"
            self.selectedOption = 'D'
        else:
            print "No Option selected"
            self.selectedOption = 'N'
        
        self.resultDict[str(self.questionIndex)] = self.selectedOption #Store the Result in Dict

        if self.selectedOption == 'N':
            self.btn[str(self.questionIndex)].setStyleSheet("QPushButton{ background-image: url(btnImages/markredForReviewImg.png); }")
            self.statusDict[self.questionIndex] = 'e' #Marked for Review
        else :
            self.btn[str(self.questionIndex)].setStyleSheet("QPushButton{ background-image: url(btnImages/answeredAndMarkedForReviewImg.png); }")
            self.statusDict[self.questionIndex] = 'c' #answred and Marked for Review
            
        self.moveToNextQuestion()


    def clrResponseFcn(self):
        #when Review Btn is Pressed change the color of respective Btn
        print "clr Response Function Selected"
        
        #Change the icon
        self.btn[str(self.questionIndex)].setStyleSheet("QPushButton{ background-image: url(btnImages/unansweredImg.png); }")
        #update the CheckButtons
        ui.buttonGroup.setExclusive(False)
        ui.optARadioButton.setChecked(False)
        ui.optBRadioButton.setChecked(False)
        ui.optCRadioButton.setChecked(False)
        ui.optDRadioButton.setChecked(False)
        ui.buttonGroup.setExclusive(True)
        #Update the resultDict
        self.resultDict[str(self.questionIndex)] = 'N'

        self.statusDict[self.questionIndex] = 'd' # Not Answered 
                  

        
    def saveAndNextFcn(self):
        # When submit button is pressed see which of the toggle button is checked and select the option accordingly
        # and the store the respective value to the resulDict with QIndex as Key
        # then Change the color of the Respective Button is Scroll btn usinf Qindex 
        
        print "Save and Next Function is Selected Btn Pressed"

        if ui.optARadioButton.isChecked():
            print "Option A is Selected"
            self.selectedOption = 'A'
        elif ui.optBRadioButton.isChecked():
            print "Option Bis Selected"
            self.selectedOption = 'B'
        elif ui.optCRadioButton.isChecked():
            print "Option C is Selected"
            self.selectedOption = 'C'
        elif ui.optDRadioButton.isChecked():
            print"Option D is Selected"
            self.selectedOption = 'D'
        else:
            print "No Option selected"
            self.selectedOption = 'N'
            
        self.resultDict[str(self.questionIndex)] = self.selectedOption #Store the Result in Dict
        if self.selectedOption == 'N':
            self.btn[str(self.questionIndex)].setStyleSheet("QPushButton{ background-image: url(btnImages/unansweredImg.png); }")
            
            self.statusDict[self.questionIndex] = 'd'#unanswered
        else :
            self.btn[str(self.questionIndex)].setStyleSheet("QPushButton{ background-image: url(btnImages/answeredBtnImg.png); }")
            self.statusDict[self.questionIndex] = 'a'
            
        self.moveToNextQuestion()

    def moveToNextQuestion(self):
         #This function increment the questionIndex and Display the Question using Index
        self.questionIndex=newLogic.questionIndex+1
        if self.questionIndex > self.data.maxQuestions :
            self.questionIndex = 1
        self.statusDict[self.questionIndex] = 'd'
        self.retranslateUi(newLogic.questionIndex)
        self.showPreviosOption(self.questionIndex)

        
    def submitFcn(self):
        #when endTest btn is clicked Print the Resulting Dict
        #Do the Remapping qId's with uId's and store the Uid's and Corresponding option Strings in the _outputDict
        
        print "endTest Btn Pressed"
        print "Output Dict is "
        print self.resultDict #Result Dict used in Program
        _outputDict = {}
#To Indicate the unattempted and Unanswwered questions as Nothing selected I need to change the For loop below
#i need to check for each key in key dict 

        for key in self.data.keyDict :
            _uId = self.data.keyDict[str(key)]#get the Corresponding UId for qId

            if key in self.resultDict :
               
                _opt = self.resultDict[key]#get the selected option
           

                if _opt == 'A':
                    _outputDict[_uId] = self.data.optADict[str(key)]
                elif _opt == 'B':
                    _outputDict[_uId] = self.data.optBDict[str(key)]
                elif _opt == 'C':
                    _outputDict[_uId] = self.data.optCDict[str(key)]
                elif _opt == 'D':
                    _outputDict[_uId] = self.data.optDDict[str(key)]
                elif _opt == 'N':
                    _outputDict[_uId] = 'Nothing Selected'
            else :
                _outputDict[_uId] = 'Nothing Selected'
            #print outputDict
        print 'Dict sent to Via Post Request is'       
        print _outputDict
        
#sending the result via Post Request
        _outputPost = json.dumps(_outputDict)
        _postData = [('dict',_outputPost),('uName',self.userName),('tId',self.userTId)]
        _postData = urllib.urlencode(_postData)
        _req = urllib2.Request('http://www.newpythonscripts.16mb.com/new6.php',_postData)
        _req.add_header("Content-type", "application/x-www-form-urlencoded")
        _page=urllib2.urlopen(_req).read()

        print 'result is'
        print _page

        shutil.rmtree("temp") # delete the temporary directory
        self.closeExam()

    def retranslateUi(self,QIndex):
        #this function takes QIndex as argument
        #where Qindex is Key value in Data
        #using key values we set the Text of Question label and optA,B,C and D Radio Buttons 
#        ui.testNameLabel.setText(_translate("prepare2Pg", "TEST NAME", None))

        #for Question first we are checking the type of Question whether it is a img oriented q?
        x = str(newLogic.data.queDict[str(QIndex)])
        y = str(QIndex)
        
        checked = self.resultDict.get(QIndex,False)
        if checked == False:
            self.btn[str(self.questionIndex)].setStyleSheet("QPushButton{ background-image: url(btnImages/unansweredImg.png); }")

        if x==y:  # if the key and value are same then its a img oriented question
            htmlQuestion = '''<html>
                        <head>
                        <title>A Sample Page</title>
                        </head>
                        <body>
                        <img src="'''+os.getcwd()+'''/temp/'''+str(newLogic.data.keyDict[str(QIndex)])+'''.jpg" align="middle">
                        '''+str(newLogic.data.imgQueDict[str(QIndex)][0])+'''
                        </body>
                        </html>'''
        else:
             htmlQuestion =  '''<html>
                        <head>
                        <title>A Sample Page</title>
                        </head>
                        <body><p style="position: fixed; bottom: 0; width:100%;"><b>Q:)</b>
                        '''+str(newLogic.data.queDict[str(QIndex)])+'''
                        </p></body>
                        </html>'''
        ui.QuestionLabel.setHtml(htmlQuestion)

        htmlQNo = '''
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600; color:#0055ff;">  QUESTION NO  : ''' + str(self.questionIndex) +'''</span></p></body></html>
'''
        ui.questionNo.setHtml(htmlQNo)
        
        #img = open('123.png', 'rb').read()
        #ui.QuestionLabel.setContent(img, 'image/png')
        #ui.QuestionLabel.setText(_translate("prepare2Pg", newLogic.data.queDict[str(QIndex)], None))
        ui.optARadioButton.setText(_translate("prepare2Pg", newLogic.data.optADict[str(QIndex)], None))
        ui.optBRadioButton.setText(_translate("prepare2Pg", newLogic.data.optBDict[str(QIndex)], None))
        ui.optCRadioButton.setText(_translate("prepare2Pg", newLogic.data.optCDict[str(QIndex)], None))
        ui.optDRadioButton.setText(_translate("prepare2Pg", newLogic.data.optDDict[str(QIndex)], None))
        
        #this logic has to be worked On.. This is A "BUG" i cant Find - Solved
        # Aug 28 -Create A Button Group - http://stackoverflow.com/questions/29270307/how-can-i-change-the-name-of-a-qbuttongroup-in-qt-designer
        # http://stackoverflow.com/questions/8689909/uncheck-radiobutton-pyqt4
        ui.buttonGroup.setExclusive(False)
        ui.optARadioButton.setChecked(False)
        ui.optBRadioButton.setChecked(False)
        ui.optCRadioButton.setChecked(False)
        ui.optDRadioButton.setChecked(False)
        ui.buttonGroup.setExclusive(True)

                
        # answered = 'a' 
        # notVisited = 'b'
        # answeredAndMarkedForReview= 'c'
        # notAnsweredBtn = 'd'
        # markedForReview = 'e'

        totalA = 0
        totalC = 0
        totalD = 1
        totalE = 0
        #totalB = 1

        for k in self.statusDict:
            status = self.statusDict[k]
            if status == 'a':
                totalA = totalA + 1
            elif status == 'c':
                totalC = totalC+1
            elif status == 'd':
                totalD = totalD+1
            else:
                totalE = totalE+1

        print totalA
        print totalC
        print totalD
        print totalE

        totalB= self.data.maxQuestions - totalA-totalC-totalD-totalE
                


        ui.answerdBtn.setText(str( totalA))
      
        ui.answeredAndMarkedForReview.setText(str(totalC))
        ui.notAnswerdBtn.setText(str(totalD))
        ui.markedForReview.setText(str(totalE))
        
        ui.notVisited.setText(str(totalB))
        


if __name__ == "__main__":
    import sys
    import os
    import urllib2, urllib
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    exitDialog = QtGui.QDialog()
   

    
    ui = Ui_prepare2Pg()
    ui.setupUi(MainWindow)

    loginDialog = QtGui.QDialog()
    termsDialog = QtGui.QDialog()
    
    newLogic = guiLogic()
    
    testCompleted = Ui_testCompleted()
    testCompleted.setupUi(exitDialog)

    

   
    sys.exit(app.exec_())

  
