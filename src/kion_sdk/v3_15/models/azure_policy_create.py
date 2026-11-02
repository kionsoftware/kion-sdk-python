from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.azure_policy_definition_create import AzurePolicyDefinitionCreate





T = TypeVar("T", bound="AzurePolicyCreate")



@_attrs_define
class AzurePolicyCreate:
    """ AzurePolicyCreate defines an Azure Policy create object with owners.

        Attributes:
            azure_policy (AzurePolicyDefinitionCreate | Unset): AzurePolicyDefinitionCreate represents an create Azure
                Policy Definition, complete with the policy itself and its parameters.
            owner_user_groups (list[int] | None | Unset): List of user group IDs that will be owners of the azure policy.
                Example: [1].
            owner_users (list[int] | None | Unset): List of user IDs that will be owners of the azure policy. Example: [1].
     """

    azure_policy: AzurePolicyDefinitionCreate | Unset = UNSET
    owner_user_groups: list[int] | None | Unset = UNSET
    owner_users: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.azure_policy_definition_create import AzurePolicyDefinitionCreate
        azure_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_policy, Unset):
            azure_policy = self.azure_policy.to_dict()

        owner_user_groups: list[int] | None | Unset
        if isinstance(self.owner_user_groups, Unset):
            owner_user_groups = UNSET
        elif isinstance(self.owner_user_groups, list):
            owner_user_groups = self.owner_user_groups


        else:
            owner_user_groups = self.owner_user_groups

        owner_users: list[int] | None | Unset
        if isinstance(self.owner_users, Unset):
            owner_users = UNSET
        elif isinstance(self.owner_users, list):
            owner_users = self.owner_users


        else:
            owner_users = self.owner_users


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if azure_policy is not UNSET:
            field_dict["azure_policy"] = azure_policy
        if owner_user_groups is not UNSET:
            field_dict["owner_user_groups"] = owner_user_groups
        if owner_users is not UNSET:
            field_dict["owner_users"] = owner_users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.azure_policy_definition_create import AzurePolicyDefinitionCreate
        d = dict(src_dict)
        _azure_policy = d.pop("azure_policy", UNSET)
        azure_policy: AzurePolicyDefinitionCreate | Unset
        if isinstance(_azure_policy,  Unset):
            azure_policy = UNSET
        else:
            azure_policy = AzurePolicyDefinitionCreate.from_dict(_azure_policy)




        def _parse_owner_user_groups(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_groups_type_0 = cast(list[int], data)

                return owner_user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_groups = _parse_owner_user_groups(d.pop("owner_user_groups", UNSET))


        def _parse_owner_users(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_users_type_0 = cast(list[int], data)

                return owner_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_users = _parse_owner_users(d.pop("owner_users", UNSET))


        azure_policy_create = cls(
            azure_policy=azure_policy,
            owner_user_groups=owner_user_groups,
            owner_users=owner_users,
        )


        azure_policy_create.additional_properties = d
        return azure_policy_create

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
