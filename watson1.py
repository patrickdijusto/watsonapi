# watson credentials

  # "url": "https://gateway.watsonplatform.net/tone-analyzer/api",
  # "username": "419a0281-d84a-4281-bc03-3def84761f7f",
  # "password": "aTC4VyXndf2v"

import json
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import WatsonApiException




tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='419a0281-d84a-4281-bc03-3def84761f7f',
    password='aTC4VyXndf2v'
)


tone_analyzer.set_url('https://gateway.watsonplatform.net/tone-analyzer/api')

tone_analyzer.set_detailed_response(False)


#text = 'Team, I know that times are tough! Product sales have been disappointing for the past three quarters. We have a competitive product, but we need to do a better job of selling it!'
content_type = 'application/json'

text = "Go to the darkest sky you can find. A beach is great. Near a park or cemetery is good, too. If the sky is overcast, you will not see the planets. I actually have to say this. The planets will be visible in this pattern all week. Keep looking up!"

# content_type = 'text/plain'

try:
	tone = tone_analyzer.tone({"text": text},content_type, True)
except WatsonApiException as ex:
    print "Method failed with status code " + str(ex.code) + ": " + ex.message
	


print(tone)	
## Access response from methodName
print(json.dumps(tone, indent=2))
