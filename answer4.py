def findTime(arr, cooldown):
    seq = []
    record = {}
    time = 0
    for t in arr:
        if t not in record:
            seq.append(t)
            record[t] = time + cooldown
        else:
            if record[t] == time:
                seq.append(t)
            else:
                delta = record[t] - time
                for i in range(delta+1):
                    seq.append("_")
                    time = time + 1
                seq.append(t)
                record[t] = time + cooldown
        time += 1
    print ("Total time: ", time)
    print ("Sequence: " + " ".join(str(item) for item in seq))
findTime([1,1,2,1], 2)
