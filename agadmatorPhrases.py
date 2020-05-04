#AviationFreak / PhysicsLover999
#April 14, 2020

from youtube_transcript_api import YouTubeTranscriptApi
import re, time

videoID = input("Input the video ID: ")

phrases = [ #List of phrases that should be noted in the transcript
"captures captures", "captors captures", "captors captures", "captors captors", "captures and captures", "captors and captures", "captures and captors", "captors and captors",
"it was in this position", "twas in this position",
"hello everyone",
"never repeated again", "never again repeated",
"completely new game", "a completely new position", "a new position",
"bust open the position", "busting open the position",
"give you a couple of seconds", "give you a couple seconds",
"just want to enjoy the show", "just wanna enjoy the show",
"check check check", "church church church",
"sorry about that", "sorry bout that"
]

transcript = YouTubeTranscriptApi.get_transcript(videoID)

def getCorrection(phraseIndex): #Corrects phrases that the transcript "misheard"
    if phraseIndex <= 7:
        return "captures captures"
    elif phraseIndex <= 9:
        return "it was in this position"
    elif phraseIndex <= 10:
        return "hello everyone"
    elif phraseIndex <= 12:
        return "never repeated again"
    elif phraseIndex <= 15:
        return "completely new game"
    elif phraseIndex <= 17:
        return "busting open the position"
    elif phraseIndex <= 19:
        return "give you a couple of seconds"
    elif phraseIndex <= 21:
        return "for those who just want to enjoy the show"
    elif phraseIndex <= 23:
        return "check check check"
    elif phraseIndex <= 25:
        return "sorry about that"

text = ""
indexCounter = 1
moments = []

for x in range(len(transcript)):
    text += " " + transcript[x]["text"].lower()
    transcript[x].update({"index" : indexCounter})
    indexCounter = len(text)

for x in range(len(phrases)):
    indices = [m.start() for m in re.finditer(phrases[x], text)]
    if len(indices) > 0:
        for y in range(len(indices)):
            indexNum = indices[y]
            foundMatch = False
            while not foundMatch:
                for z in range(len(transcript)):
                    if transcript[z]["index"] == indexNum:
                        foundMatch = True
                        startTime = transcript[z]["start"]
                        startTime = time.strftime('%M:%S', time.gmtime(startTime))
                        if (indexNum, startTime, getCorrection(x)) not in moments:
                            moments.append((indexNum, startTime, getCorrection(x)))
                indexNum -= 1

moments.sort()

for x in range(len(moments)):
    print(moments[x][2], moments[x][1])
