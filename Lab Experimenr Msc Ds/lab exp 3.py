# Exp = 3;Implement any two methods to find the outliers from a given set of data
l=[3, 42, 39, 40, 44, 48, 45, 43, 46, 100, 41, 40, 42, 46]
mean = sum(l) / len(l)
deviation = [abs(x - mean) for x in l]
md = sum(deviation) / len(l)
outliers = []
for x in l:
    if abs(x - mean) > 2 * md:
        outliers.append(x)
print("Mean:", mean)
print("Mean Deviation:", md)
print("Outliers:", outliers)