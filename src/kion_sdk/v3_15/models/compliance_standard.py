from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceStandard")



@_attrs_define
class ComplianceStandard:
    """ ComplianceStandard defines a Compliance Standard.

        Attributes:
            created_at (str | Unset): Date when the Compliance Standard was added to the application. Example:
                2019-02-12T22:57:10+0000.
            created_by_user_id (int | None | Unset): CreatedByUserID refers to the User in the application who created the
                Compliance Standard Example: 1.
            ct_managed (bool | None | Unset): Will soon be deprecated! Use the system_managed field instead.
                Managed signifies that this compliance standard is managed by Kion
            description (str | Unset): Description for the Compliance Standard in the application. Example: The NIST SP
                800-53 provides a catalog of controls that support the development of secure and resilient federal information
                systems..
            id (int | Unset): ID of the compliance standard in the application. Example: 1.
            name (str | Unset): Name of the Compliance Standard in the application. Example: NIST 800-53.
            system_managed (bool | None | Unset): Managed signifies that this compliance standard is managed by Kion
     """

    created_at: str | Unset = UNSET
    created_by_user_id: int | None | Unset = UNSET
    ct_managed: bool | None | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    system_managed: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        created_by_user_id: int | None | Unset
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        ct_managed: bool | None | Unset
        if isinstance(self.ct_managed, Unset):
            ct_managed = UNSET
        else:
            ct_managed = self.ct_managed

        description = self.description

        id = self.id

        name = self.name

        system_managed: bool | None | Unset
        if isinstance(self.system_managed, Unset):
            system_managed = UNSET
        else:
            system_managed = self.system_managed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if ct_managed is not UNSET:
            field_dict["ct_managed"] = ct_managed
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if system_managed is not UNSET:
            field_dict["system_managed"] = system_managed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        def _parse_created_by_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created_by_user_id = _parse_created_by_user_id(d.pop("created_by_user_id", UNSET))


        def _parse_ct_managed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ct_managed = _parse_ct_managed(d.pop("ct_managed", UNSET))


        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_system_managed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        system_managed = _parse_system_managed(d.pop("system_managed", UNSET))


        compliance_standard = cls(
            created_at=created_at,
            created_by_user_id=created_by_user_id,
            ct_managed=ct_managed,
            description=description,
            id=id,
            name=name,
            system_managed=system_managed,
        )


        compliance_standard.additional_properties = d
        return compliance_standard

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
