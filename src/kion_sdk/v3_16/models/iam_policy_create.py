from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="IAMPolicyCreate")



@_attrs_define
class IAMPolicyCreate:
    """ IAMPolicyCreate defines an IAM policy creation.

        Attributes:
            name (str): Name of the IAM policy in the application. Example: ReadOnly.
            policy (str): Text of the IAM policy in AWS to be stored in AWS.
            aws_iam_path (str | Unset): Text of the IAM Path in AWS to be stored in AWS. Example: /iam-path/.
            car_restricted (bool | None | Unset): True if the policy has been restricted for use by a subset of
                Users/UGroups on a Cloud Access Role.
            car_restricted_user_group_ids (list[int] | None | Unset): List of groups IDs who have been allowed to use the
                iam policy on Cloud Access Roles in the system. Example: [1, 2].
            car_restricted_user_ids (list[int] | None | Unset): List of user IDs who have been allowed to use the iam policy
                on Cloud Access Roles in the system. Example: [1, 2].
            description (str | Unset): Description for the IAM policy in the application. Example: Gives user read only
                access to all AWS services..
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the iam policy. Is required if
                no owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the iam policy. Is required if no owner
                group IDs are listed. Example: [1, 2].
     """

    name: str
    policy: str
    aws_iam_path: str | Unset = UNSET
    car_restricted: bool | None | Unset = UNSET
    car_restricted_user_group_ids: list[int] | None | Unset = UNSET
    car_restricted_user_ids: list[int] | None | Unset = UNSET
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        policy = self.policy

        aws_iam_path = self.aws_iam_path

        car_restricted: bool | None | Unset
        if isinstance(self.car_restricted, Unset):
            car_restricted = UNSET
        else:
            car_restricted = self.car_restricted

        car_restricted_user_group_ids: list[int] | None | Unset
        if isinstance(self.car_restricted_user_group_ids, Unset):
            car_restricted_user_group_ids = UNSET
        elif isinstance(self.car_restricted_user_group_ids, list):
            car_restricted_user_group_ids = self.car_restricted_user_group_ids


        else:
            car_restricted_user_group_ids = self.car_restricted_user_group_ids

        car_restricted_user_ids: list[int] | None | Unset
        if isinstance(self.car_restricted_user_ids, Unset):
            car_restricted_user_ids = UNSET
        elif isinstance(self.car_restricted_user_ids, list):
            car_restricted_user_ids = self.car_restricted_user_ids


        else:
            car_restricted_user_ids = self.car_restricted_user_ids

        description = self.description

        owner_user_group_ids: list[int] | None | Unset
        if isinstance(self.owner_user_group_ids, Unset):
            owner_user_group_ids = UNSET
        elif isinstance(self.owner_user_group_ids, list):
            owner_user_group_ids = self.owner_user_group_ids


        else:
            owner_user_group_ids = self.owner_user_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids


        else:
            owner_user_ids = self.owner_user_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "policy": policy,
        })
        if aws_iam_path is not UNSET:
            field_dict["aws_iam_path"] = aws_iam_path
        if car_restricted is not UNSET:
            field_dict["car_restricted"] = car_restricted
        if car_restricted_user_group_ids is not UNSET:
            field_dict["car_restricted_user_group_ids"] = car_restricted_user_group_ids
        if car_restricted_user_ids is not UNSET:
            field_dict["car_restricted_user_ids"] = car_restricted_user_ids
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        policy = d.pop("policy")

        aws_iam_path = d.pop("aws_iam_path", UNSET)

        def _parse_car_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        car_restricted = _parse_car_restricted(d.pop("car_restricted", UNSET))


        def _parse_car_restricted_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                car_restricted_user_group_ids_type_0 = cast(list[int], data)

                return car_restricted_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        car_restricted_user_group_ids = _parse_car_restricted_user_group_ids(d.pop("car_restricted_user_group_ids", UNSET))


        def _parse_car_restricted_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                car_restricted_user_ids_type_0 = cast(list[int], data)

                return car_restricted_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        car_restricted_user_ids = _parse_car_restricted_user_ids(d.pop("car_restricted_user_ids", UNSET))


        description = d.pop("description", UNSET)

        def _parse_owner_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_group_ids_type_0 = cast(list[int], data)

                return owner_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_group_ids = _parse_owner_user_group_ids(d.pop("owner_user_group_ids", UNSET))


        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))


        iam_policy_create = cls(
            name=name,
            policy=policy,
            aws_iam_path=aws_iam_path,
            car_restricted=car_restricted,
            car_restricted_user_group_ids=car_restricted_user_group_ids,
            car_restricted_user_ids=car_restricted_user_ids,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
        )


        iam_policy_create.additional_properties = d
        return iam_policy_create

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
