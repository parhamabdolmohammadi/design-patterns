class MailService:
    # Abstraction hides unnecessary implementation details from
    # the code that uses this class.
    #
    # The caller only needs to know about send_mail().
    # It does NOT need to know how we connect, authenticate,
    # or disconnect.
    #
    # This also reduces coupling. If we change how connection or
    # authentication works, the code using MailService does not
    # need to change, as long as send_mail() keeps the same interface.

    def send_mail(self):
        self.__connect()
        self.__authenticate()

        print("Mail Sent")

        self.__disconnect()

    def __connect(self):
        # Internal implementation detail hidden from the caller
        print("connect")

    def __disconnect(self):
        # Internal implementation detail hidden from the caller
        print("disconnect")

    def __authenticate(self):
        # Internal implementation detail hidden from the caller
        print("authenticate")
