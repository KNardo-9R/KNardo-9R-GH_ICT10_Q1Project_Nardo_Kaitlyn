from pyscript import display, document

# FOR CONTACT

has_delivery = True # boolean
popular_item_price = 200 # integer
product_names = ['Adobong Mani','Taho','Omelet','Sinigang','Sisig'] # list
business_hours_opening = 8 # integer
business_hours_closing = 12 # integer
menu_prices = ['₱120','₱20','₱240','₱300','₱367'] # list 
common_allergens = ['Peanuts','Soybeans','Egg', 'Milk']  #   list 
tax_rate = 12.00 # float


display(f'OPENING & CLOSING TIMES: {business_hours_opening}AM-{business_hours_closing}PM', target='times')
display(f'DELIVERY: {has_delivery}', target="delivery")
display(f'TAX RATE: {tax_rate}', target="tax")
