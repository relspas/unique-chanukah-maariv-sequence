import calendar
import requests
import re


def hebcal(year):
    url = "https://www.hebcal.com/hebcal?v=1&cfg=json&maj=off&min=off&mod=off&nx=on&year="+\
    str(year)+"&month=x&ss=off&c=off&mf=off&geo=geoname&geonameid=3448439&M=on&s=off"
    r = requests.get(url)
    return r.json()

#find when first day of 2 day Rosh CHodesh CHanukah falls on a tuesday as well as the day beginning the saying of VeTen Tal Umatar
def main():
    c = calendar.Calendar()
    for year in range(1582,3000):
        # print(year)
        for monthNumber, month in enumerate(c.yeardatescalendar(year,12)[0]):
            monthNumber += 1 #move to 1 indexed
            for week in month:
                for dayofWeek, day in enumerate(week):
                    if day.month != monthNumber: #skipping days that belong to wrong month imbedded in calendar because complete week is always stored.
                        continue
                    if dayofWeek != 1: #Tuesday
                        continue
                    if day.month != 12:
                        continue

                    VTUday = None #Veten tal umatar
                    if year >= 1582 and year < 1700:
                        if calendar.isleap(year+1) and day.day == 3:
                            VTUday = 3
                        elif not calendar.isleap(year+1) and day.day == 2:
                            VTUday = 2
                        else:
                            continue
                    elif year >= 1700 and year < 1800:
                        if calendar.isleap(year+1) and day.day == 4:
                            VTUday = 4
                        elif not calendar.isleap(year+1) and day.day == 3:
                            VTUday = 3
                        else:
                            continue
                    elif year >= 1800 and year < 1900:
                        if calendar.isleap(year+1) and day.day == 5:
                            VTUday = 5
                        elif not calendar.isleap(year+1) and day.day == 4:
                            VTUday = 4
                        else:
                            continue
                    elif year >= 1900 and year < 2100:
                        if calendar.isleap(year+1) and day.day == 6:
                            VTUday = 6
                        elif not calendar.isleap(year+1) and day.day == 5:
                            VTUday = 5
                        else:
                            continue
                    elif year >= 2100 and year < 2200:
                        if calendar.isleap(year+1) and day.day == 7:
                            VTUday = 7
                        elif not calendar.isleap(year+1) and day.day == 6:
                            VTUday = 6
                        else:
                            continue
                    elif year >= 2200 and year < 2300:
                        if calendar.isleap(year+1) and day.day == 8:
                            VTUday = 8
                        elif not calendar.isleap(year+1) and day.day == 7:
                            VTUday = 7
                        else:
                            continue
                    elif year >= 2300 and year < 2500:
                        if calendar.isleap(year+1) and day.day == 9:
                            VTUday = 9
                        elif not calendar.isleap(year+1) and day.day == 8:
                            VTUday = 8
                        else:
                            continue
                    elif year >= 2500 and year < 2600:
                        if calendar.isleap(year+1) and day.day == 10:
                            VTUday = 10
                        elif not calendar.isleap(year+1) and day.day == 9:
                            VTUday = 9
                        else:
                            continue
                    elif year >= 2600 and year < 2700:
                        if calendar.isleap(year+1) and day.day == 11:
                            VTUday = 11
                        elif not calendar.isleap(year+1) and day.day == 10:
                            VTUday = 10
                        else:
                            continue
                    elif year >= 2700 and year < 2900:
                        if calendar.isleap(year+1) and day.day == 12:
                            VTUday = 12
                        elif not calendar.isleap(year+1) and day.day == 11:
                            VTUday = 11
                        else:
                            continue
                    elif year >= 2900 and year < 3000:
                        if calendar.isleap(year+1) and day.day == 13:
                            VTUday = 13
                        elif not calendar.isleap(year+1) and day.day == 12:
                            VTUday = 12
                        else:
                            continue
                    else:
                        continue

                    # print(VTUday, year)

                    #rosh chodesh
                    j = hebcal(year)
                    cnt = 0
                    date_ = None
                    for item in j["items"]:
                        if item["title"] == "Rosh Chodesh Tevet":
                            cnt += 1
                            if not date_:
                                date_ = item["date"]
                    if cnt != 2: #must be 2 days of Rosh Chodesh
                        continue
                    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_)
                    rhy = match[1] #year
                    rhm = match[2] #month
                    rhd = match[3] #day
                    print("RH",date_)
                    if rhy != year: #possible if RH tevet is so late it is in january
                        continue
                    if rhm != 12:
                        continue
                    if VTUday != rhd:
                        continue
                    
                    print("FOUND ->",day)

main()