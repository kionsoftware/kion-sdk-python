from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AzurePolicyDefinition")



@_attrs_define
class AzurePolicyDefinition:
    """ AzurePolicyDefinition represents an Azure Policy Definition, complete with the policy itself and its parameters.

        Attributes:
            azure_managed_policy_def_id (str | Unset): ID of the policy in Azure if this policy definition is managed by
                Azure. Example: 0004bbf0-5099-4179-869e-e9ffe5fb0945.
            ct_managed (bool | None | Unset): Managed signifies that this policy definition is managed by cloudtamer.io
            description (str | Unset): The human-readable description of the policy Example: My description.
            enabled (bool | None | Unset): Indicates that the policy is currently applied to an account Example: True.
            id (int | Unset): Unique identifier for the Azure Policy Definition Example: 1.
            name (str | Unset): Human-readable name of the Azure Policy Definition Example: MyPolicy.
            parameters (str | Unset): The parameters for the policy Example: {}.
            policy (str | Unset): The JSON for the policy Example: {}.
     """

    azure_managed_policy_def_id: str | Unset = UNSET
    ct_managed: bool | None | Unset = UNSET
    description: str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    parameters: str | Unset = UNSET
    policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        azure_managed_policy_def_id = self.azure_managed_policy_def_id

        ct_managed: bool | None | Unset
        if isinstance(self.ct_managed, Unset):
            ct_managed = UNSET
        else:
            ct_managed = self.ct_managed

        description = self.description

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        id = self.id

        name = self.name

        parameters = self.parameters

        policy = self.policy


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if azure_managed_policy_def_id is not UNSET:
            field_dict["azure_managed_policy_def_id"] = azure_managed_policy_def_id
        if ct_managed is not UNSET:
            field_dict["ct_managed"] = ct_managed
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        azure_managed_policy_def_id = d.pop("azure_managed_policy_def_id", UNSET)

        def _parse_ct_managed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ct_managed = _parse_ct_managed(d.pop("ct_managed", UNSET))


        description = d.pop("description", UNSET)

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        parameters = d.pop("parameters", UNSET)

        policy = d.pop("policy", UNSET)

        azure_policy_definition = cls(
            azure_managed_policy_def_id=azure_managed_policy_def_id,
            ct_managed=ct_managed,
            description=description,
            enabled=enabled,
            id=id,
            name=name,
            parameters=parameters,
            policy=policy,
        )


        azure_policy_definition.additional_properties = d
        return azure_policy_definition

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
