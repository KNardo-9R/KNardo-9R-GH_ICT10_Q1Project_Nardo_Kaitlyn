from pyscript import display, document

# FOR HOMEPAGE 

product_names = ['Adobong Mani','Taho','Omelet','Sinigang','Sisig'] # list
business_hours_opening = 8 # integer
business_hours_closing = 12 # integer
menu_prices = ['₱120','₱20','₱240','₱300','₱367'] # list 


display(f'OPENING & CLOSING TIMES: {business_hours_opening}AM-{business_hours_closing}PM', target='times')
display(f'{product_names[0]}', target='AdobongMani')
display(f'{product_names[1]}', target='Taho')
display(f'{product_names[2]}', target='Omelet')
display(f'{product_names[3]}', target='Sinigang')
display(f'{product_names[4]}', target='Sisig')

display(f'{menu_prices[0]}', target='AdobongManiPrice')
display(f'{menu_prices[1]}', target='TahoPrice')
display(f'{menu_prices[2]}', target='OmeletPrice')
display(f'{menu_prices[3]}', target='SinigangPrice')
display(f'{menu_prices[4]}', target='SisigPrice')

