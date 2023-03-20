from __future__ import annotations
from abc import ABC, abstractmethod


class IEmailService(ABC):
    @abstractmethod
    def send_activation_email(self, email: str, msg: str) -> None:
        pass


class MockEmailService(IEmailService):
    def send_activation_email(self, email: str, msg: str) -> None:
        return email
