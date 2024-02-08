def mean(x):
    return sum(x)/len(x)

def median(x):
    x.sort()
    n = len(x)
    if n % 2 == 0:
        return (x[n//2-1]+x[n//2])/2
    else:
        return x[n//2]
    
def mode(x):
    counts = {}
    for i in x:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    max_count = max(counts.values())
    mode = [i for i in counts if counts[i] == max_count]
    return mode

def main():
    x = [1,2,3,4,5,6,7,8,9,10]
    print(mean(x))
    print(median(x))
    print(mode(x))

if __name__ == "__main__":
    main()
    