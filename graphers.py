import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set_style("darkgrid")
sns.set_palette("RdBu_r")
sns.set_context("paper")

def Saver(filename):
    path = "./out/" + filename + ".png"
    plt.savefig(path, bbox_inches="tight")
    
def date_frequency(whatsapp_frame, gcname):
    print("Running date frequency")
    try:
        plt.clf()
        whatsapp_frame_datetime = whatsapp_frame
        sns.histplot(x=whatsapp_frame_datetime.index, kde=True)
        plt.title("Date distribution of messages sent in " + gcname)
        plt.xticks(rotation=45)
        plt.xlabel("Date")
        plt.ylabel("Frequency")
        Saver("fig1")
    except:
        print("WARNING: Date frequency function failed. Check CHANGEME.ini")


def message_distribution(whatsapp_frame, gcname):
    print("Running message distribution")
    try:
        plt.clf()
        sns.countplot(x="name", data=whatsapp_frame)
        plt.title("Message distribution of each person in " + gcname)
        plt.ylabel("Messages sent")
        plt.xlabel("Person")
        Saver("fig2")
    except:
        print("WARNING: Message distribution function failed. Check CHANGEME.ini")

def word_search(whatsapp_frame, wordsearch, gcname):
    print("Running word search")
    try:
        plt.clf()
        pattern = ""
        if len(wordsearch) <= 1:
            pattern = wordsearch[0] + "|"
        else:
            for word in wordsearch:
                pattern += word + "|"
        
        pattern = pattern[:-1]

        whatsapp_frame_hasword = whatsapp_frame
        whatsapp_frame_hasword["hasword"] = whatsapp_frame["message"].str.contains(pattern, regex=True)
        whatsapp_frame_hasword = whatsapp_frame_hasword[whatsapp_frame_hasword["hasword"] == True]

        sns.countplot(x="name", data=whatsapp_frame_hasword)
        plt.title("Amount of messages containing '" + ', '.join(wordsearch) + "' in " + gcname + " by person")
        plt.ylabel("Message count")
        plt.yticks()
        plt.xlabel("Person")
        Saver("fig3")
    except:
        print("WARNING: Word search function failed. Check CHANGEME.ini. Word(s) might be never used.")

def time_distribution(whatsapp_frame, gcname):
    print("Running time_distribution")
    try:
        plt.clf()
        whatsapp_frame_time = whatsapp_frame
        whatsapp_frame_time["date"] = whatsapp_frame_time.index
        whatsapp_frame_time["hour"] = whatsapp_frame_time["date"].dt.hour

        sns.countplot(x="hour", data=whatsapp_frame_time)
        plt.title("Time distribution of messages sent in " + gcname)
        plt.xlabel("Hour of day")
        plt.xticks(range(24), range(24))
        plt.ylabel("Amount of messages sent")
        Saver("fig4")
    except:
        print("WARNING: Time distribution function failed. Check CHANGEME.ini")

def media_search(whatsapp_frame, gcname):
    print("Running media search")
    try:
        plt.clf()
        whatsapp_frame_memes = whatsapp_frame
        whatsapp_frame_memes["hasmedia"] = whatsapp_frame["message"].str.contains("<Media omitted>", regex=False)
        whatsapp_frame_hasmedia = whatsapp_frame_memes[whatsapp_frame_memes["hasmedia"] == True]
        
        sns.countplot(x="name", data=whatsapp_frame_hasmedia)
        plt.title("Amount of media files sent by person in " + gcname)
        plt.ylabel("Media message count")
        plt.xlabel("Person")

        Saver("fig5")

    except:
        print("WARNING: Media search function failed. Check CHANGEME.ini")