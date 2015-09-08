import time
import imaplib
import RPi.GPIO as GPIO

chan_list = (18, 25, 12, 16, 23, 21)

print('press ctl-c to stop')
try:
    while True:
        M = imaplib.IMAP4_SSL('imap.gmail.com')
        M.login('drewatkinson5@gmail.com', 'cgvnhthdytvgttjm')
        M.select()
        unread_count = len(M.search(None, 'UnSeen')[1][0].split())
        M.logout()

        print(str(unread_count) + ' unread in your inbox')

        output_values = []
        while unread_count > 0:
            output_values.append(unread_count % 2)
            unread_count = unread_count // 2

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(chan_list, GPIO.OUT)

        if len(output_values) > len(chan_list):
            output_values = []
            for i in range(len(chan_list)):
                output_values.append(1)
                
        elif len(output_values) < len(chan_list):
            while len(output_values) < len(chan_list):
                output_values.append(0)

        GPIO.output(chan_list, output_values)
        
        print('sleeping for 1 minute')
        time.sleep(60)

except KeyboardInterrupt:
    GPIO.cleanup()
