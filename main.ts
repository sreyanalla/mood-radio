radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    if (receivedNumber == 0) {
        basic.showIcon(IconNames.Happy)
    }
    
    if (receivedNumber == 1) {
        basic.showIcon(IconNames.Sad)
    }
    
    if (receivedNumber == 2) {
        basic.showIcon(IconNames.Angry)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendNumber(0)
    basic.showIcon(IconNames.Happy)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendNumber(1)
    basic.showIcon(IconNames.Sad)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    radio.sendNumber(2)
    basic.showIcon(IconNames.Angry)
})
basic.showString("How are you today?")
