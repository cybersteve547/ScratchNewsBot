
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
featured = session.connect_project(sa.featured_projects()[0]['id'])
print(featured)
print("preparing comments...")
c1 = t.strftime("SCRATCH NEWS %m-%d-%Y Hello Scratchers! Below you will find info about some things happening today!")
c2 = "Today's featured project is " + featured.title + " by " + featured.author_name + "! You can play it at " + featured.url
c3 = "Want to know how it works? download the source code at https://github.com/cybersteve547/ScratchNewsBot"

print(c1)
comment = target.post_comment(c1)
time.sleep(120)
print(c2)
comment.reply(c2)
time.sleep(120)
print(c3)
comment.reply(c3)
