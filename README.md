# ZoomAutoJoinAndRecordSession
 Automatic Zoom Session Join And Record With Python
 
 This is an automatic tool to join zoom sessions and record them with ffmpeg.
 
 To work you need Python 3 and pandas installed. Pandas is used to read the csv file. The csv file can be edited with  notepad++. In the csv file in starttime  put the day and start time in the following format "Mon 17:30" without the quotes of the zoom session, and in the meetingid put the zoom session link, and in endtime put the end time of the zoom session in the following format "17:30" without the quotes. You can have as many entries as you want.
 And to open the zoom links it has portable web browser falkon
 This tool also records the desktop.
 
 Thing you need:

 Notepad++ 
 https://notepad-plus-plus.org/downloads/

 To use the script

 download the zip and extract it

 Open command prompt 



 cd ZoomAutoJoinAndRecordSession\env\Scripts

 
 activate


 cd .. and cd ..


 python main.py

or run run.bat

to run the csv reader
readcsv.bat

 Thanks to Anish Malla https://www.youtube.com/watch?v=V3IOfvGmqxs
 
 Also you need to change some zoom settings shown in the images bellow:
 
 
 
 ![alt text](https://github.com/evilcomputer12/WindowsAutoJoinAndRecordZoomSession/blob/master/ZoomAudio.png?raw=true)
 
 
 
 
 ![alt text](https://github.com/evilcomputer12/WindowsAutoJoinAndRecordZoomSession/blob/master/ZoomVideo.png?raw=true)
 
 
 
 ![alt text](https://github.com/evilcomputer12/WindowsAutoJoinAndRecordZoomSession/blob/master/ZoomBrowser.png?raw=true)
 
 Also you need to change the audio source in my case is audio="Stereo Mix (Realtek High Definition Audio)"
 
 
 ffmpeger=subprocess.Popen('"bin/ffmpeg.exe" -f gdigrab -i desktop  -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast -strftime 1 ' + dt_file_name , shell=True, stdin=subprocess.PIPE)
 
 To enable Stereo Mix in Windows
 
 On the speaker icon in taskbar right click > Sounds
 
 then
	
 right click stereo mix
 ![alt text](https://github.com/evilcomputer12/WindowsAutoJoinAndRecordZoomSession/blob/master/SoundSettings.png?raw=true)
 
 ![alt text](https://github.com/evilcomputer12/WindowsAutoJoinAndRecordZoomSession/blob/master/SoundSettings1.png?raw=true)
 
 If you don't have Stereo Mix, You can download https://vb-audio.com/Cable/index.htm, extract it, go to folder VBCABLE_Driver_Pack43 depending on if you have 64bit machine run VBCABLE_Setup_x64 as administrator and install the driver.
 
 Also if you dont have Stereo Mix, you have to comment this line in the code with #
 
 #ffmpeger=subprocess.Popen('"bin/ffmpeg.exe" -f gdigrab -i desktop  -f dshow -i audio="Stereo Mix (Realtek High Definition Audio)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast -strftime 1 ' + dt_file_name , shell=True, stdin=subprocess.PIPE)
 
 and uncomment
 
 ffmpeger=subprocess.Popen('"bin/ffmpeg.exe" -f gdigrab -i desktop  -f dshow -i audio="CABLE Output (VB-Audio Virtual Cable)" -vcodec libx264 -pix_fmt yuv420p -preset ultrafast -strftime 1 ' + dt_file_name , shell=True, stdin=subprocess.PIPE) 
  
 
 
 
 Then right click > Sounds
 
 right click Cable
 
 ![alt text](https://github.com/evilcomputer12/WindowsAutoJoinAndRecordZoomSession/blob/master/SoundSettings2.png?raw=true)
 
 
 ![alt text](https://github.com/evilcomputer12/WindowsAutoJoinAndRecordZoomSession/blob/master/SoundSettings3.png?raw=true)


zoom settings

![alt text](https://github.com/evilcomputer12/WindowsAutoJoinAndRecordZoomSession/blob/master/ZoomSettings.png?raw=true)



![alt text](https://github.com/evilcomputer12/WindowsAutoJoinAndRecordZoomSession/blob/master/ZoomSettings1.png?raw=true)


 
 Before next zoom session please close the browser that's default !
 
 # This is only for education purposes. Please use it at your own risk.
 
 If anyone has improvements to add please feel free to add. My goal is to make it work in mac and linux
 Update ...
 If you dont have zoom link you can add the meeting id in the csv and password for the meeting
 Please don't use the computer while you have a meeting id and password 
 
 Update i have made a mac OS version
 https://github.com/evilcomputer12/macOSAutoJoinAndRecordZoomSession

