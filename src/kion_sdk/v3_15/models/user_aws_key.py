from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.null_uint import NullUint





T = TypeVar("T", bound="UserAWSKey")



@_attrs_define
class UserAWSKey:
    """ UserAWSKey defines the state of a user AWS key

        Attributes:
            access_key_expiring_notice (bool | None | Unset): Whether notification for expiring access key will be sent.
            account_id (int | None | Unset): ID of the account associated with this AWS key. Example: 123.
            aws_iam_path (str | Unset): Path to the IAM user in AWS. Example: /service/admin/.
            aws_iam_user_arn (str | Unset): Amazon Resource Name (ARN) for the IAM user. Example:
                arn:aws:iam::123456789012:user/johndoe.
            aws_iam_username (str | Unset): IAM username in AWS. Example: johndoe.
            created_at (datetime.datetime | Unset): Timestamp when the AWS key was created. Example: 2023-04-15T14:32:10Z.
            enabled (bool | None | Unset): Whether the AWS key is enabled. Example: True.
            id (int | Unset): Unique identifier for the user AWS key. Example: 1.
            key_id (str | Unset): ID of the access key. Example: AKIAIOSFODNN7EXAMPLE.
            ou_cloud_access_role_id (NullUint | Unset): NullUint represents a uint that may be NULL.
            resource_role_id (NullUint | Unset): NullUint represents a uint that may be NULL.
            user_enabled (bool | None | Unset): Whether the user is enabled. Example: True.
            user_id (int | None | Unset): ID of the user who owns this AWS key. Example: 42.
     """

    access_key_expiring_notice: bool | None | Unset = UNSET
    account_id: int | None | Unset = UNSET
    aws_iam_path: str | Unset = UNSET
    aws_iam_user_arn: str | Unset = UNSET
    aws_iam_username: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    id: int | Unset = UNSET
    key_id: str | Unset = UNSET
    ou_cloud_access_role_id: NullUint | Unset = UNSET
    resource_role_id: NullUint | Unset = UNSET
    user_enabled: bool | None | Unset = UNSET
    user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.null_uint import NullUint
        access_key_expiring_notice: bool | None | Unset
        if isinstance(self.access_key_expiring_notice, Unset):
            access_key_expiring_notice = UNSET
        else:
            access_key_expiring_notice = self.access_key_expiring_notice

        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        aws_iam_path = self.aws_iam_path

        aws_iam_user_arn = self.aws_iam_user_arn

        aws_iam_username = self.aws_iam_username

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        id = self.id

        key_id = self.key_id

        ou_cloud_access_role_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ou_cloud_access_role_id, Unset):
            ou_cloud_access_role_id = self.ou_cloud_access_role_id.to_dict()

        resource_role_id: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resource_role_id, Unset):
            resource_role_id = self.resource_role_id.to_dict()

        user_enabled: bool | None | Unset
        if isinstance(self.user_enabled, Unset):
            user_enabled = UNSET
        else:
            user_enabled = self.user_enabled

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_key_expiring_notice is not UNSET:
            field_dict["access_key_expiring_notice"] = access_key_expiring_notice
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if aws_iam_path is not UNSET:
            field_dict["aws_iam_path"] = aws_iam_path
        if aws_iam_user_arn is not UNSET:
            field_dict["aws_iam_user_arn"] = aws_iam_user_arn
        if aws_iam_username is not UNSET:
            field_dict["aws_iam_username"] = aws_iam_username
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if key_id is not UNSET:
            field_dict["key_id"] = key_id
        if ou_cloud_access_role_id is not UNSET:
            field_dict["ou_cloud_access_role_id"] = ou_cloud_access_role_id
        if resource_role_id is not UNSET:
            field_dict["resource_role_id"] = resource_role_id
        if user_enabled is not UNSET:
            field_dict["user_enabled"] = user_enabled
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.null_uint import NullUint
        d = dict(src_dict)
        def _parse_access_key_expiring_notice(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        access_key_expiring_notice = _parse_access_key_expiring_notice(d.pop("access_key_expiring_notice", UNSET))


        def _parse_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        aws_iam_path = d.pop("aws_iam_path", UNSET)

        aws_iam_user_arn = d.pop("aws_iam_user_arn", UNSET)

        aws_iam_username = d.pop("aws_iam_username", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        id = d.pop("id", UNSET)

        key_id = d.pop("key_id", UNSET)

        _ou_cloud_access_role_id = d.pop("ou_cloud_access_role_id", UNSET)
        ou_cloud_access_role_id: NullUint | Unset
        if isinstance(_ou_cloud_access_role_id,  Unset):
            ou_cloud_access_role_id = UNSET
        else:
            ou_cloud_access_role_id = NullUint.from_dict(_ou_cloud_access_role_id)




        _resource_role_id = d.pop("resource_role_id", UNSET)
        resource_role_id: NullUint | Unset
        if isinstance(_resource_role_id,  Unset):
            resource_role_id = UNSET
        else:
            resource_role_id = NullUint.from_dict(_resource_role_id)




        def _parse_user_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        user_enabled = _parse_user_enabled(d.pop("user_enabled", UNSET))


        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        user_aws_key = cls(
            access_key_expiring_notice=access_key_expiring_notice,
            account_id=account_id,
            aws_iam_path=aws_iam_path,
            aws_iam_user_arn=aws_iam_user_arn,
            aws_iam_username=aws_iam_username,
            created_at=created_at,
            enabled=enabled,
            id=id,
            key_id=key_id,
            ou_cloud_access_role_id=ou_cloud_access_role_id,
            resource_role_id=resource_role_id,
            user_enabled=user_enabled,
            user_id=user_id,
        )


        user_aws_key.additional_properties = d
        return user_aws_key

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
