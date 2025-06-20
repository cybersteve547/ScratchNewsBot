
import scratchattach as sa
from datetime import datetime
import os

time = datetime.now()
session = sa.login(os.environ['SCRATCH_USERNAME'], os.environ['SCRATCH_PASSWORD'])
target = session.connect_user("ScratchNewsBot")
comment = target.post_comment(time.strftime("SCRATCH NEWS %m-%d-%Y Source code: https://github.com/cybersteve547/ScratchNewsBot Hello Scratchers! Below you will find info about some things happening today!"))
