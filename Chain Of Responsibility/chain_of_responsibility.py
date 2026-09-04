"""
CHAIN OF RESPONSIBILITY PATTERN

What is it?
- Behavioral design pattern.
- A request is passed through a chain of handlers.
- Each handler:
    1. performs its own responsibility
    2. decides whether to continue
    3. forwards the request to the next handler

In this example:

WebServer
    ↓
AuthenticatorHandler
    ↓
LoggerHandler
    ↓
CompressorHandler

Benefits:
- WebServer does not need to know every processing step.
- Handlers are independent from each other.
- New handlers can be added without changing WebServer.
- The order of handlers can easily be changed.
"""


from abc import ABC, abstractmethod


# ==================================================
# HTTP REQUEST
# ==================================================

class HttpRequest:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


# ==================================================
# ABSTRACT HANDLER
#
# Stores a reference to the next handler.
# Provides the common forwarding behavior.
# ==================================================

class Handler(ABC):

    def __init__(self, next_handler=None):
        self.__next = next_handler

    def handle(self, request: HttpRequest):

        # Let the concrete handler perform its own job.
        if not self.do_handle(request):
            return

        # If processing should continue,
        # forward the request to the next handler.
        if self.__next is not None:
            self.__next.handle(request)

    @abstractmethod
    def do_handle(self, request: HttpRequest) -> bool:
        pass


# ==================================================
# AUTHENTICATOR HANDLER
#
# Stops the chain if authentication fails.
# ==================================================

class Authenticator(Handler):

    def do_handle(self, request: HttpRequest) -> bool:

        print("Authentication")

        is_valid = (
            request.get_username() == "admin"
            and request.get_password() == "1234"
        )

        if not is_valid:
            print("Authentication failed")
            return False

        print("Authentication successful")

        return True


# ==================================================
# LOGGER HANDLER
#
# Logs the request, then allows the chain to continue.
# ==================================================

class Logger(Handler):

    def do_handle(self, request: HttpRequest) -> bool:

        print("Log")

        return True


# ==================================================
# COMPRESSOR HANDLER
#
# Compresses the response/request and continues.
# ==================================================

class Compressor(Handler):

    def do_handle(self, request: HttpRequest) -> bool:

        print("Compress")

        return True


# ==================================================
# WEB SERVER
#
# The WebServer knows only about the first Handler.
# It does not know the details of the whole chain.
# ==================================================

class WebServer:

    def __init__(self, handler: Handler):
        self.__handler = handler

    def handle(self, request: HttpRequest):
        self.__handler.handle(request)


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    # Build the chain from the end backwards.

    compressor = Compressor()

    logger = Logger(compressor)

    authenticator = Authenticator(logger)

    # WebServer only receives the first handler.
    server = WebServer(authenticator)

    request = HttpRequest("admin", "1234")

    server.handle(request)
