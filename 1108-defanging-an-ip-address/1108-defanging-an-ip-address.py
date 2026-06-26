class Solution(object):
    def defangIPaddr(self, address):
        a=list(address)
        for i in range (len(a)):
            if a[i]=='.':
                a[i]='[.]'
        return ''.join(a)
        
        """
        :type address: str
        :rtype: str
        """
        