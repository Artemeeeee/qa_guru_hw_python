from dataclasses import dataclass
from typing import List, Optional

from src.email_adress import EmailAddress
from src.status import Status
from src.utils import clean_text


@dataclass
class Email:
    subject: str
    body: str
    sender: EmailAddress
    recipients: List[EmailAddress]
    date: Optional[str] = None
    short_body: Optional[str] = None
    status: Status = Status.DRAFT

    def __post_init__(self):

        if not isinstance(self.recipients, list):
            self.recipients = [self.recipients]

    def get_recipients_str(self) -> str:
        return ", ".join(str(recipient) for recipient in self.recipients)

    def clean_data(self) -> "Email":
        self.subject = clean_text(self.subject)
        self.body = clean_text(self.body)
        return self

    def add_short_body(self, n: int = 10) -> "Email":
        if not self.body:
            self.short_body = None
        elif len(self.body) <= n:
            self.short_body = self.body
        else:
            self.short_body = self.body[:n] + "..."
        return self

    def is_valid_fields(self) -> bool:
        """Проверяет, что поля subject и body заполнены"""
        return bool(self.subject and self.body and self.sender and self.recipients)


    def prepare(self) -> "Email":
        self.clean_data()
        self.add_short_body()
        if self.is_valid_fields():
            self.status = Status.READY
        else:
            self.status = Status.INVALID
        return self

    def __str__(self) -> str:
        recipients_str = self.get_recipients_str()
        body_to_show = self.short_body or self.body

        return (
            f"Status: {self.status}\n"
            f"Кому: {recipients_str}\n"
            f"От: {self.sender.masked}\n"
            f"Тема: {self.subject}, дата {self.date}\n"
            f"{body_to_show}"
        )
