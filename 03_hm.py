import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^0-9+]', '', phone_number).strip()
    
    if cleaned_number.startswith('+'):
        if cleaned_number.startswith('+38'):
            return cleaned_number
        else:
            return '+38' + cleaned_number[1:]
    else:
        if cleaned_number.startswith('380'):
            return '+' + cleaned_number
        else:
            return '+38' + cleaned_number

print(normalize_phone("    +38(050)123-32-34")) 
print(normalize_phone("     0503451234"))     
print(normalize_phone("(050)8889900"))         
print(normalize_phone("38050-111-22-22"))       
print(normalize_phone("38050 111 22 11   "))