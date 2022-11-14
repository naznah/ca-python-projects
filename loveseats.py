#This is a Codecademy project for building a simple inventory and receipts for customers.

#Greeting
greeting = "Thank you for shopping at Lovely Loveseats for Neat Suites on Fleet Street. Have a pleasant day."

#Sales tax
sales_tax = 0.088

#Item 1
lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

#Item 2
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inchces high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

#Item 3
luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

#Customer one
customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization = "Lovely Loveseat, " + "Luxurious Lamp." 
customer_one_tax = customer_one_total * sales_tax

print("Customer One items: ", customer_one_itemization)
print("Customer One total (before tax): £", customer_one_total)
print("Customer One sales tax: £", customer_one_tax)
print("Customer One grand total: £", customer_one_tax + customer_one_total)
print()
print(greeting)