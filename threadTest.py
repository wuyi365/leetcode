import threading, time, datetime


def foo(atest, edf):
	print 'calling foo....'
	print atest
	print edf
	time.sleep(5)

def b():
    a =  datetime.datetime.now()
    print 'started at:   ', a
    thr = threading.Thread(target=foo, args=('abc','zzzzzzzzzzzzz'), kwargs={})
    thr.start() # will run "foo"
    thr.is_alive() # will return whether foo is running currently
    #thr.join() # will wait till "foo" is done
    print 'completed'
    b = datetime.datetime.now()
    print 'Ened at:   ', b
    print b - a
    return 0
aa =  datetime.datetime.now()
print 'Ouside started at:   ', aa
b()
bb = datetime.datetime.now()
print 'Ouside Ened at:   ', bb
print bb - aa


