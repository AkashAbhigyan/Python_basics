class EmailService:

    def _connect(self):
        print("Connecting to the server....")
    def _authenticate(self,email):
        print(f"Auntheticating email {email}")
    
    def _disconnect(self):
        print("disconnecting....")

    def show(self):
        self._connect()
        self._authenticate("slsdj2280@gmail.com")
        print("Sending email.")
        self._disconnect()

email = EmailService()
email.show()
