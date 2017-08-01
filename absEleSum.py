def abs_sum(n, ar, itr, incr):
    for x in range(itr):
    	new_list = [y+1 for y in incr.index(x)]
    	print(new_list)
    
    
a = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
it = int(input().strip())
inc = list(map(int,input().strip().split(' ')))
