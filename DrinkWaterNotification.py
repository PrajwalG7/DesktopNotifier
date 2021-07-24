import time
from plyer import notification

if __name__=='__main__':
   title="DRINK WATER NOW!!!"

   message="An adequate daily fluid intake is:  " \
           " About 15.5 cups (3.7 liters) of fluids a day for men." \
           " About 11.5 cups (2.7 liters) of fluids a day for women."

   IconURL="C:\\Users\Aryan\PycharmProjects\pythonProject\FirstDirect\PythonProjects\DesktopAutomation\Icons8-Ios7-Industry-Water.ico"

   # on loop run
   while True:
       notification.notify(
       title=title,
       message=message,
       app_icon=IconURL,
       timeout=5
       )
       time.sleep(60*60)

      
