import subprocess
import time
import pandas as pd
from datetime import datetime
#import webbrowser
import keyboard
from pyautogui import press, typewrite, hotkey

# Reading the file
df = pd.read_csv('Lectures.csv')
print("Program Started !")
print(datetime.now().strftime("%d-%m-%Y-%H-%M"))

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%a %H:%M")
    now1 = datetime.now().strftime("%a %H:%M")
    if now in str(df['starttime']):
       row = df.loc[df['starttime'] == now]
       link = str(row.iloc[0,1])
       pwd = str(row.iloc[0,3])
       if link.startswith('http'):
        if pd.isnull(df.loc[0, 'pass']):
          now = datetime.now()
          dt_file_name = now.strftime('"ZoomRecording-%Y-%m-%d_%H-%M-%S.mkv"')
          ffmpeger=subprocess.Popen('"bin/ffmpeg.exe" -f gdigrab -i desktop  -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast -strftime 1 ' + dt_file_name , shell=True, stdin=subprocess.PIPE)
          chrome=subprocess.Popen('"bin/browser/App/Falkon/falkon.exe" ' + link ,shell = True, stdout=subprocess.PIPE)
          print("1")
          time.sleep(10)
          subprocess.call("TASKKILL /f  /IM  FALKON.EXE")       
          time.sleep(60)
        else:
          now = datetime.now()
          dt_file_name = now.strftime('"ZoomRecording-%Y-%m-%d_%H-%M-%S.mkv"')
          ffmpeger=subprocess.Popen('"bin/ffmpeg.exe" -f gdigrab -i desktop  -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast -strftime 1 ' + dt_file_name , shell=True, stdin=subprocess.PIPE)
          chrome=subprocess.Popen('"bin/browser/App/Falkon/falkon.exe" ' + link ,shell = True, stdout=subprocess.PIPE)
          print("2")
          time.sleep(15)
          typewrite(pwd, interval=0.4)
          time.sleep(10)
          keyboard.press('enter')
          time.sleep(15)  
          subprocess.call("TASKKILL /f  /IM  FALKON.EXE")    
          time.sleep(60)

       else:
       	now = datetime.now()
       	dt_file_name = now.strftime('"ZoomRecording-%Y-%m-%d_%H-%M-%S.mkv"')
       	ffmpeger=subprocess.Popen('"bin/ffmpeg.exe" -f gdigrab -i desktop  -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast -strftime 1 ' + dt_file_name , shell=True, stdin=subprocess.PIPE)
       	#ffmpeger=subprocess.Popen('"bin/ffmpeg.exe" -f gdigrab -i desktop  -f dshow -i audio="CABLE Output (VB-Audio Virtual Cable)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast -strftime 1 ' + dt_file_name , shell=True, stdin=subprocess.PIPE) 
       	link1 = "https://zoom.us/join"
        print("3")
        chrome=subprocess.Popen('"bin/browser/App/Falkon/falkon.exe" ' + link1 ,shell = True, stdout=subprocess.PIPE)
       	time.sleep(15)
       	typewrite(link, interval=0.4)
       	time.sleep(10)
       	press('enter')
        time.sleep(10)
       	typewrite(pwd, interval=0.4)
       	time.sleep(10)
       	press('enter')
       	time.sleep(15)
        subprocess.call("TASKKILL /f  /IM  FALKON.EXE")
       	time.sleep(60)
       	
    if now1 in str(df['endtime']):
        ffmpeger.stdin.write('q'.encode("GBK"))
        ffmpeger.stdin.write('q'.encode("GBK"))
        ffmpeger.stdin.write('q'.encode("GBK"))
        ffmpeger.communicate()
        ffmpeger.communicate()
        ffmpeger.communicate()
        keyboard.press_and_release('ctrl+q')
        time.sleep(60)     

        
