import hashlib
import requests



def length_check(password):
    length = len(password)
    if length < 8:
        return 0
    elif length < 12 and length > 7:
        return 1
    elif length < 16 and length > 12:
        return 2
    else:
        return 3
def num_specials(password):
    count = 0
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                       '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', 
                       "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|', 
                       '`', '~']
    for x in password:
        for y in special_characters:
            if x == y:
                count = count + 1
    return count
def num_uppers(password):
    count = 0
    for x in password:
        if x.isupper():
            count += 1
    return count
def num_lowers(password):
    count = 0
    for x in password:
        if x.islower():
            count += 1
    return count
def num_nums(password):
    count = 0
    nums = ['1','2','3','4','5','6','7','8','9','0']
    for x in password:
        for y in nums:
            if x == y:
                count += 1
    return count
def num_chars_calc(password):
    lowers = num_lowers(password)
    uppers = num_uppers(password)
    nums = num_nums(password)
    specials = num_specials(password)
    score = 0
    if uppers > 2:
        score = score + 3
    if uppers == 2:
        score = score + 2
    if uppers == 1:
        score = score + 1
    if nums > 2:
        score = score + 3
    if nums == 2:
        score = score + 2
    if nums == 1:
        score = score + 1
    if specials > 2:
        score = score + 3
    if specials == 2:
        score = score + 2
    if specials == 1:
        score = score + 1
    return score
def special_variety(password):
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
                           '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', 
                           "'", '"', ',', '.', '<', '>', '/', '?', '\\', '|', 
                           '`', '~','£']
    specials_count = []
    for x in special_characters:
        count = 0
        for y in password:
            if x == y:
                count = count + 1
        specials_count.append(count)
    highest = max(specials_count)
    repetition_score = 0
    if highest > 2:
        repetition_score = 1
    elif highest == 2:
        repetition_score = 2
    elif highest == 1:
        repetition_score = 3
    variety_count = 0
    for a in specials_count:
        if a > 0:
            variety_count += 1
    if variety_count == 0:
       varscore = 0
    elif variety_count == 1:
       varscore = 1
    elif variety_count == 2:
        varscore = 2
    else:
        varscore = 3
    total_score = (varscore + repetition_score)/2
    return total_score
def common_password_check(password):
    with open("10k-most-common.txt","r") as file:
        common_passwords = [line.strip() for line in file]
    score = 3
    for x in common_passwords:
        if x == password:
            score = 0
    return score
def predictable_dates_check(password):
    if len(password) > 3:
       x = 0
       while x < (len(password)-1):
               date = password[x:x+4]
               if date.isdigit():
                 date = int(date)
                 if 1926 < date and date < 2026:
                   return 0
                 else:
                   x = x + 1
               else:
                   x = x + 1
               
    return 3
def breach_check(password):
    num_of_leaks = 0
    count = 0
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper() # this hashes the password into a hexadecimal capital string and then the next two lines take the first 5 digits or last 5 digits of the hex string
    prefix = sha1[:5]
    suffix = sha1[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}") #this line takes from the API of previously leaked or breached passwords and looks for ones with the prefix of the current password
    for line in response.text.splitlines():
        if suffix in line:
            count = line.split(":")[1] #there is only one colon in what is returned and it is before the count number on how many times the password has come up in data leaks
            num_of_leaks = int(count)
    if num_of_leaks > 5000:
        return "very weak"
    elif num_of_leaks < 5001 and num_of_leaks > 1000:
        return "weak"
    elif num_of_leaks > 200 and num_of_leaks < 1001:

        return "medium"
    else:
        return "strong"
def common_pattern_check(password):
    keyboard_rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    password_lower = password.lower()
    for row in keyboard_rows:
        for x in range(len(row)- 3):
            substr = row[x:x+4]
            if substr in password_lower:
                return 0
    return 3
def Strength_calc(password):
    tips = []
    if num_chars_calc(password) < 4:
        tips.append("use a mix of numbers, capitals and special characters")
    if common_pattern_check(password) == 0:
        tips.append("you are using common keyboard patterns such as 'qwerty' don't do this")
    if breach_check(password) == "weak" or breach_check(password) == "very weak":
        tips.append("your password has been common in previous data breaches, use a more original password")
    if predictable_dates_check(password) == 0:
        tips.append("your password uses a recent date, this makes it easier to predict and could also give away personal information")
    if common_password_check(password) == 0:
        tips.append("this password is too common, use a more original password")
    if special_variety(password) == 0 or special_variety(password) == 1:
        tips.append("don't use too many of the same special character, and if you don't use any, try to use a variety")
    if length_check(password) == 0 or length_check(password) == 1:
        tips.append("Your password is too short, I would make it a bit longer for extra security")
    score = 0
    score = score + num_chars_calc(password) + common_pattern_check(password) + predictable_dates_check(password) + common_password_check(password) + special_variety(password) + length_check(password)
    max_score = 24
    percentage = (score / max_score) * 100
    percentage = round(percentage,0)
    if breach_check(password) == "strong":
        if percentage > 90:
            label = "VERY STRONG"
        elif percentage > 75 and percentage < 91:
            label = "STRONG"
        elif percentage < 76 and percentage > 50:
            label = "WEAK"
        else:
            label = "VERY WEAK"
    else:
      label = "TOO COMMON"
    return {
        "label": label,
        "score": percentage,
        "tips": tips
    }
