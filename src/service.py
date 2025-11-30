import copy
from datetime import datetime
from typing import List

from src.email import Email
from src.status import Status


class EmailService:


    def add_send_date(self) -> str:
        return datetime.now().strftime("%Y-%m-%d")

    def send_email(self, email: Email) -> List[Email]:
        """Возвращает список отправленных писем"""
        sent_emails = []

        for recipient in email.recipients:
            email_copy = copy.deepcopy(email)
            email_copy.recipients = [recipient]
            email_copy.date = self.add_send_date()
            if email.status == Status.READY:
                email_copy.status = Status.SENT
            else:
                email_copy.status = Status.FAILED

            sent_emails.append(email_copy)

        return sent_emails