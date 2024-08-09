while True:
    m_inp = input("""Do you want to buy a -
1. Computer
2. Printer
3. Exit
                  
Option -> """)
    if m_inp == "1":
        inp = input("""Do you want a -
1. Desktop
2. Laptop

Option -> """)
        if inp == '1':
            print("Price is 35000 Rs.")
        elif inp=='2':
            print("Price is 60000 Rs.")
    elif m_inp=='2':
        inp = input("""Do you want a -
1. Laser printer
2. Inkjet printer

Option -> """)
        if inp == '1':
            print("Price is 10000 Rs.")
        elif inp=='2':
            print("Price is 8000 Rs.")
    elif m_inp == '3':
        break
        