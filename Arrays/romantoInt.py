# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
def romantoInt(str):
    finalSum = 0
    prev_value = 0

    roman_dict = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }

    for char in str:
        if char in roman_dict:
            current_value = roman_dict[char]
            if current_value > prev_value:
                finalSum += prev_value - current_value
        else:
            return "Illegal Charecter detected"
            break
        
    return finalSum

print(romantoInt("MCMXCIV"))

