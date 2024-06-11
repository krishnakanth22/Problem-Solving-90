class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr_set=set(arr2)
        arr_count=defaultdict(int)
        end=[]
        for n in arr1:
            if n not in arr_set:
                end.append(n)
            arr_count[n]+=1
        end.sort()
        res=[]
        for i in arr2:
            res.extend([i]*arr_count[i])
        res.extend(end)

        return res
