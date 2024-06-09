def romanToInt(s: str) -> int:
    symbols = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    number = 0
    for i in range(len(s)-1):
        if symbols[s[i]]<symbols[s[i+1]]:
            number-=symbols[s[i]]
        else:
            number+=symbols[s[i]]
        
    number+=symbols[s[-1]]
    return number

print(romanToInt("MCMXCIV"))