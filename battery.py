from plyer import notification,battery
from time import sleep

def notify(percentage):

    notification.notify(

        title = "Battery Alert",
        message = "Your Battery Percentage Is " + str(percentage) + " % . PLease Connect To Charging ASAP",
        app_name = "BATTERY NOTIFIER",
        app_icon = "battery.ico",
        timeout = 15

    )

while True:

    battery_status_dict = battery.get_state()

    if not battery_status_dict["isCharging"]:

        print("Not Charging")
        
        battery_percentage = battery_status_dict["percentage"]
        print(battery_percentage)
        if battery_percentage == 2:
            notify(battery_percentage)
            
        elif battery_percentage == 5:
            notify(battery_percentage)

        elif battery_percentage == 10:
            notify(battery_percentage)

        elif battery_percentage == 15:
            notify(battery_percentage)

        elif battery_percentage == 20:
            notify(battery_percentage)

        elif battery_percentage == 30:
            notify(battery_percentage)

        elif battery_percentage == 35:
            notify(battery_percentage)

        elif battery_percentage == 40:
            notify(battery_percentage)

        elif battery_percentage == 50:
            notify(battery_percentage)

    sleep(60)