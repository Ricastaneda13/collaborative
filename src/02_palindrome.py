def is_palindrome(text):
    text_list = list(text)
    if text_list==text_list[::-1]:
        print("is palindrome")
    else:
        print("not palindrome")