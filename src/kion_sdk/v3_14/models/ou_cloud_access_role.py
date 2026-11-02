from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OUCloudAccessRole")



@_attrs_define
class OUCloudAccessRole:
    """ OUCloudAccessRole defines a cloud access role for an ou.

        Attributes:
            aws_iam_path (str | Unset): Text of the IAM Path in AWS to be stored in AWS. Example: /iam-path/.
            aws_iam_role_name (str | Unset): AWS IAM role name corresponding to the cloud access role. Example: read-only.
            id (int | Unset): ID of the record in the application. Example: 1.
            long_term_access_keys (bool | None | Unset): If long term key access is true, users of this cloud access role
                can generate aws long-term access keys. Example: True.
            name (str | Unset): Name of the cloud access role in the application. Example: Read Only.
            ou_id (int | None | Unset): ID of the ou where the cloud access role is defined. Example: 1.
            short_term_access_keys (bool | None | Unset): If short term key access is true, users of this cloud access role
                can generate short-term access keys. Example: True.
            web_access (bool | None | Unset): If web access is true, users of this cloud access role can log into the
                console Example: True.
     """

    aws_iam_path: str | Unset = UNSET
    aws_iam_role_name: str | Unset = UNSET
    id: int | Unset = UNSET
    long_term_access_keys: bool | None | Unset = UNSET
    name: str | Unset = UNSET
    ou_id: int | None | Unset = UNSET
    short_term_access_keys: bool | None | Unset = UNSET
    web_access: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        aws_iam_path = self.aws_iam_path

        aws_iam_role_name = self.aws_iam_role_name

        id = self.id

        long_term_access_keys: bool | None | Unset
        if isinstance(self.long_term_access_keys, Unset):
            long_term_access_keys = UNSET
        else:
            long_term_access_keys = self.long_term_access_keys

        name = self.name

        ou_id: int | None | Unset
        if isinstance(self.ou_id, Unset):
            ou_id = UNSET
        else:
            ou_id = self.ou_id

        short_term_access_keys: bool | None | Unset
        if isinstance(self.short_term_access_keys, Unset):
            short_term_access_keys = UNSET
        else:
            short_term_access_keys = self.short_term_access_keys

        web_access: bool | None | Unset
        if isinstance(self.web_access, Unset):
            web_access = UNSET
        else:
            web_access = self.web_access


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aws_iam_path is not UNSET:
            field_dict["aws_iam_path"] = aws_iam_path
        if aws_iam_role_name is not UNSET:
            field_dict["aws_iam_role_name"] = aws_iam_role_name
        if id is not UNSET:
            field_dict["id"] = id
        if long_term_access_keys is not UNSET:
            field_dict["long_term_access_keys"] = long_term_access_keys
        if name is not UNSET:
            field_dict["name"] = name
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id
        if short_term_access_keys is not UNSET:
            field_dict["short_term_access_keys"] = short_term_access_keys
        if web_access is not UNSET:
            field_dict["web_access"] = web_access

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aws_iam_path = d.pop("aws_iam_path", UNSET)

        aws_iam_role_name = d.pop("aws_iam_role_name", UNSET)

        id = d.pop("id", UNSET)

        def _parse_long_term_access_keys(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        long_term_access_keys = _parse_long_term_access_keys(d.pop("long_term_access_keys", UNSET))


        name = d.pop("name", UNSET)

        def _parse_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_id = _parse_ou_id(d.pop("ou_id", UNSET))


        def _parse_short_term_access_keys(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        short_term_access_keys = _parse_short_term_access_keys(d.pop("short_term_access_keys", UNSET))


        def _parse_web_access(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        web_access = _parse_web_access(d.pop("web_access", UNSET))


        ou_cloud_access_role = cls(
            aws_iam_path=aws_iam_path,
            aws_iam_role_name=aws_iam_role_name,
            id=id,
            long_term_access_keys=long_term_access_keys,
            name=name,
            ou_id=ou_id,
            short_term_access_keys=short_term_access_keys,
            web_access=web_access,
        )


        ou_cloud_access_role.additional_properties = d
        return ou_cloud_access_role

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
