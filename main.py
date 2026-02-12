from pyscript import document, display



def validate_form(e):
    document.getElementById("output").innerHTML = ' '  #clears the output div for new output
    name = document.getElementById("name").value
    pass1 = document.getElementById("pass1").value

    i = name
    p = pass1

    uca = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # uppercase alphabet for checking
    num = '0123456789'  # numbers for checking

    if len(i) >= 7:  # username must be at least 7 characters long
        nval = True
    else:
        nval = False

    p2 = False
    p3 = False
    plen = False
    
    if len(p) >= 10:  # password must be at least 10 characters long
        plen = True
        for char in p:
            if char in uca:   # password must contain at least one uppercase letter
                p2 = True
            if char in num:   # password must contain at least one number
                p3 = True

    if p2 == False and plen == True:
        display("*password must contain at least one uppercase letter", target="output")
    if p3 == False and plen == True:
        display("*password must contain at least one number", target="output")
    if plen == False:
        display("*password must be at least 10 characters long", target="output")
        
    pval = p2 and p3 and plen    # validity checking and variable combining for easier checking



    if pval == True:    # validity checking and displaying for password
        display("password is valid", target="output")
    else:
        display("password is invalid, try again!", target="output")
    
    if nval == True:    # validity checking and displaying for username
        display("username is valid", target="output")
    else:
        display("username is invalid, try again!", target="output")

    if pval == True and nval == True:    #if both are correct 
        display("submitted!", target="output")