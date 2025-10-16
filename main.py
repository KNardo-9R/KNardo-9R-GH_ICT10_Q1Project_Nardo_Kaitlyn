from pyscript import display, document

# --- FOR ORDER PAGE ---

def details_pop(e):
    document.getElementById('output').innerHTML = " "

# ITEMS
    fooda = document.getElementById('food1')
    foodb = document.getElementById('food2')
    foodc = document.getElementById('food3')
    foodd = document.getElementById('food4')
    foode = document.getElementById('food5')
# ITEM VALUES
    food1 = float(document.getElementById('food1').value)
    food2 = float(document.getElementById('food2').value)
    food3 = float(document.getElementById('food3').value)
    food4 = float(document.getElementById('food4').value)
    food5 = float(document.getElementById('food5').value)
# CUSTOMER INFO
    customer_name = document.getElementById('custname').value 
    customer_address = document.getElementById('custaddress').value
    customer_contact = document.getElementById('custnumber').value

    total = (food1) * fooda.checked + (food2) * foodb.checked + (food3) * foodc.checked + (food4) * foodd.checked + (food5) * foode.checked

# WHAT WILL POPUP 
    order_info = f"""

    Customer Name: {customer_name}
    Customer Address: {customer_address}
    Customer Contact: {customer_contact}
    Total of Order: {total} Pesos

    """

# FOR POPUP TO APPEAR
    display(order_info, target="output")



