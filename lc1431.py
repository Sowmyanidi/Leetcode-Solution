def kidsWithCandies(candies, extraCandies):
        boolean = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max(candies):
                boolean.append(True)
            else:
                 boolean.append(False)
        return boolean
print(kidsWithCandies([2,3,5,1,3],3))