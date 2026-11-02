from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AWSSessionTag")



@_attrs_define
class AWSSessionTag:
    """ AWSSessionTag defines an AWSSessionTag in an account managed by cloudtamer.io.

        Attributes:
            cloud_access_role_id (int | None | Unset): Cloud Access Role ID that the session tag is attached to.
                Can only be attached to either a Cloud Access Role ID or an OU Cloud Access Role ID. Example: 1.
            id (int | Unset): ID of the record in the application. Example: 1.
            ou_cloud_access_role_id (int | None | Unset): OU Cloud Access Role ID that the session tag is attached to.
                Can only be attached to either a Cloud Access Role ID or an OU Cloud Access Role ID. Example: 1.
            tag_key (str | Unset): Key of the session tag. Example: department.
            tag_value (str | Unset): Value of the session tag. Example: engineering.
     """

    cloud_access_role_id: int | None | Unset = UNSET
    id: int | Unset = UNSET
    ou_cloud_access_role_id: int | None | Unset = UNSET
    tag_key: str | Unset = UNSET
    tag_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cloud_access_role_id: int | None | Unset
        if isinstance(self.cloud_access_role_id, Unset):
            cloud_access_role_id = UNSET
        else:
            cloud_access_role_id = self.cloud_access_role_id

        id = self.id

        ou_cloud_access_role_id: int | None | Unset
        if isinstance(self.ou_cloud_access_role_id, Unset):
            ou_cloud_access_role_id = UNSET
        else:
            ou_cloud_access_role_id = self.ou_cloud_access_role_id

        tag_key = self.tag_key

        tag_value = self.tag_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cloud_access_role_id is not UNSET:
            field_dict["cloud_access_role_id"] = cloud_access_role_id
        if id is not UNSET:
            field_dict["id"] = id
        if ou_cloud_access_role_id is not UNSET:
            field_dict["ou_cloud_access_role_id"] = ou_cloud_access_role_id
        if tag_key is not UNSET:
            field_dict["tag_key"] = tag_key
        if tag_value is not UNSET:
            field_dict["tag_value"] = tag_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cloud_access_role_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_access_role_id = _parse_cloud_access_role_id(d.pop("cloud_access_role_id", UNSET))


        id = d.pop("id", UNSET)

        def _parse_ou_cloud_access_role_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_cloud_access_role_id = _parse_ou_cloud_access_role_id(d.pop("ou_cloud_access_role_id", UNSET))


        tag_key = d.pop("tag_key", UNSET)

        tag_value = d.pop("tag_value", UNSET)

        aws_session_tag = cls(
            cloud_access_role_id=cloud_access_role_id,
            id=id,
            ou_cloud_access_role_id=ou_cloud_access_role_id,
            tag_key=tag_key,
            tag_value=tag_value,
        )


        aws_session_tag.additional_properties = d
        return aws_session_tag

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
