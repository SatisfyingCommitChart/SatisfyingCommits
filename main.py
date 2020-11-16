import schedule
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess as cmd


def dailyCommits():
    timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    bodyText = time.strftime("Year: %Y, Month: %m, Day: %d \n Hour: %H, Minute: %M, Second: %S")
    with open(timestr+".txt", "w") as file: 
        file.write(bodyText)
        print("File: " + timestr + " created")

def commitFiles():
    timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    cp = cmd.run("git add .", check = True, shell = True)
    cp = cmd.run(f"git commit -m '{timestr}'", check=True, shell=True)
    cp = cmd.run("git push -u origin master -f", check=True, shell=True)
    
scheduler = BlockingScheduler()
scheduler.add_job(dailyCommits, 'interval', seconds = 1)
# scheduler.add_job(commitFiles, 'interval', seconds = 15)
scheduler.start()