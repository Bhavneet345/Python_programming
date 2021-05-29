import re
import requests
email = requests.get("https://www.universityofcalifornia.edu/uc-system/contact-us")
contact_details = email.text
details = re.compile(r"\w+@ucop.edu|\w+@ucapplication.net\b")
contact_detail_list = details.findall(contact_details)

with open("contact_details.txt", "a") as c:
    for detail in contact_detail_list:
        c.write(detail+"\n")

with open("contact_details.txt", "r") as c:
    l = []
    for lines in c:
        l.append(lines)

new_list = set(l)
with open("new_contact_details.txt", "w") as n:
    for lines in new_list:
        n.write(f"{lines}")

with open("new_contact_details.txt", "r") as c:
    from win32com.client import Dispatch
    speaker = Dispatch("SAPI.SpVoice")
    for lines in c:
        a = c.read()
        speaker.Speak(a)




