from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ServiceControlPolicyUpdate")



@_attrs_define
class ServiceControlPolicyUpdate:
    """ ServiceControlPolicyUpdate defines an Service Control policy update.

        Attributes:
            description (str | Unset): Description for the Service Control policy in the application. Example: Gives user
                read only access to all AWS services..
            name (str | Unset): Name of the Service Control policy in the application. Example: ReadOnly.
            policy (str | Unset): Text of the Service Control policy in AWS to be stored in AWS.
     """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        policy = self.policy


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        policy = d.pop("policy", UNSET)

        service_control_policy_update = cls(
            description=description,
            name=name,
            policy=policy,
        )


        service_control_policy_update.additional_properties = d
        return service_control_policy_update

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
