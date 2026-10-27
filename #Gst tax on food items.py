#Gst tax on food items 
menu = {"idli":40,"dosa":70,"paddu":45,"upma":35,"pulao":50}

food_name= input("Enter your food name:")
quantity=int(input("Enter your quantity:"))
total=menu[food_name]*quantity
gst_rate=18
gst_amount=total*gst_rate/100
total_amount=total+gst_amount
print(f"your ordered {quantity} {food_name} so bill is {total_amount} including GST ")