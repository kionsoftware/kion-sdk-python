from enum import Enum

class DiagnosticBillingReportListStatus(str, Enum):
    DELETED = "deleted"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"
    PROCESSED = "processed"
    QUEUED = "queued"
    SYNCED = "synced"
    SYNC_NEEDED = "sync_needed"

    def __str__(self) -> str:
        return str(self.value)
