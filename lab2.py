#Matt Layman CSC113 lab2.py
class MyTime:

	def __init__(self, hrs=0, mins=0, secs=0):
		totalsecs = hrs*3600 + mins*60 + secs
		self.hours = totalsecs // 3600
		leftoversecs = totalsecs % 3600
		self.minutes = leftoversecs // 60
		self.seconds = leftoversecs % 60

	def __str__(self):
		return "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

	def __add__(self, other):
		return MyTime(0, 0, self.to_seconds() + other.to_seconds())

	def __lt__(self, other):
		return self.to_seconds() < other.to_seconds()

	def __le__(self, other):
		return self.to_seconds() <= other.to_seconds()

	def __gt__(self, other):
		return self.to_seconds() > other.to_seconds()

	def __ge__(self, other):
		return self.to_seconds() >= other.to_seconds()

	def increment(self, seconds):
		#increment time obj by seconds
		try:
			time = MyTime(0, 0, self.to_seconds() + seconds)
			self.hours = time.hours
			self.minutes = time.minutes
			self.seconds = time.seconds
		except:
			raise TypeError("Please enter an integer in seconds")

	def to_seconds(self):
		#convert time to seconds
		return self.hours*3600 + self.minutes*60 + self.seconds

	def between(self, t1, t2):
		#check time between t1 and t2n
		return t1.to_seconds() <= self.to_seconds() and self.to_seconds() < t2.to_seconds()

def add_time(t1, t2):
	secs = t1.to_seconds() + t2.to_seconds()
	return MyTime(0, 0, secs)

if __name__ == "__main__":
	current_time = MyTime(9, 14, 30)
	bread_time = MyTime(3, 35, 0)
	done_time = add_time(current_time, bread_time)
	current_time.increment(500)
	t1 = current_time + bread_time
	print(done_time, current_time, current_time > bread_time, t1)
	print(t1 < current_time)
	print(t1.between(current_time, bread_time), t1 > bread_time)
	print(current_time)
	current_time.increment(-500)
	print(current_time)
	current_time.increment(800)
	print(current_time)
