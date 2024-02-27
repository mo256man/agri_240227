import psutil
import datetime
import gc

class Memory():
	def __init__(self):
		self.filename = "memory.csv"
		self.process = psutil.Process()
		memory_info = self.process.memory_info()
		self.last_rss = memory_info.rss									# Resident Set Siteの初期値
		self.last_vms = memory_info.vms									# Virtual Memory Sizeの初期値
		self.memory = psutil.virtual_memory()
		self.last_used_memory = self.memory.used
		self.is_available = True

	def show(self, text):
		if self.is_available:
			"""
			memory_info = self.process.memory_info()
			rss = memory_info.rss
			rss_diff = rss - self.last_rss
			self.last_rss = rss
			vms = memory_info.vms
			vms_diff = rss - self.last_vms
			self.last_vms = vms
			str_date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
			msg = f"{str_date},{text},{rss},{rss_diff},{vms},{vms_diff}\n"
			"""
			used_memory = self.memory.used
			used_diff = used_memory - self.last_used_memory
			self.last_used_memory = used_memory
			str_date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
			msg = f"{str_date},{text},{used_memory},{used_diff}\n"
			with open(self.filename, "a", encoding="utf-8") as f:
				f.write(msg)
			gc.collect()
