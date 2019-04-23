# coding=utf-8
import sys
import traceback
import Ice
import AppServer
import json


class MP3ManagerI(AppServer.MP3Manager):
    def __init__(self):
        self.trackList = []

    def add(self, track, current=None):
        self.trackList.append(track)
        return True

    def remove(self, title, current=None):
        for track in self.trackList:
            if track.title == title:
                self.trackList.remove(track)
                return True
        return False

    # def play(self, id, current=None):

    def search(self, key, value, current=None):
        for track in self.trackList:
            if getattr(track, key) == value:
                return track
        return None

    def getTrackList(self, current=None):
        if len(self.trackList) == 0:
            return "\nAucune musique n'a été enregistré dans la base de données...\n"
        str = "\nTitre - Artiste - Album - Path\n------------------------------\n"
        for track in self.trackList:
            str += track.title + " - " + track.artist + " - " + track.album + " - " + track.path + "\n"
        return str

status = 0
ic = None
try:  # Server implementation here!
    ic = Ice.initialize(sys.argv)  # Initializes the Ice run time
    # Creates an object adapter (adapter name, default port)
    adapter = ic.createObjectAdapterWithEndpoints(
        "SimpleMP3ManagerAdapter", "default -p 10000")
    object = MP3ManagerI()  # Creates a servant for our MP3Manager interface
    # Informs the object adapter of the presence of a new servant (servant, identifier)
    adapter.add(object, ic.stringToIdentity("SimpleMP3Manager"))
    adapter.activate()  # Activates the adapter
    # Suspends the calling thread until the server implementation terminates
    ic.waitForShutdown()
except:  # Catches all exceptions that may be thrown by the code
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()  # Destroys the communicator
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)
