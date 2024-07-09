def number_to_words(n):
   
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
            "sixteen", "seventeen", "eighteen", "nineteen"]
    
    
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    if n == 1000:
        return "one thousand"
    elif n >= 100:
        hundreds = ones[n // 100] + " hundred"
        rest = n % 100
        if rest == 0:
            return hundreds
        else:
            return hundreds + " and " + number_to_words(rest)
    elif n >= 20:
        return tens[n // 10] + " " + ones[n % 10]
    else:
        return ones[n]

def count_letters_in_numbers():
    total_letters = 0
    for i in range(1, 1001):
        words = number_to_words(i)
        
        letters = len(words.replace(" ", "").replace("-", ""))
        total_letters += letters
    return total_letters


total_letters = count_letters_in_numbers()
print("Total letters used:", total_letters)
