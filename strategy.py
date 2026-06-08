import asyncio
from abc import ABC, abstractmethod

class NotificationSender(ABC):
    @abstractmethod
    async def send_message(self, text: str) -> str:
        """Каждая стратегия должна реализовать этот метод асинхронно"""
        pass

class EmailDelivery(NotificationSender):
    async def send_message(self, text: str) -> str:
        await asyncio.sleep(0.5)
        return f"[EMAIL SENT]: {text.strip()}"

class SmsDelivery(NotificationSender):
    async def send_message(self, text: str) -> str:
        await asyncio.sleep(0.5)
        return f"[SMS SENT]: {text[:10]}..."

class NotificationService:
    def __init__(self, delivery_method: NotificationSender):
        self._method = delivery_method

    @property
    def method(self) -> NotificationSender:
        return self._method

    @method.setter
    def method(self, new_method: NotificationSender):
        self._method = new_method

    async def broadcast(self, message: str) -> str:
        return await self._method.send_message(message)

async def main():
    notifier = NotificationService(EmailDelivery())
    result_email = await notifier.broadcast("Привет, это важное уведомление! ")
    print(result_email)  

    notifier.method = SmsDelivery()
    result_sms = await notifier.broadcast("Привет, это важное уведомление! ")
    print(result_sms)

if __name__ == "__main__":
    asyncio.run(main())
