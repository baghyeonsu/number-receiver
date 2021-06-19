radio.onReceivedValue(function (name, value) {
    if (name == "left") {
        Received_Number = value
    }
})
let Received_Number = 0
Received_Number = 0
radio.setGroup(1)
basic.forever(function () {
    basic.showNumber(Received_Number)
})
