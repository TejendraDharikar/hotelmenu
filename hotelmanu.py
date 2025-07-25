# making dictionary of food items(menu)

menu={
    'pizza':40,
    'pasta':50,
    'burger':60,
    'saled':70,
    'coffee':80,
}



# displays welcome and food items

print("welcome to python resturent")
print("pizza:rs40\npasta:rs50\nburger:rs60\nsalad:rs70\ncoffee:rs80")

order_total=0


# enter first order

item_1=input("enter the name of the item you want to order=")
if item_1 in menu:
    order_total+= menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print(f"ordered item {item_1} is not available yet!")



#choose if u want another item

another_order=input("do you want to add another item? (yes/no) ")
if another_order=="yes" or another_order=="y":



    # enter name of another item

    item_2=input("enter the name of second item=")
    if item_2 in menu:
         order_total +=menu[item_2]
         print(f"Item {item_2} has been added to order")
    else:
         print(F"ordered item {item_2 }is not available")



# displays the total amount

print(f"the total amount of item to pay is {order_total}")