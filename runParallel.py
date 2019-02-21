from multiprocessing import Pool

def printRange(lrange):
	print ("First is " + str(lrange[0]) + " and last is " + str(lrange[1]))

def generateRange(total_rows):
	listRange = [[0, 4000]]
	total = total_rows
	numofprocesses = 100
	segment = 4000
	while listRange[-1][1] < total:
		first = listRange[-1][1]
		last = first + segment
		if last >= total:
			last = total
		listRange.append([first, last])
	return listRange

def runInParallel():
	ranges = generateRange(41235)
	pool = Pool(processes=len(ranges))
	pool.map(printRange, ranges)

if __name__ == '__main__':
	runInParallel()

