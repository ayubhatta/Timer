import winsound
import time

def beep_alarm():
    for repeats in range(7):
        winsound.Beep(3000, 500)
        winsound.Beep(6000, 300)
        
        
timeduration = int(input("Enter the time in seconds: "))

hours, minutes, seconds = 0, 0, 0
        
for i in range(timeduration):
    print('\n'*100)
    
    seconds += 1
    if seconds == 60:
        minutes += 1
    if minutes == 60:
        hours += 1
        minutes = 0
        
    print(str(hours) + ':' + str(minutes) + ':' + str(seconds))
    time.sleep(1)
    
if __name__ == '__main__':
    beep_alarm()