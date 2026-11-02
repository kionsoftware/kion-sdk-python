from enum import Enum

class SubscriptionCSPBillingInfoBillingCycle(str, Enum):
    ANNUAL = "annual"
    MONTHLY = "monthly"
    NONE = "none"
    ONE_TIME = "one_time"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
