from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.compliance_check import ComplianceCheck
  from ..models.compliance_standard import ComplianceStandard
  from ..models.u_group import UGroup
  from ..models.user import User





T = TypeVar("T", bound="ComplianceStandardFull")



@_attrs_define
class ComplianceStandardFull:
    """ ComplianceStandardFull defines a Compliance Standard and checks.

        Attributes:
            compliance_checks (list[ComplianceCheck] | None | Unset): List of Compliance Checks attached to the Compliance
                Standard
            compliance_standard (ComplianceStandard | Unset): ComplianceStandard defines a Compliance Standard.
            owner_user_groups (list[UGroup] | None | Unset): List of groups that own the Compliance Standard.
            owner_users (list[User] | None | Unset): List of users that own the Compliance Standard.
     """

    compliance_checks: list[ComplianceCheck] | None | Unset = UNSET
    compliance_standard: ComplianceStandard | Unset = UNSET
    owner_user_groups: list[UGroup] | None | Unset = UNSET
    owner_users: list[User] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.compliance_check import ComplianceCheck
        from ..models.compliance_standard import ComplianceStandard
        from ..models.u_group import UGroup
        from ..models.user import User
        compliance_checks: list[dict[str, Any]] | None | Unset
        if isinstance(self.compliance_checks, Unset):
            compliance_checks = UNSET
        elif isinstance(self.compliance_checks, list):
            compliance_checks = []
            for compliance_checks_type_0_item_data in self.compliance_checks:
                compliance_checks_type_0_item = compliance_checks_type_0_item_data.to_dict()
                compliance_checks.append(compliance_checks_type_0_item)


        else:
            compliance_checks = self.compliance_checks

        compliance_standard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compliance_standard, Unset):
            compliance_standard = self.compliance_standard.to_dict()

        owner_user_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_user_groups, Unset):
            owner_user_groups = UNSET
        elif isinstance(self.owner_user_groups, list):
            owner_user_groups = []
            for owner_user_groups_type_0_item_data in self.owner_user_groups:
                owner_user_groups_type_0_item = owner_user_groups_type_0_item_data.to_dict()
                owner_user_groups.append(owner_user_groups_type_0_item)


        else:
            owner_user_groups = self.owner_user_groups

        owner_users: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_users, Unset):
            owner_users = UNSET
        elif isinstance(self.owner_users, list):
            owner_users = []
            for owner_users_type_0_item_data in self.owner_users:
                owner_users_type_0_item = owner_users_type_0_item_data.to_dict()
                owner_users.append(owner_users_type_0_item)


        else:
            owner_users = self.owner_users


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if compliance_checks is not UNSET:
            field_dict["compliance_checks"] = compliance_checks
        if compliance_standard is not UNSET:
            field_dict["compliance_standard"] = compliance_standard
        if owner_user_groups is not UNSET:
            field_dict["owner_user_groups"] = owner_user_groups
        if owner_users is not UNSET:
            field_dict["owner_users"] = owner_users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compliance_check import ComplianceCheck
        from ..models.compliance_standard import ComplianceStandard
        from ..models.u_group import UGroup
        from ..models.user import User
        d = dict(src_dict)
        def _parse_compliance_checks(data: object) -> list[ComplianceCheck] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_checks_type_0 = []
                _compliance_checks_type_0 = data
                for compliance_checks_type_0_item_data in (_compliance_checks_type_0):
                    compliance_checks_type_0_item = ComplianceCheck.from_dict(compliance_checks_type_0_item_data)



                    compliance_checks_type_0.append(compliance_checks_type_0_item)

                return compliance_checks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceCheck] | None | Unset, data)

        compliance_checks = _parse_compliance_checks(d.pop("compliance_checks", UNSET))


        _compliance_standard = d.pop("compliance_standard", UNSET)
        compliance_standard: ComplianceStandard | Unset
        if isinstance(_compliance_standard,  Unset):
            compliance_standard = UNSET
        else:
            compliance_standard = ComplianceStandard.from_dict(_compliance_standard)




        def _parse_owner_user_groups(data: object) -> list[UGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_groups_type_0 = []
                _owner_user_groups_type_0 = data
                for owner_user_groups_type_0_item_data in (_owner_user_groups_type_0):
                    owner_user_groups_type_0_item = UGroup.from_dict(owner_user_groups_type_0_item_data)



                    owner_user_groups_type_0.append(owner_user_groups_type_0_item)

                return owner_user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroup] | None | Unset, data)

        owner_user_groups = _parse_owner_user_groups(d.pop("owner_user_groups", UNSET))


        def _parse_owner_users(data: object) -> list[User] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_users_type_0 = []
                _owner_users_type_0 = data
                for owner_users_type_0_item_data in (_owner_users_type_0):
                    owner_users_type_0_item = User.from_dict(owner_users_type_0_item_data)



                    owner_users_type_0.append(owner_users_type_0_item)

                return owner_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[User] | None | Unset, data)

        owner_users = _parse_owner_users(d.pop("owner_users", UNSET))


        compliance_standard_full = cls(
            compliance_checks=compliance_checks,
            compliance_standard=compliance_standard,
            owner_user_groups=owner_user_groups,
            owner_users=owner_users,
        )


        compliance_standard_full.additional_properties = d
        return compliance_standard_full

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
