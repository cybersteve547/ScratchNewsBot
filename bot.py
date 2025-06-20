
import scratchattach as sa
from datetime import datetime
import os

time = datetime.now()
session = sa.login(os.environ['SCRATCH_USERNAME'], os.environ['SCRATCH_PASSWORD'])
target = session.connect_user("ScratchNewsBot")
target.post_comment(time.strftime("%Y-%m-%d %H:%M:%S"))
