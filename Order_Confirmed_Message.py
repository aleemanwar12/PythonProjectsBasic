name = input("What's your name: ")
phone = input("provide your phone number: ")

def order_confirmed_msg(name, phone):
    print(f"Hi! {name}")
    print("Thanks for shopping with us")
    print(f"We'll contact you with delivery updates on {phone}")


order_confirmed_msg(name, phone)

