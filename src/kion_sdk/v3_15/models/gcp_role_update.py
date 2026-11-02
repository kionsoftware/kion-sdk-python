from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GCPRoleUpdate")



@_attrs_define
class GCPRoleUpdate:
    """ GCPRoleUpdate defines an GCP Role Definition update.

        Attributes:
            car_restricted (bool | None | Unset): True if the policy has been restricted for use by a subset of
                Users/UGroups on a Cloud Access Role.
            description (str | Unset): Description for the GCP Role Definition in the application and GCP. Example: Gives
                user read only access to all GCP services..
            gcp_role_launch_stage (int | Unset): GCPRoleLaunchStage is the launch stage for a gcp role
            name (str | Unset): Name of the GCP Role Definition in the application and GCP. Example: Read Only.
            owner_user_group_ids (list[int] | None | Unset): List of group IDs who will own the GCP Role. Ownership will
                remain unchanged if not omitted from the update request. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the GCP Role. Ownership will remain
                unchanged if not omitted from the update request. Example: [1, 2].
            role_denials (list[str] | None | Unset): List of GCP Permissions to deny when applying this role. Wildcards are
                supported. Example: ['iam.roles.get', 'resourcemanager.*'].
            role_permissions (list[str] | None | Unset): List of GCP Permissions to assign the role. Example:
                ['iam.roles.get', 'iam.roles.list'].
     """

    car_restricted: bool | None | Unset = UNSET
    description: str | Unset = UNSET
    gcp_role_launch_stage: int | Unset = UNSET
    name: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    role_denials: list[str] | None | Unset = UNSET
    role_permissions: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        car_restricted: bool | None | Unset
        if isinstance(self.car_restricted, Unset):
            car_restricted = UNSET
        else:
            car_restricted = self.car_restricted

        description = self.description

        gcp_role_launch_stage = self.gcp_role_launch_stage

        name = self.name

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

        role_permissions: list[str] | None | Unset
        if isinstance(self.role_permissions, Unset):
            role_permissions = UNSET
        elif isinstance(self.role_permissions, list):
            role_permissions = self.role_permissions


        else:
            role_permissions = self.role_permissions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if car_restricted is not UNSET:
            field_dict["car_restricted"] = car_restricted
        if description is not UNSET:
            field_dict["description"] = description
        if gcp_role_launch_stage is not UNSET:
            field_dict["gcp_role_launch_stage"] = gcp_role_launch_stage
        if name is not UNSET:
            field_dict["name"] = name
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids
        if role_denials is not UNSET:
            field_dict["role_denials"] = role_denials
        if role_permissions is not UNSET:
            field_dict["role_permissions"] = role_permissions

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

        gcp_role_launch_stage = d.pop("gcp_role_launch_stage", UNSET)

        name = d.pop("name", UNSET)

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


        def _parse_role_permissions(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                role_permissions_type_0 = cast(list[str], data)

                return role_permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        role_permissions = _parse_role_permissions(d.pop("role_permissions", UNSET))


        gcp_role_update = cls(
            car_restricted=car_restricted,
            description=description,
            gcp_role_launch_stage=gcp_role_launch_stage,
            name=name,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
            role_denials=role_denials,
            role_permissions=role_permissions,
        )


        gcp_role_update.additional_properties = d
        return gcp_role_update

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
