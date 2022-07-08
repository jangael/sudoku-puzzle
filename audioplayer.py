# audioplayer.py
# very basic audio file player without external modules
# for Windows and Mac in Python.  Only plays wav files
# on Windows, seems to work with wav, mp3 and other formats on Macs.

# Provides two functions:
# startSound(filename, asyncPlay=True, loop=True)
# stopSound()
# original source: http://www.kosbie.net/cmu/spring-15/15-112/notes/simpleAudio.py
# modified to support multiple async audio playback for windows
# need to install simpleaudio library (http://simpleaudio.readthedocs.io/en/latest/)
# python -m pip install simpleaudio
# by James Lee (slee10@conncoll.edu)

import sys, platform, subprocess, time, threading

def checkForOS(*terms):
    platformString = (sys.platform + platform.platform()).lower()
    for term in terms:
        if (term in platformString): return True
    return False

osIsWindows = checkForOS("win32", "win64", "windows")
osIsLinux = checkForOS("linux")

if (osIsWindows == True):
    import simpleaudio as sa
    import wave
    from multiprocessing import Process
    soundProcesses = [ ]

    def startSound(filename, asyncPlay=True, loop=True):
        if (asyncPlay == True): startAsyncSound(filename, loop)
        else: startSyncSound(filename, loop)
    def startSyncSound(filename, loop, thread=None):
        wave_read = wave.open(filename, 'rb')
        wave_obj = sa.WaveObject.from_wave_read(wave_read)
        while True:
            play_obj = wave_obj.play()
            play_obj.wait_done()
            if (loop == False): break
    def startAsyncSound(filename, loop):
        p = Process(target=startSyncSound, args=(filename,loop,))
        p.start()
        soundProcesses.append(p)
    def stopSound():
        sa.stop_all()
        while (soundProcesses != [ ]):
            try: soundProcesses.pop().terminate()
            except: pass

else:
    # For now, just do Mac OS (sorry, Linux...)
    soundProcesses = [ ]
    soundThreads = [ ]
    soundThreadCounter = 0
    def startSound(filename, asyncPlay=True, loop=True):
        if (asyncPlay == True): startAsyncSound(filename, loop)
        else: startSyncSound(filename, loop)
    def startSyncSound(filename, loop, thread=None):
        while True:
            app = "aplay" if osIsLinux else "afplay"
            p = subprocess.Popen([app, filename])
            soundProcesses.append(p)
            p.wait()
            if (p in soundProcesses): soundProcesses.remove(p)
            if (loop == False): break
            if ((thread != None) and (thread not in soundThreads)): break
    def startAsyncSound(filename, loop):
        global soundThreadCounter
        tc = soundThreadCounter
        soundThreadCounter += 1
        soundThreads.append(tc)
        thread = threading.Thread(target=startSyncSound,
                                  args=(filename,loop,tc))
        thread.daemon = True
        thread.start()
    def stopSound():
        global soundThreads
        soundThreads = [ ]
        while (soundProcesses != [ ]):
            try: soundProcesses.pop().terminate()
            except: pass

#####################################
# Simple test
#####################################

def testSoundPlaying():
     print ("starting sound!...")
     startSound("bgm.wav", asyncPlay=True, loop=True)
     print ("done!")

     startSound("swfaith.wav", True, False)
     
     print ("sleeping for 4 seconds...")
     time.sleep(4)
     print ("done!")

     print ("stopping sound...")
     stopSound()
     print ("done!")


if __name__ == "__main__":
     testSoundPlaying()

