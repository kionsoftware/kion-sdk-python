from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.u_group import UGroup
  from ..models.user import User





T = TypeVar("T", bound="UGroupWithUsersAndOwners")



@_attrs_define
class UGroupWithUsersAndOwners:
    """ UGroupWithUsersAndOwners defines a user group with users and owners.

        Attributes:
            owner_group (list[UGroup] | None | Unset):
            owner_users (list[User] | None | Unset):
            user_group (UGroup | Unset): UGroup defines a user group.
            users (list[User] | None | Unset): Users that are in the user group.
            viewer_groups (list[UGroup] | None | Unset):
            viewer_users (list[User] | None | Unset):
     """

    owner_group: list[UGroup] | None | Unset = UNSET
    owner_users: list[User] | None | Unset = UNSET
    user_group: UGroup | Unset = UNSET
    users: list[User] | None | Unset = UNSET
    viewer_groups: list[UGroup] | None | Unset = UNSET
    viewer_users: list[User] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.u_group import UGroup
        from ..models.user import User
        owner_group: list[dict[str, Any]] | None | Unset
        if isinstance(self.owner_group, Unset):
            owner_group = UNSET
        elif isinstance(self.owner_group, list):
            owner_group = []
            for owner_group_type_0_item_data in self.owner_group:
                owner_group_type_0_item = owner_group_type_0_item_data.to_dict()
                owner_group.append(owner_group_type_0_item)


        else:
            owner_group = self.owner_group

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

        user_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_group, Unset):
            user_group = self.user_group.to_dict()

        users: list[dict[str, Any]] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, list):
            users = []
            for users_type_0_item_data in self.users:
                users_type_0_item = users_type_0_item_data.to_dict()
                users.append(users_type_0_item)


        else:
            users = self.users

        viewer_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.viewer_groups, Unset):
            viewer_groups = UNSET
        elif isinstance(self.viewer_groups, list):
            viewer_groups = []
            for viewer_groups_type_0_item_data in self.viewer_groups:
                viewer_groups_type_0_item = viewer_groups_type_0_item_data.to_dict()
                viewer_groups.append(viewer_groups_type_0_item)


        else:
            viewer_groups = self.viewer_groups

        viewer_users: list[dict[str, Any]] | None | Unset
        if isinstance(self.viewer_users, Unset):
            viewer_users = UNSET
        elif isinstance(self.viewer_users, list):
            viewer_users = []
            for viewer_users_type_0_item_data in self.viewer_users:
                viewer_users_type_0_item = viewer_users_type_0_item_data.to_dict()
                viewer_users.append(viewer_users_type_0_item)


        else:
            viewer_users = self.viewer_users


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if owner_group is not UNSET:
            field_dict["owner_group"] = owner_group
        if owner_users is not UNSET:
            field_dict["owner_users"] = owner_users
        if user_group is not UNSET:
            field_dict["user_group"] = user_group
        if users is not UNSET:
            field_dict["users"] = users
        if viewer_groups is not UNSET:
            field_dict["viewer_groups"] = viewer_groups
        if viewer_users is not UNSET:
            field_dict["viewer_users"] = viewer_users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.u_group import UGroup
        from ..models.user import User
        d = dict(src_dict)
        def _parse_owner_group(data: object) -> list[UGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_group_type_0 = []
                _owner_group_type_0 = data
                for owner_group_type_0_item_data in (_owner_group_type_0):
                    owner_group_type_0_item = UGroup.from_dict(owner_group_type_0_item_data)



                    owner_group_type_0.append(owner_group_type_0_item)

                return owner_group_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroup] | None | Unset, data)

        owner_group = _parse_owner_group(d.pop("owner_group", UNSET))


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


        _user_group = d.pop("user_group", UNSET)
        user_group: UGroup | Unset
        if isinstance(_user_group,  Unset):
            user_group = UNSET
        else:
            user_group = UGroup.from_dict(_user_group)




        def _parse_users(data: object) -> list[User] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                users_type_0 = []
                _users_type_0 = data
                for users_type_0_item_data in (_users_type_0):
                    users_type_0_item = User.from_dict(users_type_0_item_data)



                    users_type_0.append(users_type_0_item)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[User] | None | Unset, data)

        users = _parse_users(d.pop("users", UNSET))


        def _parse_viewer_groups(data: object) -> list[UGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                viewer_groups_type_0 = []
                _viewer_groups_type_0 = data
                for viewer_groups_type_0_item_data in (_viewer_groups_type_0):
                    viewer_groups_type_0_item = UGroup.from_dict(viewer_groups_type_0_item_data)



                    viewer_groups_type_0.append(viewer_groups_type_0_item)

                return viewer_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroup] | None | Unset, data)

        viewer_groups = _parse_viewer_groups(d.pop("viewer_groups", UNSET))


        def _parse_viewer_users(data: object) -> list[User] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                viewer_users_type_0 = []
                _viewer_users_type_0 = data
                for viewer_users_type_0_item_data in (_viewer_users_type_0):
                    viewer_users_type_0_item = User.from_dict(viewer_users_type_0_item_data)



                    viewer_users_type_0.append(viewer_users_type_0_item)

                return viewer_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[User] | None | Unset, data)

        viewer_users = _parse_viewer_users(d.pop("viewer_users", UNSET))


        u_group_with_users_and_owners = cls(
            owner_group=owner_group,
            owner_users=owner_users,
            user_group=user_group,
            users=users,
            viewer_groups=viewer_groups,
            viewer_users=viewer_users,
        )


        u_group_with_users_and_owners.additional_properties = d
        return u_group_with_users_and_owners

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
