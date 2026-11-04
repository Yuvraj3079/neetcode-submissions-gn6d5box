class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapStrToCounter = defaultdict(list)

        for s in strs:
            counter = Counter(s)
            key = frozenset(counter.items())

            mapStrToCounter[key].append(s)
        
        return (list(mapStrToCounter.values()))