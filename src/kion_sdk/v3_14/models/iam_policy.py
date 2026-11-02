from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IAMPolicy")



@_attrs_define
class IAMPolicy:
    """ IAMPolicy defines an IAM policy.

        Attributes:
            aws_iam_path (str | Unset): Text of the IAM Path in AWS to be stored in AWS.
            aws_managed_policy (bool | None | Unset): True if the policy is created and managed by AWS
            car_restricted (bool | None | Unset): True if the policy has been restricted for use by a subset of
                Users/UGroups on a Cloud Access Role.
            description (str | Unset): Description for the IAM policy in the application. Example: Gives user read only
                access to all AWS services..
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the IAM policy in the application. Example: Read Only.
            path_suffix (str | Unset): Name of the IAM policy in AWS, as referenced in its ARN. Example: ReadOnly.
            policy (str | Unset): Text of the IAM policy in AWS to be stored in AWS.
            system_managed_policy (bool | None | Unset): True if the policy comes packaged with cloudtamer.io
     """

    aws_iam_path: str | Unset = UNSET
    aws_managed_policy: bool | None | Unset = UNSET
    car_restricted: bool | None | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    path_suffix: str | Unset = UNSET
    policy: str | Unset = UNSET
    system_managed_policy: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        aws_iam_path = self.aws_iam_path

        aws_managed_policy: bool | None | Unset
        if isinstance(self.aws_managed_policy, Unset):
            aws_managed_policy = UNSET
        else:
            aws_managed_policy = self.aws_managed_policy

        car_restricted: bool | None | Unset
        if isinstance(self.car_restricted, Unset):
            car_restricted = UNSET
        else:
            car_restricted = self.car_restricted

        description = self.description

        id = self.id

        name = self.name

        path_suffix = self.path_suffix

        policy = self.policy

        system_managed_policy: bool | None | Unset
        if isinstance(self.system_managed_policy, Unset):
            system_managed_policy = UNSET
        else:
            system_managed_policy = self.system_managed_policy


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aws_iam_path is not UNSET:
            field_dict["aws_iam_path"] = aws_iam_path
        if aws_managed_policy is not UNSET:
            field_dict["aws_managed_policy"] = aws_managed_policy
        if car_restricted is not UNSET:
            field_dict["car_restricted"] = car_restricted
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if path_suffix is not UNSET:
            field_dict["path_suffix"] = path_suffix
        if policy is not UNSET:
            field_dict["policy"] = policy
        if system_managed_policy is not UNSET:
            field_dict["system_managed_policy"] = system_managed_policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        aws_iam_path = d.pop("aws_iam_path", UNSET)

        def _parse_aws_managed_policy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aws_managed_policy = _parse_aws_managed_policy(d.pop("aws_managed_policy", UNSET))


        def _parse_car_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        car_restricted = _parse_car_restricted(d.pop("car_restricted", UNSET))


        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        path_suffix = d.pop("path_suffix", UNSET)

        policy = d.pop("policy", UNSET)

        def _parse_system_managed_policy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        system_managed_policy = _parse_system_managed_policy(d.pop("system_managed_policy", UNSET))


        iam_policy = cls(
            aws_iam_path=aws_iam_path,
            aws_managed_policy=aws_managed_policy,
            car_restricted=car_restricted,
            description=description,
            id=id,
            name=name,
            path_suffix=path_suffix,
            policy=policy,
            system_managed_policy=system_managed_policy,
        )


        iam_policy.additional_properties = d
        return iam_policy

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
