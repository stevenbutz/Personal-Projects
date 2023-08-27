
def largestAltitude(gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        alt = 0
        lst = [0]
        for i in range(0,len(gain)-1):
            lst.append(lst[i]+gain[i])
        print(lst)
        return max(lst)
gain = [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]
print(largestAltitude(gain))
print(ord("b"))
