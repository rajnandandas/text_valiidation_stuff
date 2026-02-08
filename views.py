from better_profanity import profanity

def has_profanity(text):
    """
    Check if the given text contains any profane words.

    Args:
        text (str): The text to be checked.
    """
    return profanity.contains_profanity(text)
    
# print(has_profanity("This is a clean sentence."))  # Expected output: False
# print(has_profanity("This is a damn sentence."))   # Expected output: True

def chk_length(text):
    """
    Check if the given text meets the minimum length requirement.

    Args:
        text (str): The text to be checked.
        min_length (int): The minimum required length of the text.
    """
    return len(text) >= 10