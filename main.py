# Simple Backup Script

# Import needed Modules
import shutil                               # This Module will be used for copying data
import os                                   # We'll use "os.chdir". Its used to change dir. Just like "cd"
from datetime import date                   # This is to specify date in backup filename
from distutils.dir_util import copy_tree    # This will be used to create directory
import smtplib
from email.message import EmailMessage


# Hold the current date
today = date.today()
date_format = today.strftime("%d_%b_%Y_")

#3 Location of the dirs and files
src_dir = "/root/test_src"
src_file = "src_file"
dst_dir = "/root/test_dst"
dst_file = ""

# The process of copy
try:
    # Test if Dst DIR exists
    if dst_dir == "":
        log_file = open("/root/test_dst/log_file", "w")
        log_file.write(date_format + " >>> You didn't mention the dst dir!\Check above block #3")
        log_file.close()

    # If Src File not specified, copy entire Src DIR > Dst DIR
    if src_file == "":
        copy_tree(src_dir, dst_dir)
        log_file = open("/root/test_dst/log_file", "w")
        log_file.write(date_format + " >>> Src File not specified! copied entire Src DIR > Dst DIR")
        log_file.close()

    # If Src File specified, Src file > Dst DIR
    if dst_file == "":
        dst_file = src_file
        log_file = open("/root/test_dst/log_file", "w")
        log_file.write(date_format + " >>> Src File not specified! copied entire Src DIR > Dst DIR")
        log_file.close()

    shutil.copy2(os.path.join(src_dir, src_file), os.path.join(dst_dir, dst_file + "_" + date_format))

except FileNotFoundError:
    log_file = open("/root/test_dst/log_file", "w")
    log_file.write(date_format + " >>> Couldn't find file!\Enter complete path")
    log_file.close()

with open("/root/test_dst/log_file") as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

msg["Subject"] = "Daily log file " + date_format
msg['From'] = test@test.test
msg['To'] = test@test.test
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
