from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceStandardAssociations")



@_attrs_define
class ComplianceStandardAssociations:
    """ ComplianceStandardAssociations defines a Compliance Standard association update.

        Attributes:
            compliance_check_ids (list[int] | None | Unset): List of Compliance Checks where the Standard is applied
                Example: [1].
     """

    compliance_check_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        compliance_check_ids: list[int] | None | Unset
        if isinstance(self.compliance_check_ids, Unset):
            compliance_check_ids = UNSET
        elif isinstance(self.compliance_check_ids, list):
            compliance_check_ids = self.compliance_check_ids


        else:
            compliance_check_ids = self.compliance_check_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if compliance_check_ids is not UNSET:
            field_dict["compliance_check_ids"] = compliance_check_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        compliance_standard_associations = cls(
            compliance_check_ids=compliance_check_ids,
        )


        compliance_standard_associations.additional_properties = d
        return compliance_standard_associations

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
