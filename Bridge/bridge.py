"""
BRIDGE PATTERN

What is Bridge?
- Bridge is a structural design pattern.
- It separates an abstraction/feature hierarchy from its
  implementation hierarchy so both can change independently.

Problem:
- Without Bridge, we may create classes like:

    SonyRemoteControl
    SonyAdvancedRemoteControl
    SamsungRemoteControl
    SamsungAdvancedRemoteControl

- Every new remote type combined with every new device brand
  creates more classes.

Solution:
- Separate the two dimensions:

    FEATURE hierarchy:
        RemoteControl
        AdvancedRemoteControl

    IMPLEMENTATION hierarchy:
        Device
        SonyTV
        SamsungTV

- RemoteControl HAS-A Device.
- RemoteControl delegates device-specific work to Device.

In this example:

RemoteControl          = Abstraction
AdvancedRemoteControl  = Refined Abstraction

Device                 = Implementation interface
SonyTV                 = Concrete Implementation

Key idea:

    RemoteControl does not care which brand the device is.

    RemoteControl
         |
         +---- Device
                 |
                 +---- SonyTV
                 +---- SamsungTV

Both sides can grow independently.
"""


from abc import ABC, abstractmethod


# ==================================================
# IMPLEMENTATION INTERFACE
#
# Represents the device side of the Bridge.
# ==================================================

class Device(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_channel(self, number):
        pass


# ==================================================
# CONCRETE IMPLEMENTATION
#
# Sony-specific device behavior.
# ==================================================

class SonyTV(Device):

    def turn_on(self):
        print("Sony TV: Turn ON")

    def turn_off(self):
        print("Sony TV: Turn OFF")

    def set_channel(self, number):
        print(f"Sony TV: Set channel to {number}")


# ==================================================
# ABSTRACTION / FEATURE
#
# RemoteControl contains a Device.
#
# It does NOT know whether the device is:
# - Sony
# - Samsung
# - LG
# etc.
#
# It simply delegates the work to Device.
# ==================================================

class RemoteControl:

    def __init__(self, device: Device):
        self._device = device

    def turn_on(self):
        self._device.turn_on()

    def turn_off(self):
        self._device.turn_off()


# ==================================================
# REFINED ABSTRACTION
#
# Adds more features to RemoteControl.
#
# Notice that this class still works with ANY Device.
# ==================================================

class AdvancedRemoteControl(RemoteControl):

    def set_channel(self, number):
        self._device.set_channel(number)


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    sony_tv = SonyTV()

    # Basic remote controlling Sony TV
    remote = RemoteControl(sony_tv)

    remote.turn_on()
    remote.turn_off()

    print("-----")

    # Advanced remote controlling the SAME Sony TV type
    advanced_remote = AdvancedRemoteControl(sony_tv)

    advanced_remote.turn_on()
    advanced_remote.set_channel(10)
    advanced_remote.turn_off()
