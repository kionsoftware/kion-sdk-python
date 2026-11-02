from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ComplianceCheckSuppressedFindingCreate")



@_attrs_define
class ComplianceCheckSuppressedFindingCreate:
    """ ComplianceCheckSuppressedFindingCreate defines a Compliance Check Suppressed Finding Create.

        Attributes:
            reason (str | Unset): Reason describes the purpose of the finding suppression. Example: 1.
            suppression_timeout (int | Unset): Defines the amount of time the finding will be suppressed. Example: 7.
            suppression_timeout_unit_id (int | None | Unset): The unit of time (frequency-type) the suppression_timeout is
                in Example: 4.
     """

    reason: str | Unset = UNSET
    suppression_timeout: int | Unset = UNSET
    suppression_timeout_unit_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        suppression_timeout = self.suppression_timeout

        suppression_timeout_unit_id: int | None | Unset
        if isinstance(self.suppression_timeout_unit_id, Unset):
            suppression_timeout_unit_id = UNSET
        else:
            suppression_timeout_unit_id = self.suppression_timeout_unit_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if suppression_timeout is not UNSET:
            field_dict["suppression_timeout"] = suppression_timeout
        if suppression_timeout_unit_id is not UNSET:
            field_dict["suppression_timeout_unit_id"] = suppression_timeout_unit_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason", UNSET)

        suppression_timeout = d.pop("suppression_timeout", UNSET)

        def _parse_suppression_timeout_unit_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        suppression_timeout_unit_id = _parse_suppression_timeout_unit_id(d.pop("suppression_timeout_unit_id", UNSET))


        compliance_check_suppressed_finding_create = cls(
            reason=reason,
            suppression_timeout=suppression_timeout,
            suppression_timeout_unit_id=suppression_timeout_unit_id,
        )


        compliance_check_suppressed_finding_create.additional_properties = d
        return compliance_check_suppressed_finding_create

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
