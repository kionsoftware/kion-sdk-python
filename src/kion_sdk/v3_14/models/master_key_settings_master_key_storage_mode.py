from enum import Enum

class MasterKeySettingsMasterKeyStorageMode(str, Enum):
    AWS = "aws"
    DATABASE = "database"

    def __str__(self) -> str:
        return str(self.value)
