def on_received_value(name, value):
    global Received_Number
    if name == "left":
        basic.show_number(value)
        Received_Number = value
radio.on_received_value(on_received_value)

Received_Number = 0
Received_Number = 0
radio.set_group(1)

def on_forever():
    basic.show_number(Received_Number)
basic.forever(on_forever)
