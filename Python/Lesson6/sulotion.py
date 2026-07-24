import re

def to_camel_case(text):
    # Split the string on either "-" or "_"
    words = re.split(r'[-_]', text)

    # If the string is empty, return it
    if not words:
        return ""

    # Keep the first word exactly as it is
    camel = words[0]

    # Capitalize every remaining word
    for word in words[1:]:
        camel += word.capitalize()

    return camel