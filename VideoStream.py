class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		try:
			self.file = open(filename, 'rb')
		except:
			raise IOError
		self.frameNum = 0
		self.totalFrames = self.countTotalFrames()
		
	def nextFrame(self):
		"""Get next frame by searching for JPEG markers"""

		SOI = b'\xff\xd8'
		EOI = b'\xff\xd9'

		frame_data = b''

		data = self.file.read(2)
		if not data:
			return None

		while data != SOI:
			current_pos = self.file.tell()
			self.file.seek(current_pos - 1)
			data = self.file.read(2)
			if not data:
				return None
		
		frame_data += SOI

		last_byte = b''

		while True:
			current_byte = self.file.read(1)

			if not current_byte:
				# End of file reached without finding EOI
				return None

			frame_data += current_byte

			if last_byte == b'\xff' and current_byte == b'\xd9':
				self.frameNum += 1
				return frame_data
			
			last_byte = current_byte
	
	def countTotalFrames(self):
		SOI = b'\xff\xd8'
		EOI = b'\xff\xd9'

		count = 0
		last_byte = b''

		pos = self.file.tell()
		self.file.seek(0)

		while True:
			byte = self.file.read(1)
			if not byte:
				break
			if last_byte == b'\xff' and byte == b'\xd9':
				count += 1
			last_byte = byte

		self.file.seek(pos)
		return count

	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum
	
	