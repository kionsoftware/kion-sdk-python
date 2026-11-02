from enum import Enum

class UserCloudAccessFavoriteCloudServiceProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"
    OCI = "oci"

    def __str__(self) -> str:
        return str(self.value)
