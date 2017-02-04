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
    print str(wav_list)

    for wav_file in wav_list:
        #creating sound object
        sound = pygame.mixer.Sound(os.path.join('sounds/', wav_file))

        # creating sound file string to test if it exists
        sound_file = os.path.join('sounds/', wav_file)
        # checking if sound file exists for each word
        try:
            contextlib.closing(wave.open(sound_file, 'r'))
        except:
            print 'No such file exists.'
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


def playNewSound(word_list = []):
    pygame.mixer.init()
    wav_list = word_list 
    #print str(wav_list)
    wav_list = stripPunctuation(wav_list)
    wav_list = [word + '.wav' for word in wav_list]
    wav_list = [word.lower() for word in wav_list]
    print str(wav_list)

    for wav_file in wav_list:
        #creating sound object
        sound = pygame.mixer.Sound(os.path.join('sounds/new', wav_file))

        # creating sound file string to test if it exists
        sound_file = os.path.join('sounds/new', wav_file)
        # checking if sound file exists for each word
        try:
            contextlib.closing(wave.open(sound_file, 'r'))
        except:
            print 'No such file exists.'
            continue

        # playing each sound sequentially
        if pygame.mixer.Channel(0).get_busy() == False:
            sound.play()
        while pygame.mixer.Channel(0).get_busy() == True:
            continue


def soundTest():
    test_sounds = 'do'.split(' ')
    playNewSound(test_sounds)

    #test_sounds = 'well its been a lot we have accomplished thank you its you we thank'.split(' ')
    #playSound(test_sounds)


subprocess.call('cp /home/arthur/Desktop/TrumpSounds/Hannity/Words/*.wav /tweetreader/sounds/new', shell=True)

#getTimeline()

soundTest()
