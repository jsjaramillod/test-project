class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(nums)<2:
            return 0
        
        v=[]
        w=[]
        for i in range(len(nums)):
            
            if i%2==0:
                v=v+[nums[i]]
                
            elif i%2!=0:
                w=w+[nums[i]]
        def coun(V):
            m=mode(V)
            cont=0
            for k in range(len(V)):
                if V[k]!=m:
                    V[k]=m
                    cont=cont+1
            return cont
        
        if mode(v)==mode(w):
            return(+coun(w))
    
    
        elif mode(v)!=mode(w):   
             return coun(w)+coun(v)
             print(coun(w)+coun(v))
