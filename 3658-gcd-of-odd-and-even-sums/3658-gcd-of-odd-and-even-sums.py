class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd_numbers = 0
        even_numbers = 0
        for i in range(1,(n*2)+1):
            if i%2 == 0:
                print(i)
                even_numbers+=i
            elif i%2 != 0:
                odd_numbers+=i
        while even_numbers != 0:
            odd_numbers,even_numbers = even_numbers,odd_numbers%even_numbers
        return odd_numbers


        