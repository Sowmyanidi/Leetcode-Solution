class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        roman = ''
        while(num>0):
            if s[0]!='9' and s[0]!='4':
                if num>=1000:
                    num-=1000
                    roman+='M'
                elif num>=500 and num<1000:
                    num-=500
                    roman+='D'
                elif num>=100 and num<500:
                    num-=100
                    roman+='C'
                elif num>=50 and num<100:
                    num-=50
                    roman+='L'
                elif num>=10 and num<50:
                    num-=10
                    roman+='X'
                elif num>=5 and num<10:
                    num-=5
                    roman+='V'
                elif num>=1 and num<5:
                    num-=1
                    roman+='I'
            else:
                if num>=900 and num<1000:
                    roman+='CM'
                    num-=900
                elif num>=90 and num<100:
                    roman+='XC'
                    num-=90
                elif num>=9 and num<10:
                    roman+='IX'
                    num-=9
                elif num>=400 and num<500:
                    roman+='CD'
                    num-=400
                elif num>=40 and num<50:
                    roman+='XL'
                    num-=40
                elif num>=4 and num<5:
                    roman+='IV'
                    num-=4
                
            s = str(num)
        return roman

sol = Solution()
print(sol.intToRoman(1994))