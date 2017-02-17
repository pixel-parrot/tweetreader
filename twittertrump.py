import os, sys
import pygame
import wave
import contextlib
import config
from twitter import *
import subprocess

os.chdir('/tweetreader/')
#print os.getcwd()


def stripPunctuation(word_list = []):
    #print str(word_list)
    for index, word in enumerate(word_list):
        letter_list = list(word)
        #print str(letter_list)
        letter_list = [letter for letter in letter_list if letter.isalpha()]
        #print str(letter_list)
        word_list[index] = ''.join(letter_list)
    #print str(word_list)

    return word_list


def playSound(word_list = []):
    pygame.mixer.init()
    wav_list = word_list 
    #print str(wav_list)
    wav_list = stripPunctuation(wav_list)
    wav_list = [word + '.wav' for word in wav_list]
    wav_list = [word.lower() for word in wav_list]
    #print str(wav_list)

    for wav_file in wav_list:
        #creating sound object
        sound = pygame.mixer.Sound(os.path.join('sounds/', wav_file))

        # creating sound file string to test if it exists
        sound_file = os.path.join('sounds/', wav_file)
        # checking if sound file exists for each word
        try:
            contextlib.closing(wave.open(sound_file, 'r'))
        except:
            print 'No such file exists: ' + sound_file
            continue

        # playing each sound sequentially
        if pygame.mixer.Channel(0).get_busy() == False:
            sound.play()
        while pygame.mixer.Channel(0).get_busy() == True:
            continue


def getTimeline():
    config = {}
    config_path = os.path.join('config.py')
    execfile(config_path, config)

    twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

    user = "realDonaldTrump"

    results = twitter.statuses.user_timeline(screen_name = user)

#    for status in results:
#        print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))

    # example of how to reference just text in a tweet
#    for i in range(0,1):
#        print results[i]["text"]

    for i in range(0,1):
        text_list = results[i]["text"].split()
        #print str(text_list)
        playSound(text_list)


def getTimelineTest():
    config = {}
    config_path = os.path.join('config.py')
    execfile(config_path, config)

    twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

    user = "realDonaldTrump"

    results = twitter.statuses.user_timeline(screen_name = user)

#    for status in results:
#        print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))

    # example of how to reference just text in a tweet
#    for i in range(0,1):
#        print results[i]["text"]

    while True:
        tweet_number = raw_input("Enter Tweet Number: ")

        if tweet_number <> 'xit':
            tweet_int = int(tweet_number)
            tweet_start = tweet_int - 1

            for i in range(tweet_start, tweet_int):
                text_list = results[i]["text"].split()
                text_string = ' '.join(text_list)
                print str('Tweet Text: ' + text_string)
                playSound(text_list)
        else:
            return False


def soundTest(test_sounds = []):
    playSound(test_sounds)


def testLoop():
    test_string = ""

    while test_string <> "xit":
        test_string = raw_input("Phrase to test: ")
        subprocess.call('cp /home/arthur/Desktop/TrumpSounds/Hannity/Words/*.wav /tweetreader/sounds', shell=True)

        if test_string <> "xit":
            test_list = test_string.split(' ')
            soundTest(test_list)

        subprocess.call('cp /home/arthur/Desktop/TrumpSounds/Hannity/Words/*.wav /tweetreader/sounds', shell=True)


#MAIN SECTION
choice = raw_input('testLoop or getTimeline: ')
if choice == 'testLoop':
    testLoop()
else:
    getTimelineTest()


#subprocess.call('cp /home/arthur/Desktop/TrumpSounds/Hannity/Words/*.wav /tweetreader/sounds', shell=True)

#getTimeline()

#soundTest()

#testLoop()


