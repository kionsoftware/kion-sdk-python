from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.gcp_role import GCPRole
  from ..models.u_group import UGroup
  from ..models.user import User





T = TypeVar("T", bound="GCPRoleWithOwners")



@_attrs_define
class GCPRoleWithOwners:
    """ GCPRoleWithOwners defines an GCP Role with owners.

        Attributes:
            car_restricted_ugroups (list[UGroup] | None | Unset):
            car_restricted_users (list[User] | None | Unset):
            gcp_role (GCPRole | Unset): GCPRole defines a GCP Role.
            owner_user_groups (list[UGroup] | None | Unset):
            owner_users (list[User] | None | Unset):
     """

    car_restricted_ugroups: list[UGroup] | None | Unset = UNSET
    car_restricted_users: list[User] | None | Unset = UNSET
    gcp_role: GCPRole | Unset = UNSET
    owner_user_groups: list[UGroup] | None | Unset = UNSET
    owner_users: list[User] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.gcp_role import GCPRole
        from ..models.u_group import UGroup
        from ..models.user import User
        car_restricted_ugroups: list[dict[str, Any]] | None | Unset
        if isinstance(self.car_restricted_ugroups, Unset):
            car_restricted_ugroups = UNSET
        elif isinstance(self.car_restricted_ugroups, list):
            car_restricted_ugroups = []
            for car_restricted_ugroups_type_0_item_data in self.car_restricted_ugroups:
                car_restricted_ugroups_type_0_item = car_restricted_ugroups_type_0_item_data.to_dict()
                car_restricted_ugroups.append(car_restricted_ugroups_type_0_item)


        else:
            car_restricted_ugroups = self.car_restricted_ugroups

        car_restricted_users: list[dict[str, Any]] | None | Unset
        if isinstance(self.car_restricted_users, Unset):
            car_restricted_users = UNSET
        elif isinstance(self.car_restricted_users, list):
            car_restricted_users = []
            for car_restricted_users_type_0_item_data in self.car_restricted_users:
                car_restricted_users_type_0_item = car_restricted_users_type_0_item_data.to_dict()
                car_restricted_users.append(car_restricted_users_type_0_item)


        else:
            car_restricted_users = self.car_restricted_users

        gcp_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_role, Unset):
            gcp_role = self.gcp_role.to_dict()

        owner_user_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_user_groups, Unset):
            owner_user_groups = UNSET
        elif isinstance(self.owner_user_groups, list):
            owner_user_groups = []
            for owner_user_groups_type_0_item_data in self.owner_user_groups:
                owner_user_groups_type_0_item = owner_user_groups_type_0_item_data.to_dict()
                owner_user_groups.append(owner_user_groups_type_0_item)


        else:
            owner_user_groups = self.owner_user_groups

        owner_users: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_users, Unset):
            owner_users = UNSET
        elif isinstance(self.owner_users, list):
            owner_users = []
            for owner_users_type_0_item_data in self.owner_users:
                owner_users_type_0_item = owner_users_type_0_item_data.to_dict()
                owner_users.append(owner_users_type_0_item)


        else:
            owner_users = self.owner_users


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if car_restricted_ugroups is not UNSET:
            field_dict["car_restricted_ugroups"] = car_restricted_ugroups
        if car_restricted_users is not UNSET:
            field_dict["car_restricted_users"] = car_restricted_users
        if gcp_role is not UNSET:
            field_dict["gcp_role"] = gcp_role
        if owner_user_groups is not UNSET:
            field_dict["owner_user_groups"] = owner_user_groups
        if owner_users is not UNSET:
            field_dict["owner_users"] = owner_users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gcp_role import GCPRole
        from ..models.u_group import UGroup
        from ..models.user import User
        d = dict(src_dict)
        def _parse_car_restricted_ugroups(data: object) -> list[UGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                car_restricted_ugroups_type_0 = []
                _car_restricted_ugroups_type_0 = data
                for car_restricted_ugroups_type_0_item_data in (_car_restricted_ugroups_type_0):
                    car_restricted_ugroups_type_0_item = UGroup.from_dict(car_restricted_ugroups_type_0_item_data)



                    car_restricted_ugroups_type_0.append(car_restricted_ugroups_type_0_item)

                return car_restricted_ugroups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroup] | None | Unset, data)

        car_restricted_ugroups = _parse_car_restricted_ugroups(d.pop("car_restricted_ugroups", UNSET))


        def _parse_car_restricted_users(data: object) -> list[User] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                car_restricted_users_type_0 = []
                _car_restricted_users_type_0 = data
                for car_restricted_users_type_0_item_data in (_car_restricted_users_type_0):
                    car_restricted_users_type_0_item = User.from_dict(car_restricted_users_type_0_item_data)



                    car_restricted_users_type_0.append(car_restricted_users_type_0_item)

                return car_restricted_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[User] | None | Unset, data)

        car_restricted_users = _parse_car_restricted_users(d.pop("car_restricted_users", UNSET))


        _gcp_role = d.pop("gcp_role", UNSET)
        gcp_role: GCPRole | Unset
        if isinstance(_gcp_role,  Unset):
            gcp_role = UNSET
        else:
            gcp_role = GCPRole.from_dict(_gcp_role)




        def _parse_owner_user_groups(data: object) -> list[UGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_groups_type_0 = []
                _owner_user_groups_type_0 = data
                for owner_user_groups_type_0_item_data in (_owner_user_groups_type_0):
                    owner_user_groups_type_0_item = UGroup.from_dict(owner_user_groups_type_0_item_data)



                    owner_user_groups_type_0.append(owner_user_groups_type_0_item)

                return owner_user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroup] | None | Unset, data)

        owner_user_groups = _parse_owner_user_groups(d.pop("owner_user_groups", UNSET))


        def _parse_owner_users(data: object) -> list[User] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_users_type_0 = []
                _owner_users_type_0 = data
                for owner_users_type_0_item_data in (_owner_users_type_0):
                    owner_users_type_0_item = User.from_dict(owner_users_type_0_item_data)



                    owner_users_type_0.append(owner_users_type_0_item)

                return owner_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[User] | None | Unset, data)

        owner_users = _parse_owner_users(d.pop("owner_users", UNSET))


        gcp_role_with_owners = cls(
            car_restricted_ugroups=car_restricted_ugroups,
            car_restricted_users=car_restricted_users,
            gcp_role=gcp_role,
            owner_user_groups=owner_user_groups,
            owner_users=owner_users,
        )


        gcp_role_with_owners.additional_properties = d
        return gcp_role_with_owners

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
