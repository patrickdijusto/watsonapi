import json
import datetime
import re
from unicodedata import normalize
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import WatsonApiException
import twitter
from settings import *

global api
## Run entire twitter infrasctucture

print('establish the twitter object')
# see "Authentication" section below for tokens and keys
api = twitter.Api(consumer_key=CONSUMER_KEY,
	consumer_secret=CONSUMER_SECRET,
	access_token_key=OAUTH_TOKEN,
	access_token_secret=OAUTH_SECRET,
    )

print('twitter object established')

def getPast():
	## open file
	## 	Read # of previous tweet
	## Close file?

	try:
		flx = open('pastNumber.txt',"r")
	except:
		flx = open('pastNumber.txt',"w")
		flx.write("0")
		flx.close()
		flx = open('pastNumber.txt',"r")
		
	
	row = flx.read()

	flx.close()

	writeLog("Writing past number: ", int(row), "w")
	               
	return int(row)

def getCurrent(pastNumber):
	
	##Contact twitter
	## Read Trump's most recent tweet
	## Extract Tweet ID Number

	putput=[]
	
	
	St = api.GetUserTimeline(0,"realDonaldTrump",pastNumber,0,1)
	
	writeLog("Gotten current: ", 1, "a")

	print("And now we print the Status of the last Tweet")
	print(St)
		
	print("And now just the first entry")
	print (St[0].id)
	putput.append(St[0].id)


	
	print("and now just the text")
	# mid_text = normalize('NFKD', St[0].text).encode('ascii','ignore')
	
	# midi_text = re.sub(r'https://\S+', '', mid_text)
	
	# out_text = re.sub(r'@\S+', '', midi_text)
	
	# mid_text = normalize('NFKD', St[0].text).encode('ascii','ignore')
	
	# midi_text = re.sub(r'https://\S+', '', normalize('NFKD', St[0].text).encode('ascii','ignore'))
	
	mid_text = re.sub(r'@\S+', '', re.sub(r'https://\S+', '', normalize('NFKD', St[0].text).encode('ascii','ignore')))
	
	out_text = mid_text.lstrip()
	
	
	print(out_text)
	putput.append(out_text)

	
	return putput
	
	
	
	

def writePast(ccc):
        flx = open('pastNumber.txt', "w")
        flx.write(str(ccc))
        flx.close()
        writeLog("writing past: ", int(ccc), "a")

		
def writeLog(TweetText, currentNumber, mode):

        print("Writing a log...")
        now = datetime.datetime.now()
        message = "\n"+str(now)
        
        fly = open("writeLog.txt", mode)
        fly.write(message)
        fly.write(TweetText)
        fly.write(str(currentNumber))
        fly.close()

pastNumber = getPast()

print ("Past number is:")

print (pastNumber)

outlist = getCurrent(pastNumber)

print(outlist)

writePast(outlist[0])


# if (currentNumber > pastNumber):
        # postReply(TweetText, currentNumber)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='419a0281-d84a-4281-bc03-3def84761f7f',
    password='aTC4VyXndf2v'
)


tone_analyzer.set_url('https://gateway.watsonplatform.net/tone-analyzer/api')

tone_analyzer.set_detailed_response(False)










# text = 'Team, I know that times are tough! Product sales have been disappointing for the past three quarters. We have a competitive product, but we need to do a better job of selling it!'
content_type = 'application/json'

# ##text = "When in the course of human events, it becomes necessary to one people to dissolve the political bands which have connected them with another, a decent respect for the opinions of mankind compels them to list the reasons for their separation."

# # content_type = 'text/plain'

try:
	tone = tone_analyzer.tone({"text": outlist[1]},content_type, True)
except WatsonApiException as ex:
#except:
    print "Method failed with status code " + str(ex.code) + ": " + ex.message
	#print("Failure!")


##print(tone)	
print(json.dumps(tone, indent=2))
