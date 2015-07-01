import os
import subprocess

t = os.popen('python D:\QQMusicCache\WhirlCache\A\S\q.py')
print  t.read()
s = subprocess.Popen('dir', shell = True, stdout= subprocess.PIPE, stderr= subprocess.PIPE)
return_code = s.wait()
print return_code
