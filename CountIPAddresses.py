def ips_between(start, end):
    start = start.split('.')
    end = end.split('.')
    s1 = int(start[0])*(256**3) + int(start[1])*(256**2) + int(start[2])*(256) + int(start[3])
    s2 = int(end[0])*(256**3) + int(end[1])*(256**2) + int(end[2])*(256) + int(end[3])
    differ = s2-s1

    
    return differ 
