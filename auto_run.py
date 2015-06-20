import time
import os
for i in range(1, 33):
	if i % 3 == 0:
        	time.sleep(3600 * 24)
	print 'xxu46_', i, 'spider'
        cmd = 'nohup scrapy crawl xxu46_' + str(i) + ' > xxu46_' + str(i) +'.log 2>&1 &'
        os.system(cmd)
	time.sleep(23)



