# Remember to reach out for help after your own due diligence

def analyze_text(text):
    # Your code here
    alpha_count = 0
    e_count = 0

    for i in text:
        if i.isalpha() == True:
            alpha_count += 1
            if i == 'e':
                e_count += 1
            if i == 'E':
                e_count += 1

    e_percent = (e_count / alpha_count) * 100

    return ("The text contains " + repr(alpha_count) + " alphabetic characters, of which " + repr(e_count) + " "
          + "(" + ("%.2f" % e_percent) + "%)" + " are 'e'.")
