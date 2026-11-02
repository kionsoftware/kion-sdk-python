from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AzurePolicyDefinitionCreate")



@_attrs_define
class AzurePolicyDefinitionCreate:
    """ AzurePolicyDefinitionCreate represents an create Azure Policy Definition, complete with the policy itself and its
    parameters.

        Attributes:
            name (str): Human-readable name of the Azure Policy Definition Example: MyPolicy.
            policy (str): The JSON for the policy Example: {}.
            description (str | Unset): The human-readable description of the policy Example: My description.
            parameters (str | Unset): The parameters for the policy Example: {}.
     """

    name: str
    policy: str
    description: str | Unset = UNSET
    parameters: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        policy = self.policy

        description = self.description

        parameters = self.parameters


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "policy": policy,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        policy = d.pop("policy")

        description = d.pop("description", UNSET)

        parameters = d.pop("parameters", UNSET)

        azure_policy_definition_create = cls(
            name=name,
            policy=policy,
            description=description,
            parameters=parameters,
        )


        azure_policy_definition_create.additional_properties = d
        return azure_policy_definition_create

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
