from abc import ABC, abstractmethod


class PaymentProvider(ABC):

    @abstractmethod
    def process(self):
        pass


class MyPayment(PaymentProvider):
     pass# it is going to be TypeError when instantiate(make object)
    # def process(self):
    #     print("Payment processed")


payment = MyPayment()
payment.process()