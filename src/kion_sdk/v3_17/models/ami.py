from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.null_time import NullTime





T = TypeVar("T", bound="AMI")



@_attrs_define
class AMI:
    """ AMI defines an AMI in an account managed by cloudtamer.io.

        Attributes:
            account_id (int | None | Unset): AWS account application ID where the AMI is stored. Example: 1.
            aws_ami_id (str | Unset): Image ID of the AMI from AWS. Example: ami-123456.
            description (str | Unset): Description for the AMI in the application. Example: Gold image for RHEL 7.5..
            expires_at (NullTime | Unset): NullTime represents a time.Time that may be NULL.
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the AMI in the application. Example: rhel-7-5-20180213.
            region (str | Unset): AWS region where the AMI exists. Example: us-east-1.
            sync_deprecation (bool | None | Unset): Will sync the expiration date from the system into the AMI in AWS.
                Example: True.
            sync_tags (bool | None | Unset): Will sync the AWS tags from the source AMI into all the accounts where the AMI
                is shared. Example: True.
            unavailable_in_aws (bool | None | Unset): Will be true if the AMI is no longer available in AWS and should be
                cleaned up in cloudtamer.io
     """

    account_id: int | None | Unset = UNSET
    aws_ami_id: str | Unset = UNSET
    description: str | Unset = UNSET
    expires_at: NullTime | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    region: str | Unset = UNSET
    sync_deprecation: bool | None | Unset = UNSET
    sync_tags: bool | None | Unset = UNSET
    unavailable_in_aws: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.null_time import NullTime
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        aws_ami_id = self.aws_ami_id

        description = self.description

        expires_at: dict[str, Any] | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.to_dict()

        id = self.id

        name = self.name

        region = self.region

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

        unavailable_in_aws: bool | None | Unset
        if isinstance(self.unavailable_in_aws, Unset):
            unavailable_in_aws = UNSET
        else:
            unavailable_in_aws = self.unavailable_in_aws


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if aws_ami_id is not UNSET:
            field_dict["aws_ami_id"] = aws_ami_id
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if sync_deprecation is not UNSET:
            field_dict["sync_deprecation"] = sync_deprecation
        if sync_tags is not UNSET:
            field_dict["sync_tags"] = sync_tags
        if unavailable_in_aws is not UNSET:
            field_dict["unavailable_in_aws"] = unavailable_in_aws

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.null_time import NullTime
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        aws_ami_id = d.pop("aws_ami_id", UNSET)

        description = d.pop("description", UNSET)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: NullTime | Unset
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = NullTime.from_dict(_expires_at)




        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

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


        def _parse_unavailable_in_aws(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        unavailable_in_aws = _parse_unavailable_in_aws(d.pop("unavailable_in_aws", UNSET))


        ami = cls(
            account_id=account_id,
            aws_ami_id=aws_ami_id,
            description=description,
            expires_at=expires_at,
            id=id,
            name=name,
            region=region,
            sync_deprecation=sync_deprecation,
            sync_tags=sync_tags,
            unavailable_in_aws=unavailable_in_aws,
        )


        ami.additional_properties = d
        return ami

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
