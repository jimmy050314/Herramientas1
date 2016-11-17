import serial
import numpy
import matplotlib.pyplot as plt
from drawnow import *
data=[]
Port=serial.Serial('/dev/ttyUSB0',9600)
plt.ion()
cnt=0
def draw_plot():
	plt.ylim(0,500)
	plt.title('Sensor')
	plt.grid(True)
	plt.ylabel('Qué miden')
	plt.plot(data,'ro-',label='Data')
	plt.legend(loc='upper right')
while(True):
	while(Port.inWaiting==0):
		pass
	dataStr=Port.readline()
	dataf=float(dataStr)
	data.append(dataf)
	drawnow(draw_plot)
	cnt=cnt+1
	if(cnt>50):
		data.pop(0)
		cnt=cnt-1

