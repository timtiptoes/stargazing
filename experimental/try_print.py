import subprocess
lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
lpr.stdin.write("boingo and then some\n more boingo")
lpr.stdin.close()
while (1==1):
	sig=input("enter name:")
	lpr.send_signal(sig)

