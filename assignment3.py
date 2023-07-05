q1>class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum1=0
        for i in range(0,len(nums),2):
            sum1=sum1+nums[i]
        return sum1

q2>class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        set1=set()
        n=len(candyType)
        for i in range(len(candyType)):
            set1.add(candyType[i])
        m=len(set1)
        return int(min(n/2,m))

q3>class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total=0
        for i in range(len(flowerbed)-1):
            if(flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
        return n<=0

q4>class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        product1=nums[-1]*nums[-2]*nums[-3]
        product2=nums[0]*nums[1]*nums[-1]
        return max(product1,product2)

q5>n=int(input())
ar=[]
target=int(input())
for i in range(n):
    ar.append(int(input()))
for i in range(len(ar)-1):
    if ar[i]==target:
        return i
return -1

q6>class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc=True
        dec=True
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dec=False
            if nums[i]<nums[i-1]:
                inc=False
        return inc or dec