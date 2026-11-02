from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.null_string import NullString
  from ..models.null_time import NullTime





T = TypeVar("T", bound="AMICreate")



@_attrs_define
class AMICreate:
    """ AMICreate defines an AMI creation where the AMI lives in an account managed by cloudtamer.io.

        Attributes:
            account_id (int | None): AWS account application ID where the AMI is stored. Example: 1.
            aws_ami_id (str): Image ID of the AMI from AWS. Example: ami-123456.
            name (str): Name of the AMI in the application. Example: rhel-7-5-20180213.
            region (str): AWS region where the AMI exists. Example: us-east-1.
            description (str | Unset): Description for the AMI in the application. Example: Gold image for RHEL 7.5..
            expiration_alert_number (int | Unset): TThe amount of time before the expiration alert is shown Example: 1.
            expiration_alert_unit (NullString | Unset): NullString represents a string that may be NULL.
            expiration_notify (bool | None | Unset): Will notify the owners that the shared AMI has expired Example: True.
            expiration_warning_number (int | Unset): The amount of time before the expiration warning is sent Example: 1.
            expiration_warning_unit (NullString | Unset): NullString represents a string that may be NULL.
            expires_at (NullTime | Unset): NullTime represents a time.Time that may be NULL.
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the ami. Is required if no
                owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the ami. Is required if no owner group
                IDs are listed. Example: [1, 2].
            sync_deprecation (bool | None | Unset): Will sync the expiration date from the system into the AMI in AWS.
                Example: True.
            sync_tags (bool | None | Unset): Will sync the AWS tags from the source AMI into all the accounts where the AMI
                is shared. Example: True.
     """

    account_id: int | None
    aws_ami_id: str
    name: str
    region: str
    description: str | Unset = UNSET
    expiration_alert_number: int | Unset = UNSET
    expiration_alert_unit: NullString | Unset = UNSET
    expiration_notify: bool | None | Unset = UNSET
    expiration_warning_number: int | Unset = UNSET
    expiration_warning_unit: NullString | Unset = UNSET
    expires_at: NullTime | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    sync_deprecation: bool | None | Unset = UNSET
    sync_tags: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.null_string import NullString
        from ..models.null_time import NullTime
        account_id: int | None
        account_id = self.account_id

        aws_ami_id = self.aws_ami_id

        name = self.name

        region = self.region

        description = self.description

        expiration_alert_number = self.expiration_alert_number

        expiration_alert_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration_alert_unit, Unset):
            expiration_alert_unit = self.expiration_alert_unit.to_dict()

        expiration_notify: bool | None | Unset
        if isinstance(self.expiration_notify, Unset):
            expiration_notify = UNSET
        else:
            expiration_notify = self.expiration_notify

        expiration_warning_number = self.expiration_warning_number

        expiration_warning_unit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expiration_warning_unit, Unset):
            expiration_warning_unit = self.expiration_warning_unit.to_dict()

        expires_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.to_dict()

        owner_user_group_ids: list[int] | None | Unset
        if isinstance(self.owner_user_group_ids, Unset):
            owner_user_group_ids = UNSET
        elif isinstance(self.owner_user_group_ids, list):
            owner_user_group_ids = self.owner_user_group_ids


        else:
            owner_user_group_ids = self.owner_user_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids


        else:
            owner_user_ids = self.owner_user_ids

        sync_deprecation: bool | None | Unset
        if isinstance(self.sync_deprecation, Unset):
            sync_deprecation = UNSET
        else:
            sync_deprecation = self.sync_deprecation

        sync_tags: bool | None | Unset
        if isinstance(self.sync_tags, Unset):
            sync_tags = UNSET
        else:
            sync_tags = self.sync_tags


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_id": account_id,
            "aws_ami_id": aws_ami_id,
            "name": name,
            "region": region,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if expiration_alert_number is not UNSET:
            field_dict["expiration_alert_number"] = expiration_alert_number
        if expiration_alert_unit is not UNSET:
            field_dict["expiration_alert_unit"] = expiration_alert_unit
        if expiration_notify is not UNSET:
            field_dict["expiration_notify"] = expiration_notify
        if expiration_warning_number is not UNSET:
            field_dict["expiration_warning_number"] = expiration_warning_number
        if expiration_warning_unit is not UNSET:
            field_dict["expiration_warning_unit"] = expiration_warning_unit
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if sync_deprecation is not UNSET:
            field_dict["sync_deprecation"] = sync_deprecation
        if sync_tags is not UNSET:
            field_dict["sync_tags"] = sync_tags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.null_string import NullString
        from ..models.null_time import NullTime
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        account_id = _parse_account_id(d.pop("account_id"))


        aws_ami_id = d.pop("aws_ami_id")

        name = d.pop("name")

        region = d.pop("region")

        description = d.pop("description", UNSET)

        expiration_alert_number = d.pop("expiration_alert_number", UNSET)

        _expiration_alert_unit = d.pop("expiration_alert_unit", UNSET)
        expiration_alert_unit: NullString | Unset
        if isinstance(_expiration_alert_unit,  Unset):
            expiration_alert_unit = UNSET
        else:
            expiration_alert_unit = NullString.from_dict(_expiration_alert_unit)




        def _parse_expiration_notify(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        expiration_notify = _parse_expiration_notify(d.pop("expiration_notify", UNSET))


        expiration_warning_number = d.pop("expiration_warning_number", UNSET)

        _expiration_warning_unit = d.pop("expiration_warning_unit", UNSET)
        expiration_warning_unit: NullString | Unset
        if isinstance(_expiration_warning_unit,  Unset):
            expiration_warning_unit = UNSET
        else:
            expiration_warning_unit = NullString.from_dict(_expiration_warning_unit)




        _expires_at = d.pop("expires_at", UNSET)
        expires_at: NullTime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = NullTime.from_dict(_expires_at)




        def _parse_owner_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_group_ids_type_0 = cast(list[int], data)

                return owner_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_group_ids = _parse_owner_user_group_ids(d.pop("owner_user_group_ids", UNSET))


        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))


        def _parse_sync_deprecation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sync_deprecation = _parse_sync_deprecation(d.pop("sync_deprecation", UNSET))


        def _parse_sync_tags(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sync_tags = _parse_sync_tags(d.pop("sync_tags", UNSET))


        ami_create = cls(
            account_id=account_id,
            aws_ami_id=aws_ami_id,
            name=name,
            region=region,
            description=description,
            expiration_alert_number=expiration_alert_number,
            expiration_alert_unit=expiration_alert_unit,
            expiration_notify=expiration_notify,
            expiration_warning_number=expiration_warning_number,
            expiration_warning_unit=expiration_warning_unit,
            expires_at=expires_at,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            sync_deprecation=sync_deprecation,
            sync_tags=sync_tags,
        )


        ami_create.additional_properties = d
        return ami_create

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
