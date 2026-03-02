class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict(zip(heights,names))
        d_sort = sorted(d.items(),reverse=True)
        keys = [item[0] for item in d_sort]
        values = [item[1] for item in d_sort]
        return values
        