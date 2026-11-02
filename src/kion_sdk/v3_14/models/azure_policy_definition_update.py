from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AzurePolicyDefinitionUpdate")



@_attrs_define
class AzurePolicyDefinitionUpdate:
    """ AzurePolicyDefinitionUpdate represents an update Azure Policy Definition, complete with the policy itself and its
    parameters.

        Attributes:
            description (str | Unset): The human-readable description of the policy Example: My description.
            name (str | Unset): Human-readable name of the Azure Policy Definition Example: MyPolicy.
            parameters (str | Unset): The parameters for the policy Example: {}.
            policy (str | Unset): The JSON for the policy Example: {}.
     """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    parameters: str | Unset = UNSET
    policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        parameters = self.parameters

        policy = self.policy


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
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
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        parameters = d.pop("parameters", UNSET)

        policy = d.pop("policy", UNSET)

        azure_policy_definition_update = cls(
            description=description,
            name=name,
            parameters=parameters,
            policy=policy,
        )


        azure_policy_definition_update.additional_properties = d
        return azure_policy_definition_update

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
