class EmailAddress:
    def __init__(self, address: str):
        self._address = self.normalize_address(address)
        if not self._check_correct_email():
            raise ValueError(f"Invalid email address: {address}")

    def normalize_address(self, address: str) -> str:
        return address.lower().strip()

    def _check_correct_email(self) -> bool:
        if "@" not in self._address:
            return False

        domain = self._address.split('@')[1]
        return domain.endswith(('.com', '.ru', '.net'))

    @property
    def address(self) -> str:
        return self._address

    @property
    def masked(self) -> str:
        local_part, domain = self._address.split('@')
        masked_local = local_part[:2] + "***"
        return f"{masked_local}@{domain}"

    def __str__(self):
        return self.address

    def __repr__(self):
        return f"EmailAddress('{self.address}')"