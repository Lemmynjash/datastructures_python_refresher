def hourglassSum(arr):
    
    # hourglass' sums, empty yet
    sm = []
		
    for i in range(4):
        for j in range(4):
				
            temp = [hourglass[i:i+3] for hourglass in arr[j:j+3]]
						
            # "drop" the useless info from the hourglass array
            temp[1][0], temp[1][-1] = 0, 0
						
            # calculate the sum for the each hourglass and add it to the list
            sm.append(sum(sum(lst) for lst in temp))
						
    # return max value
    return max(sm)


def hourglassSum(arr):
    c = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]
    res = -math.inf
    for y in range(len(arr) - 2):
        for x in range(len(arr[y]) - 2):
            res = max(sum([arr[y + i[0]][x + i[1]] for i in c]), res)
    return res

def hourglassSum(arr):
    a=[]
    for i in range(1,5):
     for j in range(1,5):
        e=(arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i][j]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1])
        a.append(e)
    return max(a)  

def hourglass_sum(arr):
    results = []
    for i in range(4):
        for k in range(4):
            results.append(sum(arr[i][k:k + 3]) + arr[i + 1][k + 1] + sum(arr[i + 2][k:k + 3]))
    return max(results)