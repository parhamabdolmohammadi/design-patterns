"""
FACADE PATTERN

What is Facade?
- Facade is a structural design pattern.
- It provides a simple interface to a complex subsystem.

Problem:
- Sending a notification requires the client to know many steps:
    1. Create NotificationServer
    2. Connect
    3. Authenticate
    4. Create Message
    5. Send
    6. Disconnect

- The client becomes coupled to many subsystem classes and
  needs to know the correct order of operations.

Solution:
- Create a Facade that hides these steps.
- The client calls one simple method:

      notification_service.send(...)

- The Facade handles the complicated workflow internally.

In this example:

NotificationService = Facade

NotificationServer
Connection
AuthToken
Message             = Subsystem classes

Key idea:

    Complex subsystem:
    connect → authenticate → send → disconnect

    Facade:
    send()

The Facade does NOT replace the subsystem.
It simply provides an easier interface to use it.
"""


# ==================================================
# SUBSYSTEM CLASSES
# ==================================================

class Message:

    def __init__(self, content):
        self.__content = content


class AuthToken:
    pass


class Connection:

    def disconnect(self):
        print("Disconnecting")


class NotificationServer:

    def connect(self, ip_address: str):
        print("Connecting")
        return Connection()

    def authenticate(self, app_id: str, key: str):
        print("Authenticating")
        return AuthToken()

    def send(
        self,
        auth_token: AuthToken,
        message: Message,
        target: str
    ):
        print("Sending a message")


# ==================================================
# FACADE
#
# Provides a simple interface to the complicated
# notification subsystem.
# ==================================================

class NotificationService:

    def send(self, message: str, target: str):

        # The client doesn't need to know about
        # any of these individual steps.

        server = NotificationServer()

        connection = server.connect("ip")

        auth_token = server.authenticate(
            "appID",
            "Key"
        )

        message = Message(message)

        server.send(
            auth_token,
            message,
            target
        )

        connection.disconnect()


# ==================================================
# MAIN / CLIENT
# ==================================================

if __name__ == "__main__":

    service = NotificationService()

    service.send(
        "Hello World",
        "target"
    )
