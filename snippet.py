#!/usr/bin/python3

from amazfit import Core2

chip = Core2.find(timeout=10)
if chip is None:
    print("ERROR: no device found!")
print (chip)

chip.connect()
chip.pair()
print(f"Pairing key: {chip.key}")
chip.read_info()
print(
    f"Device Information:\n"
    f"- name: {chip.name}\n"
    f"- address: {chip.address}\n"
    f"- serial number: {chip.serial_number}\n"
    f"- hardware version: {chip.hardware_rev}\n"
    f"- software version: {chip.software_rev}"
)
def on_steps_callback(steps):
    print(f"- steps changed, new value: {steps}")

chip.on_steps(on_steps_callback)
chip.wait_until_break()
