from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ServiceControlPolicy")



@_attrs_define
class ServiceControlPolicy:
    """ ServiceControlPolicy defines an Service Control policy.

        Attributes:
            aws_managed_policy (bool | None | Unset): True if the policy is created and managed by AWS
            created_by_user_id (int | None | Unset): CreatedByUserID refers to the User in the application who created the
                service control policy Example: 1.
            description (str | Unset): Description for the Service Control policy in the application. Example: Gives user
                read only access to all AWS services..
            id (int | Unset): ID of the record in the application. Example: 1.
            name (str | Unset): Name of the Service Control policy in the application. Example: ReadOnly.
            policy (str | Unset): Text of the Service Control policy in AWS to be stored in AWS.
            system_managed_policy (bool | None | Unset): True if the policy comes packaged with cloudtamer.io
     """

    aws_managed_policy: bool | None | Unset = UNSET
    created_by_user_id: int | None | Unset = UNSET
    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    policy: str | Unset = UNSET
    system_managed_policy: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        aws_managed_policy: bool | None | Unset
        if isinstance(self.aws_managed_policy, Unset):
            aws_managed_policy = UNSET
        else:
            aws_managed_policy = self.aws_managed_policy

        created_by_user_id: int | None | Unset
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        description = self.description

        id = self.id

        name = self.name

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
        if aws_managed_policy is not UNSET:
            field_dict["aws_managed_policy"] = aws_managed_policy
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if policy is not UNSET:
            field_dict["policy"] = policy
        if system_managed_policy is not UNSET:
            field_dict["system_managed_policy"] = system_managed_policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_aws_managed_policy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        aws_managed_policy = _parse_aws_managed_policy(d.pop("aws_managed_policy", UNSET))


        def _parse_created_by_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        created_by_user_id = _parse_created_by_user_id(d.pop("created_by_user_id", UNSET))


        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        policy = d.pop("policy", UNSET)

        def _parse_system_managed_policy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        system_managed_policy = _parse_system_managed_policy(d.pop("system_managed_policy", UNSET))


        service_control_policy = cls(
            aws_managed_policy=aws_managed_policy,
            created_by_user_id=created_by_user_id,
            description=description,
            id=id,
            name=name,
            policy=policy,
            system_managed_policy=system_managed_policy,
        )


        service_control_policy.additional_properties = d
        return service_control_policy

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
