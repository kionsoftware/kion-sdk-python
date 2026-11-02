from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_check_state_account_with_regions import ComplianceCheckStateAccountWithRegions





T = TypeVar("T", bound="ComplianceCheckState")



@_attrs_define
class ComplianceCheckState:
    """ ComplianceCheckState defines a Compliance Check State.

        Attributes:
            account_with_regions (ComplianceCheckStateAccountWithRegions | Unset): AccountWithRegions stores mapping of
                unique accounts with regions.
            compliance_check_failure_count (int | Unset): ComplianceCheckFailureCount for the number of failures on a
                Compliance Check in the application. Example: 1.
            compliance_check_id (int | None | Unset): ID of the compliance check in the application. Example: 1.
     """

    account_with_regions: ComplianceCheckStateAccountWithRegions | Unset = UNSET
    compliance_check_failure_count: int | Unset = UNSET
    compliance_check_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_check_state_account_with_regions import ComplianceCheckStateAccountWithRegions
        account_with_regions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_with_regions, Unset):
            account_with_regions = self.account_with_regions.to_dict()

        compliance_check_failure_count = self.compliance_check_failure_count

        compliance_check_id: int | None | Unset
        if isinstance(self.compliance_check_id, Unset):
            compliance_check_id = UNSET
        else:
            compliance_check_id = self.compliance_check_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_with_regions is not UNSET:
            field_dict["account_with_regions"] = account_with_regions
        if compliance_check_failure_count is not UNSET:
            field_dict["compliance_check_failure_count"] = compliance_check_failure_count
        if compliance_check_id is not UNSET:
            field_dict["compliance_check_id"] = compliance_check_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_check_state_account_with_regions import ComplianceCheckStateAccountWithRegions
        d = dict(src_dict)
        _account_with_regions = d.pop("account_with_regions", UNSET)
        account_with_regions: ComplianceCheckStateAccountWithRegions | Unset
        if isinstance(_account_with_regions,  Unset):
            account_with_regions = UNSET
        else:
            account_with_regions = ComplianceCheckStateAccountWithRegions.from_dict(_account_with_regions)




        compliance_check_failure_count = d.pop("compliance_check_failure_count", UNSET)

        def _parse_compliance_check_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        compliance_check_id = _parse_compliance_check_id(d.pop("compliance_check_id", UNSET))


        compliance_check_state = cls(
            account_with_regions=account_with_regions,
            compliance_check_failure_count=compliance_check_failure_count,
            compliance_check_id=compliance_check_id,
        )


        compliance_check_state.additional_properties = d
        return compliance_check_state

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
