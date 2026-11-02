from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IAMPolicyUpdate")



@_attrs_define
class IAMPolicyUpdate:
    """ IAMPolicyUpdate defines an IAM policy update.

        Attributes:
            car_restricted (bool | None | Unset): True if the policy has been restricted for use by a subset of
                Users/UGroups on a Cloud Access Role.
            description (str | Unset): Description for the IAM policy in the application. Example: Gives user read only
                access to all AWS services..
            name (str | Unset): Name of the IAM policy in the application. Example: ReadOnly.
            policy (str | Unset): Text of the IAM policy in AWS to be stored in AWS.
     """

    car_restricted: bool | None | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    policy: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        car_restricted: bool | None | Unset
        if isinstance(self.car_restricted, Unset):
            car_restricted = UNSET
        else:
            car_restricted = self.car_restricted

        description = self.description

        name = self.name

        policy = self.policy


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if car_restricted is not UNSET:
            field_dict["car_restricted"] = car_restricted
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
        def _parse_car_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        car_restricted = _parse_car_restricted(d.pop("car_restricted", UNSET))


        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        policy = d.pop("policy", UNSET)

        iam_policy_update = cls(
            car_restricted=car_restricted,
            description=description,
            name=name,
            policy=policy,
        )


        iam_policy_update.additional_properties = d
        return iam_policy_update

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
