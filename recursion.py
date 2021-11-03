def rec():
    a = input('Do you want to know what\'s recursion? (write "yes" or "no") \n')
    if a.upper() == "YES":
        rec()
    else:
        print("\nfuck you")
        return 0


rec()