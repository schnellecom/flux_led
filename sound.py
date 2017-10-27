import pyaudio  
import numpy as np  
import flux_led
   
print("checking for errors")   
table = flux_led.WifiLedBulb("192.168.1.101")
ceiling1 = flux_led.WifiLedBulb("192.168.1.109")
ceiling2 = flux_led.WifiLedBulb("192.168.1.105")
projector = flux_led.WifiLedBulb("192.168.1.103")
#table.setPresetPattern(0x25, 50)
print("no errors connected to every device")

#red = 255, 0, 0

#start every light 
ceiling1.turnOn()
ceiling2.turnOn()
projector.turnOn()
print("lights are on")

ceiling1.setRgb(166,0,166)
ceiling2.setRgb(0,153,0)
projector.setRgb(44,153,142)
print("set to default")

CHUNK = 2**11  
RATE = 44100  
scene = 1
   
p = pyaudio.PyAudio()  
stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True,  
         frames_per_buffer=CHUNK)  
print("stream is active")
		 
while stream.is_active:
   data = np.fromstring(stream.read(CHUNK), dtype=np.int16)  
   peak = np.average(np.abs(data)) // 10
   bars = "#" * int(peak // 30) #/ 2**11)

   if peak > 1800:
		if scene == 1:
			#scene 1
			ceiling1.setRgb(166,0,166)
			ceiling2.setRgb(0,153,0)
			projector.setRgb(44,153,142)
			scene = scene + 1
		elif scene == 2:
			#scene 2
			#ceiling1.setPresetPattern(0x37, 100)
			#ceiling2.setPresetPattern(0x37, 100)
			#projector.setPresetPattern(0x37, 100)
			scene = scene + 1
		elif scene == 3:
			#scene 3
			ceiling1.setRgb(0,0,255)
			ceiling2.setRgb(255,0,0)
			projector.setRgb(0,0,0)
			scene = scene + 1
		elif scene == 4:
			#scene 4
			ceiling1.setRgb(0,255,255)
			ceiling2.setRgb(255,0,255)
			projector.setRgb(30,30,255)
			scene = scene + 1
		elif scene == 5:
			#scene 5
			ceiling1.setRgb(255,255,255)
			ceiling2.setRgb(255,255,255)
			projector.setRgb(255,255,255)
			scene = scene + 1
		elif scene == 6:
			#scene 6
			ceiling1.setRgb(255,0,0)
			ceiling2.setRgb(153,0,153)
			projector.setRgb(255,130,0)	
			scene = scene + 1
		elif scene == 7:
			#scene 7
			ceiling1.setPresetPattern(0x38, 100)
			ceiling2.setPresetPattern(0x38, 100)
			projector.setPresetPattern(0x38, 100)
			scene = scene + 1
		else:
			#scene default
			ceiling1.setRgb(166,0,166)
			ceiling2.setRgb(0,153,0)
			projector.setRgb(44,153,142)
			scene = 1
			
   print("%04d %02d %s" % (peak, scene, bars))
		#print 'more'
#   elif peak > 5:  
#	print 'middle'
#	table.setRgb(0, 255, 0)
   #else:
	#print 'less'
#	table.setRgb(0, 0, 255)  

#for i in range(int(1000 * 44100 / 1024)): # go for a few seconds  
#   data = np.fromstring(stream.read(CHUNK), dtype=np.int16)  
#   peak = np.average(np.abs(data)) * 2  
#   bars = "#" * int(100 * peak / 2**16)
   #star = "*" * int(50 * peak / 2 **16)
#   print("%04d %05d %s" % (i, peak, bars))  
   
stream.stop_stream()  
stream.close()  
p.terminate()  