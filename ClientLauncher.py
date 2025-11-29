import sys
from tkinter import Tk
from Client import Client

if __name__ == "__main__":
	try:
		# python command-line arguments
		serverAddr = sys.argv[1]
		serverPort = sys.argv[2]
		rtpPort = sys.argv[3]
		fileName = sys.argv[4]	
	except:
		print("[Usage: ClientLauncher.py Server_name Server_port RTP_port Video_file]\n")	
	
	# create a base window UI with tkinter
	# which will be modify (in sizes, add buttons,...) when creating a new Client
	root = Tk()
	
	# Create a new client (Client object from Client.py)
	app = Client(root, serverAddr, serverPort, rtpPort, fileName)
	app.master.title("RTPClient")	
	root.mainloop()
	