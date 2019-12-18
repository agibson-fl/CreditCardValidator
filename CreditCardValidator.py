import re

class CreditCardValidator():
    def execute(self, ccnum):
        if self.__badFirstCharacter(ccnum):
            return False
        
        if self.__badSeparatorGrouping(ccnum):
            return False
        
        stripped = self.__stripDashes(ccnum)
        if len(stripped) != 16:
            return False
        
        if self.__hasBadCharacters(stripped):
            return False
        
        if self.__hasTooManyConsecutiveDigits(stripped):
            return False
        
        return True
    
    def __get_first(self, ccnum):
        return next(iter(ccnum or []), None)
    
    def __badFirstCharacter(self, ccnum):
        return self.__get_first(ccnum) not in ['4', '5', '6']
    
    def __badSeparatorGrouping(self, ccnum):
        if '-' in ccnum:
            pattern = re.compile(r'(\d{4}-){3}(\d{4})')
            match = re.search(pattern, ccnum)
            if not match:
                return True
        return False
    
    def __stripDashes(self, ccnum):
        return ccnum.replace("-", "")
    
    def __hasBadCharacters(self, ccnum):
        return not ccnum.isdigit()
    
    def __hasTooManyConsecutiveDigits(self, ccnum):
        conseq = self.__get_first(ccnum)
        for char in ccnum[1:]:
            if conseq[0] == char:
                conseq += char
            else:
                conseq = char
            if len(conseq) > 3:
                return True            
        return False
