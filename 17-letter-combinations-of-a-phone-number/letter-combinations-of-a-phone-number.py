class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {"2":["a","b","c"], "3":["d","e","f"], "4": ["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"],"0":[" "]}
        if len(digits) == 0:
            return []
        all_outputs = [""]
        for d in digits: #3
            new_outputs = []
            chars = mapping[d] #[d,e,f]
            for c in chars: #[d,e,f]
                for s in all_outputs: #[a,b,c]
                    new_outputs.append(s + c) #[ad, bd, cd, ...]
            all_outputs = new_outputs #[ad,bd,cd..]
        return all_outputs