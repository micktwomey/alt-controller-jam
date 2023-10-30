import usb_hid

# from alt_controller_jam.usb_hid_gamepad import gamepad
# from alt_controller_jam.usb_hid_ps3 import ps3

usb_hid.enable(
    (
        usb_hid.Device.KEYBOARD,
        # gamepad,
        # ps3,
    )
)
