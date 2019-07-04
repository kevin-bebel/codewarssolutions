#https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

def pick_peaks(arr):
    print(arr)
    #your code here
    _out = {"pos":[], "peaks":[]}
    for i in range(len(arr)):
        curr = arr[i]
        
        check_arr = arr[i + 1:]
        greater_count = 0
        isPeak = False
        
        for x in range(len(check_arr)):
            if(curr > check_arr[x]):
                greater_count = greater_count + 1    
                isPeak = True
            else:
                break
            
        
        if isPeak is False:
            continue
        else:
            _out["pos"].append(i)
            _out["peaks"].append(arr[i])
        
        
        '''
        if i == 0:
            _out["pos"].append(i)
            _out["peaks"].append(arr[i])
            continue
        
        if i + 1 == len(arr):
            continue
        
        if arr[i] > arr[i - 1] and arr[i] >= arr[i + 1] :
            if arr[i] == arr[len(arr) - 1] and arr[i] == arr[len(arr) - 2] :
                continue
            _out["pos"].append(i)
            _out["peaks"].append(arr[i])
        '''
    return _out    