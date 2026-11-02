from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OUCloudAccessRoleExemption")



@_attrs_define
class OUCloudAccessRoleExemption:
    """ OUCloudAccessRoleExemption defines an exemption of an ou cloud access role for an ou.

        Attributes:
            id (int | Unset): ID of the record in the application. Example: 1.
            ou_cloud_access_role_id (int | None | Unset): ID of the ou cloud access role in the application being exempted
                from. Example: 107.
            ou_id (int | None | Unset): ID of the ou in the application. Example: 104.
            reason (str | Unset): Reason the Cloud Access Role is being exempted. Example: This CAR isn't used in this OU.
     """

    id: int | Unset = UNSET
    ou_cloud_access_role_id: int | None | Unset = UNSET
    ou_id: int | None | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        ou_cloud_access_role_id: int | None | Unset
        if isinstance(self.ou_cloud_access_role_id, Unset):
            ou_cloud_access_role_id = UNSET
        else:
            ou_cloud_access_role_id = self.ou_cloud_access_role_id

        ou_id: int | None | Unset
        if isinstance(self.ou_id, Unset):
            ou_id = UNSET
        else:
            ou_id = self.ou_id

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if ou_cloud_access_role_id is not UNSET:
            field_dict["ou_cloud_access_role_id"] = ou_cloud_access_role_id
        if ou_id is not UNSET:
            field_dict["ou_id"] = ou_id
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_ou_cloud_access_role_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_cloud_access_role_id = _parse_ou_cloud_access_role_id(d.pop("ou_cloud_access_role_id", UNSET))


        def _parse_ou_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ou_id = _parse_ou_id(d.pop("ou_id", UNSET))


        reason = d.pop("reason", UNSET)

        ou_cloud_access_role_exemption = cls(
            id=id,
            ou_cloud_access_role_id=ou_cloud_access_role_id,
            ou_id=ou_id,
            reason=reason,
        )


        ou_cloud_access_role_exemption.additional_properties = d
        return ou_cloud_access_role_exemption

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
