
import scratchattach as sa
from datetime import datetime
import time
import os

t = datetime.now()

print("logging in...")
session = sa.login(os.environ['SCRATCH_USERNAME'], os.environ['SCRATCH_PASSWORD'])
print("logged in!")

print("getting data...")
target = session.connect_user("ScratchNewsBot")
featured = sa.featured_projects[0]

print("preparing comments...")
c1 = t.strftime("SCRATCH NEWS %m-%d-%Y Source code: https://github.com/cybersteve547/ScratchNewsBot Hello Scratchers! Below you will find info about some things happening today!")
c2 = "Today's featured project is " + featured.title + " by " + featured.author_name + "!"

print(c1)
comment = target.post_comment(c1)
time.sleep(120)
print(c2)
comment.reply(c2)
