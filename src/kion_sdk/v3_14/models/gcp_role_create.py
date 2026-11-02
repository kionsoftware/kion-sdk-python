from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GCPRoleCreate")



@_attrs_define
class GCPRoleCreate:
    """ GCPRoleCreate defines an GCP Role creation.

        Attributes:
            name (str): Name of the GCP Role in the application. Example: Read Only.
            role_permissions (list[str] | None): List of GCP Permissions to assign the role Example: ['iam.roles.get',
                'iam.roles.list'].
            car_restricted_user_group_ids (list[int] | None | Unset): List of groups IDs who have been allowed to use the
                GCP Role on Cloud Access Roles in the system. Example: [1, 2].
            car_restricted_user_ids (list[int] | None | Unset): List of user IDs who have been allowed to use the GCP Role
                on Cloud Access Roles in the system. Example: [1, 2].
            description (str | Unset): Description for the GCP Role in the application. Example: Gives user read only access
                to all GCP services..
            gcp_role_launch_stage (int | Unset): GCPRoleLaunchStage is the launch stage for a gcp role
            owner_user_group_ids (list[int] | None | Unset): List of group IDs who will own the GCP Role. Is required if no
                owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the GCP Role. Is required if no owner
                group IDs are listed. Example: [1, 2].
            role_denials (list[str] | None | Unset): List of GCP Permissions to deny when applying this role. Wildcards are
                supported. Example: ['iam.roles.get', 'resourcemanager.*'].
     """

    name: str
    role_permissions: list[str] | None
    car_restricted_user_group_ids: list[int] | None | Unset = UNSET
    car_restricted_user_ids: list[int] | None | Unset = UNSET
    description: str | Unset = UNSET
    gcp_role_launch_stage: int | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    role_denials: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        role_permissions: list[str] | None
        if isinstance(self.role_permissions, list):
            role_permissions = self.role_permissions


        else:
            role_permissions = self.role_permissions

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

        gcp_role_launch_stage = self.gcp_role_launch_stage

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

        role_denials: list[str] | None | Unset
        if isinstance(self.role_denials, Unset):
            role_denials = UNSET
        elif isinstance(self.role_denials, list):
            role_denials = self.role_denials


        else:
            role_denials = self.role_denials


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "role_permissions": role_permissions,
        })
        if car_restricted_user_group_ids is not UNSET:
            field_dict["car_restricted_user_group_ids"] = car_restricted_user_group_ids
        if car_restricted_user_ids is not UNSET:
            field_dict["car_restricted_user_ids"] = car_restricted_user_ids
        if description is not UNSET:
            field_dict["description"] = description
        if gcp_role_launch_stage is not UNSET:
            field_dict["gcp_role_launch_stage"] = gcp_role_launch_stage
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if role_denials is not UNSET:
            field_dict["role_denials"] = role_denials

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_role_permissions(data: object) -> list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_permissions_type_0 = cast(list[str], data)

                return role_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None, data)

        role_permissions = _parse_role_permissions(d.pop("role_permissions"))


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

        gcp_role_launch_stage = d.pop("gcp_role_launch_stage", UNSET)

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


        def _parse_role_denials(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_denials_type_0 = cast(list[str], data)

                return role_denials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        role_denials = _parse_role_denials(d.pop("role_denials", UNSET))


        gcp_role_create = cls(
            name=name,
            role_permissions=role_permissions,
            car_restricted_user_group_ids=car_restricted_user_group_ids,
            car_restricted_user_ids=car_restricted_user_ids,
            description=description,
            gcp_role_launch_stage=gcp_role_launch_stage,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            role_denials=role_denials,
        )


        gcp_role_create.additional_properties = d
        return gcp_role_create

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
