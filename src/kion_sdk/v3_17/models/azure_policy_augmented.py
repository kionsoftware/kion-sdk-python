from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.azure_policy_definition import AzurePolicyDefinition
  from ..models.compliance_program_status import ComplianceProgramStatus
  from ..models.u_group import UGroup
  from ..models.user import User





T = TypeVar("T", bound="AzurePolicyAugmented")



@_attrs_define
class AzurePolicyAugmented:
    """ AzurePolicyAugmented defines an Azure Policy with owners and compliance programs.

        Attributes:
            azure_policy (AzurePolicyDefinition | Unset): AzurePolicyDefinition represents an Azure Policy Definition,
                complete with the policy itself and its parameters.
            compliance_programs (list[ComplianceProgramStatus] | None | Unset): List of compliance program IDs with which
                the azure policy is associated.
            owner_user_groups (list[UGroup] | None | Unset): List of user group IDs that will be owners of the azure policy.
            owner_users (list[User] | None | Unset): List of user IDs that will be owners of the azure policy.
     """

    azure_policy: AzurePolicyDefinition | Unset = UNSET
    compliance_programs: list[ComplianceProgramStatus] | None | Unset = UNSET
    owner_user_groups: list[UGroup] | None | Unset = UNSET
    owner_users: list[User] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.azure_policy_definition import AzurePolicyDefinition
        from ..models.compliance_program_status import ComplianceProgramStatus
        from ..models.u_group import UGroup
        from ..models.user import User
        azure_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_policy, Unset):
            azure_policy = self.azure_policy.to_dict()

        compliance_programs: list[dict[str, Any]] | None | Unset
        if isinstance(self.compliance_programs, Unset):
            compliance_programs = UNSET
        elif isinstance(self.compliance_programs, list):
            compliance_programs = []
            for compliance_programs_type_0_item_data in self.compliance_programs:
                compliance_programs_type_0_item = compliance_programs_type_0_item_data.to_dict()
                compliance_programs.append(compliance_programs_type_0_item)


        else:
            compliance_programs = self.compliance_programs

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
        if azure_policy is not UNSET:
            field_dict["azure_policy"] = azure_policy
        if compliance_programs is not UNSET:
            field_dict["compliance_programs"] = compliance_programs
        if owner_user_groups is not UNSET:
            field_dict["owner_user_groups"] = owner_user_groups
        if owner_users is not UNSET:
            field_dict["owner_users"] = owner_users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_policy_definition import AzurePolicyDefinition
        from ..models.compliance_program_status import ComplianceProgramStatus
        from ..models.u_group import UGroup
        from ..models.user import User
        d = dict(src_dict)
        _azure_policy = d.pop("azure_policy", UNSET)
        azure_policy: AzurePolicyDefinition | Unset
        if isinstance(_azure_policy,  Unset):
            azure_policy = UNSET
        else:
            azure_policy = AzurePolicyDefinition.from_dict(_azure_policy)




        def _parse_compliance_programs(data: object) -> list[ComplianceProgramStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                compliance_programs_type_0 = []
                _compliance_programs_type_0 = data
                for compliance_programs_type_0_item_data in (_compliance_programs_type_0):
                    compliance_programs_type_0_item = ComplianceProgramStatus.from_dict(compliance_programs_type_0_item_data)



                    compliance_programs_type_0.append(compliance_programs_type_0_item)

                return compliance_programs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ComplianceProgramStatus] | None | Unset, data)

        compliance_programs = _parse_compliance_programs(d.pop("compliance_programs", UNSET))


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


        azure_policy_augmented = cls(
            azure_policy=azure_policy,
            compliance_programs=compliance_programs,
            owner_user_groups=owner_user_groups,
            owner_users=owner_users,
        )


        azure_policy_augmented.additional_properties = d
        return azure_policy_augmented

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
