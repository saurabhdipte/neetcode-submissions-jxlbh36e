class Solution:
    def checkValidString(self, s: str) -> bool:
        nstack=[]
        sstack=[]
        for i,char in enumerate(s):
            if char=="(":
                nstack.append(i)
            elif char=="*":
                sstack.append(i)
            else:
                if not nstack and not sstack:
                    return False
                if nstack:
                    nstack.pop()
                else:
                    sstack.pop()
        while nstack and sstack:
            if sstack[-1]<nstack[-1]:
                return False
            nstack.pop()
            sstack.pop()
        if len(nstack)>0:
            return False
        else:
            return True
