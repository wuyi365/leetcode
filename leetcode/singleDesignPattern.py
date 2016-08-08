def singleton(cls):
	instances = {}
	def _singleton(*args, **kw):
		print "------" +   str(instances) + "----------"
		if cls not in instances:
			instances[cls] = cls(*args,**kw)
		return instances[cls]
	return _singleton


@singleton
class Myclass(object):
	a = 1
	def __ini__(self, x = 0):
		self.x = x
		print 'calling....__init__'