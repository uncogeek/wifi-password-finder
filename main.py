import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
print("--------------------------------")
print("WiFi password finder")
print("Author: UncoGeek.ir | 2022")
print("--------------------------------")
print("")
print(" Wifi Name:                   | Password:      ")
print("")
counter = 0
for i in profiles:
    counter += 1
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
print("")
print("Total found: ", counter)
input("")