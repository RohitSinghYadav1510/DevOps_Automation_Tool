import socket
import cv2
import subprocess as sp

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ip="192.168.43.18" 
port=1234

s.bind((ip,port)) 
s.listen()      

csession , caddr= s.accept() 

while True:

	data=csession.recv(100).decode()
	#print(data)
	#can you run the date cmd on the localhost
	if "date" in data and "run" in data and "localhost" in data:	
		output=sp.getoutput("date")
		output=output.encode()
		csession.send(output)

	# can you run the calendar cmd on the localhost 
	elif "calendar" in data and "run" in data and "localhost" in data:
		output=sp.getoutput("cal")
		output=output.encode()
		csession.send(output)

	# can you run the cheese cmd on the localhost
	elif "cheese" in data and "run" in data and "localhost" in data:
		output=sp.getoutput("cheese")
		output=output.encode()
		csession.send(output)

	# can you capture the photo on the localhost 
	elif "photo" in data and "capture" in data and "localhost" in data:
		
		cap=cv2.VideoCapture(0)
		ret, photo=cap.read()
		cv2.imshow('Rohit', photo)
		cv2.waitKey()
		cv2.destroyAllWindows()
		cap.release()


	elif "capture" in data and "video" in data and "localhost" in data:

		sp.getoutput("python36 Videocapture.py")
		output="Video have started"
		output=output.encode()
		csession.send(output)

	#can you connect the mobile camera with system
	elif "mobile" in data and "camera" in data and "localhost" in data: 	
	
		sp.getputput("python36 mobile_connect")
		output="Mobile camera has been connected with your system"
		output=output.encode()
		cession.send(output)
	

	# can you add the user on the localhost	
	elif "user" in data and "add" in data and localhost:
		
		user_name=input("Enter the user name")
		sp.getoutput("useradd {}".format(user_name))
		sp.getoutput("su - {}".format(user_name))
		output="User add and Login successful"
		output=output.encode()
		cession.send(output)


	elif "docker" in data and "run" in data and "localhost" in data:


		D_name="Enter the docker image"
		outpur=D_image.encode()
		csession.send(output)
		
		sp.getoutput("yum install docker-ce -y")
		sp.getoutput("systemctl enable docker")
		sp.getoutput("docker load -i {}".format(D_image))
		sp.getoutput("docker run -it {}".format(OS_name))
		#output=sp.getoutput("cheese")
		output="Docker launch Successfull"
		output=output.encode()
		csession.send(output)

	elif "docker" in data and "stop" in data and "localhost" in data:

		sp.getoutput("docker stop {}".formate(OS_name))
		output="Docker stop successful"
		output=output.encode()
		csession.send(output)
		

	elif "recognise" in data and "face" in data and "localhost" in data:

		sp.getoutput("python36 Face_Recognition.py")
		output="Face being recognize"
		output=output.encode()
		csession.send(output)




	#FOR REMOTE HOST



	elif "date" in data and "run" in data and "remote" in data:	
				
		output=sp.getoutput("ssh {} date".format(IP_address))
		output=output.encode()
		csession.send(output)

	elif "calendar" in data and "run" in data and "remote" in data:
		output=sp.getoutput("ssh {} cal".format(IP_address))
		output=output.encode()
		csession.send(output)

	elif "cheese" in data and "run" in data and "remote" in data:
		output=sp.getoutput("ssh {} cheese".format(IP_address))
		output=output.encode()
		csession.send(output)

	elif "photo" in data and "capture" in data and "remote" in data:
		
		sp.getoutput("scp photocapture.py {}:/root/Desktop/".format(IP_address))
		sp.getoutput("shh {} python36 /root/Desktop/photocapture.py".format(IP_address))
		sp.getoutput("scp {}:/root/Desktop/rohit2.png  /root/Desktop/".format(IP_address))
		output="Photo Capture Successfull"
		output=output.encode()
		csession.send(output)

	elif "docker" in data and "run" in data and "Remote" in data:


		D_name="Enter the docker image"
		outpur=D_image.encode()
		csession.send(output)
		
		sp.getoutput("ssh {} yum install docker-ce -y".format(IP_address))
		sp.getoutput("ssh {} systemctl enable docker".format(IP_address))
		sp.getoutput("ssh {} docker load -i {}".format(IP_address,D_image))
		sp.getoutput("ssh {} docker run -it {}".format(IP_address,OS_name))

		#output=sp.getoutput("cheese")
		output="Docker launch Successfull"
		output=output.encode()
		csession.send(output)	

	elif "docker" in data and "stop" in data and "localhost" in data:

		sp.getoutput("ssh {} docker stop {}".formate(IP_address,OS_name))
		output="Docker stop successful"
		output=output.encode()
		csession.send(output)

	else:
		csession.send("Invalid".encode())


	
	
	"""

	data = csession.recv(100) 
	cmd =data.decode()
	#print(cmd)
	output=sp.getoutput(cmd)
	#print(output)
	output=cmd.encode()
	output=output.encode()	
	csession.send(output)
	"""
