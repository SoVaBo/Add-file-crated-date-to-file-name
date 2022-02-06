from pathlib import Path
from datetime import datetime

root = Path('files')
fpaths = root.glob("**/*") 

for path in fpaths:
  if path.is_file():
    stats = path.stat()
    seconds = stats.st_ctime
    dcr = datetime.fromtimestamp(seconds)
    sdcr = dcr.strftime("%Y-%m-%d_%H:%M:%S")
    newfname = sdcr + path.name
    newfpath = path.with_name(newfname)
    path.rename(newfpath)