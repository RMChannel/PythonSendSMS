import subprocess
from time import sleep

def sendSMS(number):
    subprocess.call("adb shell am start -a android.intent.action.SENDTO -d sms:+39"+number+" --es sms_body \"Benvenuti\\ da\\ Boccia\" --ez exit_on_sent false",shell=True)
    sleep(1)
    subprocess.call("adb shell input tap 966 2498", shell=True) #Qui vanno le coordinate del pulsante invia

subprocess.call("adb devices",shell=True)
sendSMS("123456789")