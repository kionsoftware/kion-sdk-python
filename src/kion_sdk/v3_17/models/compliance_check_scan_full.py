from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.account import Account
  from ..models.compliance_check_scan import ComplianceCheckScan





T = TypeVar("T", bound="ComplianceCheckScanFull")



@_attrs_define
class ComplianceCheckScanFull:
    """ ComplianceCheckScanFull defines a Compliance Check Scan associated with its account

        Attributes:
            account (Account | Unset): Account defines an account.
            compliance_check_scan (ComplianceCheckScan | Unset): ComplianceCheckScan defines a Compliance Check Scan.
     """

    account: Account | Unset = UNSET
    compliance_check_scan: ComplianceCheckScan | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account import Account
        from ..models.compliance_check_scan import ComplianceCheckScan
        account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account, Unset):
            account = self.account.to_dict()

        compliance_check_scan: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compliance_check_scan, Unset):
            compliance_check_scan = self.compliance_check_scan.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account is not UNSET:
            field_dict["account"] = account
        if compliance_check_scan is not UNSET:
            field_dict["compliance_check_scan"] = compliance_check_scan

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.compliance_check_scan import ComplianceCheckScan
        d = dict(src_dict)
        _account = d.pop("account", UNSET)
        account: Account | Unset
        if isinstance(_account,  Unset):
            account = UNSET
        else:
            account = Account.from_dict(_account)




        _compliance_check_scan = d.pop("compliance_check_scan", UNSET)
        compliance_check_scan: ComplianceCheckScan | Unset
        if isinstance(_compliance_check_scan,  Unset):
            compliance_check_scan = UNSET
        else:
            compliance_check_scan = ComplianceCheckScan.from_dict(_compliance_check_scan)




        compliance_check_scan_full = cls(
            account=account,
            compliance_check_scan=compliance_check_scan,
        )


        compliance_check_scan_full.additional_properties = d
        return compliance_check_scan_full

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
