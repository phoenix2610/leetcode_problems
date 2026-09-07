class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_table = {}

        for s in strs:
            sort= ''.join(sorted(s))

            if sort not in strs_table:
                strs_table[sort] = []

            strs_table[sort].append(s)

        return list(strs_table.values())        
