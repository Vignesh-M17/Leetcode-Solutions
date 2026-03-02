class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        res = []
        keys = []
        value = []
        result= ""
        x =  [keys.append(chr(i)) for i in range(ord('a'),ord('z')+1)]
        y = [value.append(x) for char in key for x in char if x != " "]
        for i,char in enumerate(value):
            if char not in res:
                res.append(char)
        my_dict = dict(zip(res,keys))
        for i,schar in enumerate(message):
            if schar == " ":
                result+=" "
            else:
                result+=my_dict[schar]
        return result