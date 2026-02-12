import random
from abc import ABC, abstractmethod

class UserAccount:
    def __init__(self, username, balance, password):
        self.username = username
        self._balance = balance
        self.__password = password

    def login_check(self, username, password):
        if self.username == username and self.__password == password:
            print("OK!")
        else:
            print("Wrong username or password!")

    def get_balance(self, username, password):
        if self.username(username, password):
            return self._balance
        else:
            return None

    def __random_pass(self):
        return str(random.randint(1000, 9999))

    def reset_password(self):
        if self.username == self.username:
            self.__password = self.__random_pass()
            print("Password was reset")
        else:
            print("Wrong login!")


user = UserAccount("Ardager", 1000, "123123")

print(user.username)
print(user._balance)

print("Balance:", user.get_balance("Ardager", "123123"))

user.reset_password("Ardager", "123123")

print("Balance with old password:", user.get_balance("Ardager", "123123"))


class SendOTP(ABC):

    @abstractmethod
    def send_otp_to_phone(self, phone, code):
        pass

    @abstractmethod
    def send_otp_to_email(self, email, code):
        pass


class SendOTPKG(SendOTP):

    def send_otp_to_phone(self, phone, code):
        print(f"[KG SMS] Send {code} to {phone}")

    def send_otp_to_email(self, email, code):
        print(f"[KG EMAIL] Send {code} to {email}")


class SendOTPKZ(SendOTP):

    def send_otp_to_phone(self, phone, code):
        data = {
            "country": "KZ",
            "phone": phone,
            "otp": code
        }
        print("[KZ SMS JSON]", data)

    def send_otp_to_email(self, email, code):
        xml = f"<otp><email>{email}</email><code>{code}</code></otp>"
        print("[KZ EMAIL XML]", xml)


otp_kg = SendOTPKG()
otp_kz = SendOTPKZ()

otp_kg.send_otp_to_phone("+996700111222", "3456")
otp_kg.send_otp_to_email("a@mail.com", "3456")

otp_kz.send_otp_to_phone("+77001112233", "9999")
otp_kz.send_otp_to_email("b@mail.com", "9999")
