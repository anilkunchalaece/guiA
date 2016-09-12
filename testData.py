#Author : Kunchala Anil, Tanniru Surendra
#Email : anilkunchalaece
#date : Aug 27 2016
#import csv
import urllib2, urllib #used tos end post Request
import re #used to parse the Received Data
import os
import shutil


#Date : 30 Aug 2016 - Avoid the' \n\r' characters in received string
#http://stackoverflow.com/questions/1185524/how-to-trim-whitespace-including-tabs
class TestData(object):
    def __init__(self,testId,userName,userPswd):
        #f = open('anatomy_questions.csv','rt')
        #reader = csv.reader(f)
        #self.keys = [] This is useless List Not needed Anymore - 9th Sep 2016
        self.queDict = {}
        self.optADict = {}
        self.optBDict = {}
        self.optCDict = {}
        self.optDDict = {}
        self.keyDict = {} #Key Dict is used for Remapping Uid Values with Temporary key Values
        _key = 1 # used for keyDict as a Kay Value
        #imgDict and imDict uses the Normal Keywords Not Uid of Questons as Key Values
        self.imgUrlDict = {}
        self.imgQueDict = {}

        _testId = testId
        _userName = userName
        _userPswd = userPswd
                
        _mydata=[('ID',_testId),('UID',_userName),('UPSWD',_userPswd)]    #The first is the var name the second is the value
        _mydata=urllib.urlencode(_mydata)
        _path='http://www.newpythonscripts.16mb.com/new5.php'    #the url you want to POST to
        _req=urllib2.Request(_path, _mydata)
        _req.add_header("Content-type", "application/x-www-form-urlencoded")
        _page=urllib2.urlopen(_req).read()

        """
The Received Data is in the Form
<q> Uid||Question1||optA||optB||optC||optD <\q><q>Uid2||Question2||optA||optB||optC||optD<\q> .. and so on

First get the List of Question&Options
Then Cut the String in the list into Uid,Question,optA,optB,optC,optD


on 29 aug the Modification included is the Key Assigned to the Each question is Different to the Uid came from Post Request
The Automatically Added Key and Uid is added to the keyDict where key is the Question key in Exam and value is the Uid of the
Original Question

"""
        getQue = r"\<q\>(.+?)\<\/q\>" #re pattern used to split the received data into List Questions

        cutQue = r"(\d+?)\|\|(.+?)\|\|(.+?)\|\|(.+?)\|\|(.+?)\|\|(.+?)$" #re pattern used to Each question in list into Question and Options

        getImgUrl = r"src\=\"(.+?)\"" #re pattern used to check whether Question has Img Url and Parse the Url

        getImgQue = r"\>(.+?)$" #re pattern to parse question along with Question

        getTestName = r"\<m>(.+?)\<\/m\>" # re pattern used for test name
        getTestTime = r"\<t>(.+?)\<\/t\>" # re pattern used for test time

        try :

            self.testName = re.findall(getTestName,_page)[0]
            self.testTime = re.findall(getTestTime,_page)[0]

        except:
            self.testName = 'Got nothing From Web'
            self.testTime = 1

        for queOpt in re.findall(getQue,_page.translate(None,'\n\r\t')):
            for opt in re.findall(cutQue,queOpt):
                #self.keys.append(self.key) #Useless List 
                self.keyDict[str(_key)] = opt[0]

                self.queDict[str(_key)] = opt[1] #fixed bug here from previous code
                #check whether we received the Img in Question..
                self.qImg = re.findall(getImgUrl,opt[1])
                if self.qImg :
                    #If we received the Image in the Question.. we Fill the imgUrlDict andimgQueDict with Img Url and Img Question
                    #w replace the keyword as a Value in queDict to alert we got Image
                    self.imgUrlDict[str(_key)] = self.qImg[0]
                    self.imgQueDict[str(_key)] = re.findall(getImgQue,opt[1]) #fixed the bug here from previous code
                    self.queDict[str(_key)] = _key

                
                self.optADict[str(_key)] = opt[2]
                self.optBDict[str(_key)] = opt[3]
                self.optCDict[str(_key)] = opt[4]
                self.optDDict[str(_key)] = opt[5]
                _key = _key + 1
        #Get the Images and Save them in local Temp Directory if there is already Directory Delete it
        #os.mkdir("temp")  # create a temp directory ref http://www.tutorialspoint.com/python/python_files_io.htm
        if os.path.isdir('temp'):
               shutil.rmtree('temp')
        os.mkdir('temp')
        #download all the image files in questions data to temporary directory
        for key in self.imgUrlDict:
            #print key+":"+newLogic.data.imgUrlDict[key]
            #print newLogic.data.imgQueDict[key][0]
            urllib.urlretrieve(self.imgUrlDict[key],os.getcwd()+"/temp/"+str(self.keyDict[key])+".jpg")

                

        """
This is used for CSV Reader
        for row in reader:
            key = row[0]
            self.keys.append(key)
            self.queDict[str(key)] = row[1]
            self.optADict[str(key)] = row[2]
            self.optBDict[str(key)] = row[3]
            self.optCDict[str(key)] = row[4]
            self.optDDict[str(key)] = row[5]
        f.close()

        """

if __name__ == "__main__":
   
    data = TestData(104,'anil',123)
    print "no of Questions"
    print len(data.keyDict)
    #os.mkdir("temp")  # create a temp directory ref http://www.tutorialspoint.com/python/python_files_io.htm
    #print data.imgUrlDict["1"]
    """
    for key in data.imgUrlDict:
        print key+":"+data.imgUrlDict[key]
        print data.imgQueDict[key][0]
        urllib.urlretrieve(data.imgUrlDict[key],os.getcwd()+"/temp/"+str(data.keyDict[key])+".png")
    
shutil.rmtree("temp")
    """
