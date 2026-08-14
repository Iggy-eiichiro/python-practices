from abc import ABC, abstractmethod


class PaymentProvider(ABC):

    @abstractmethod
    def process(self):
        pass


class MyPayment(PaymentProvider):

    def process(self):
        print("Payment processed")


payment = MyPayment()
payment.process()