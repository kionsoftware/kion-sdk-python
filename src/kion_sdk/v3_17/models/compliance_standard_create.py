from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceStandardCreate")



@_attrs_define
class ComplianceStandardCreate:
    """ ComplianceStandardCreate defines a Compliance Standard creation.

        Attributes:
            created_by_user_id (int | None): CreatedByUserID refers to the User in the application who created the
                Compliance Standard Example: 1.
            name (str): Name of the Compliance Standard in the application. Example: NIST 800-53.
            cloud_rule_id (int | None | Unset): Cloud Rule ID the Compliance Standard should be added to Example: 1.
            compliance_check_ids (list[int] | None | Unset): List of compliance checks associated with the compliance
                standard Example: [1, 2].
            description (str | Unset): Description for the Compliance Standard in the application. Example: The NIST SP
                800-53 provides a catalog of controls that support the development of secure and resilient federal information
                systems..
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the Compliance Standard. Is
                required if no owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the Compliance Standard. Is required if
                no owner group IDs are listed. Example: [1, 2].
     """

    created_by_user_id: int | None
    name: str
    cloud_rule_id: int | None | Unset = UNSET
    compliance_check_ids: list[int] | None | Unset = UNSET
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_by_user_id: int | None
        created_by_user_id = self.created_by_user_id

        name = self.name

        cloud_rule_id: int | None | Unset
        if isinstance(self.cloud_rule_id, Unset):
            cloud_rule_id = UNSET
        else:
            cloud_rule_id = self.cloud_rule_id

        compliance_check_ids: list[int] | None | Unset
        if isinstance(self.compliance_check_ids, Unset):
            compliance_check_ids = UNSET
        elif isinstance(self.compliance_check_ids, list):
            compliance_check_ids = self.compliance_check_ids


        else:
            compliance_check_ids = self.compliance_check_ids

        description = self.description

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "created_by_user_id": created_by_user_id,
            "name": name,
        })
        if cloud_rule_id is not UNSET:
            field_dict["cloud_rule_id"] = cloud_rule_id
        if compliance_check_ids is not UNSET:
            field_dict["compliance_check_ids"] = compliance_check_ids
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_created_by_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        created_by_user_id = _parse_created_by_user_id(d.pop("created_by_user_id"))


        name = d.pop("name")

        def _parse_cloud_rule_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_rule_id = _parse_cloud_rule_id(d.pop("cloud_rule_id", UNSET))


        def _parse_compliance_check_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_check_ids_type_0 = cast(list[int], data)

                return compliance_check_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        compliance_check_ids = _parse_compliance_check_ids(d.pop("compliance_check_ids", UNSET))


        description = d.pop("description", UNSET)

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


        compliance_standard_create = cls(
            created_by_user_id=created_by_user_id,
            name=name,
            cloud_rule_id=cloud_rule_id,
            compliance_check_ids=compliance_check_ids,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
        )


        compliance_standard_create.additional_properties = d
        return compliance_standard_create

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
