@echo off
cd /d d:\test\WinSCP5151
winscp.exe /console /command "option batch continue" "option confirm off" "open sftp://root:Oelinux_123!@192.168.225.1:22" "option transfer binary" "get /mnt/sdcard2/Ehplog C:\Users\z1339\Desktop\Analyze\ALL" "exit"
