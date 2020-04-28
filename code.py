import xml.etree.ElementTree as ET
from datetime import datetime
import re

tree = ET.parse("Eng_College_teachers.xml")
root = tree.getroot()

# all items data
#print("\nAll item data:")
for teacher in root:
    teacher_dict = teacher.attrib
    with open(teacher_dict["name"] + ".ics", "w+") as f:
        f.writelines("BEGIN:VCALENDAR\n")

        for day in teacher:
            day_dict = day.attrib

            for hour in day:
                hour_dict = hour.attrib
                f.writelines("BEGIN:VEVENT\n")
                time = re.split("; |, | \-|\-", hour_dict["name"])
                f.writelines(
                    "DTSTART;TZID=Asia/Kolkata:"
                    + datetime.today().strftime("%Y%m%d")
                    + "T"
                    + time[0].replace(":", "")
                    + "00\n"
                )
                f.writelines(
                    "DTEND;TZID=Asia/Kolkata:"
                    + datetime.today().strftime("%Y%m%d")
                    + "T"
                    + time[1].replace(":", "")
                    + "00\n"
                )
                f.write("RRULE:FREQ=WEEKLY;BYDAY=" + day_dict["name"][:2] + "\n")

                info_about_subject = list(hour)
                #print(len(info_about_subject))
                if len(info_about_subject) > 0:
                    f.write(
                        "LOCATION:"
                        + info_about_subject[len(info_about_subject) - 1].attrib["name"]
                        + "\n"
                    )
                    f.write("SUMMARY:")
                    for counter in range(len(info_about_subject) - 1):

                        f.write(info_about_subject[counter].attrib["name"] + " ")
                    f.write("\n")
                else:
                    f.write("LOCATION:\n")
                    f.write("SUMMARY:No Lecture\n")
                f.writelines("END:VEVENT\n")

        f.writelines("END:VCALENDAR\n")

