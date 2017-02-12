import subprocess

def updateSounds():
    subprocess.call('rm allsounds', shell=True)

    subprocess.call('ls *.wav >> allsounds', shell=True)

    subprocess.call('vi allsounds', shell=True)

updateSounds()
