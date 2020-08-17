def on_received_number(receivedNumber):
    if receivedNumber == 0:
        basic.show_icon(IconNames.HAPPY)
    if receivedNumber == 1:
        basic.show_icon(IconNames.SAD)
    if receivedNumber == 2:
        basic.show_icon(IconNames.ANGRY)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(0)
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(1)
    basic.show_icon(IconNames.SAD)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    radio.send_number(2)
    basic.show_icon(IconNames.ANGRY)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

basic.show_string("How are you today?")