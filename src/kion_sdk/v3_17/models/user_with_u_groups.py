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





T = TypeVar("T", bound="UserWithUGroups")



@_attrs_define
class UserWithUGroups:
    """ UserWithUGroups defines a user with a list of user groups.

        Attributes:
            mfa (int | Unset):
            user (User | Unset): User defines a user.
            user_groups (list[UGroup] | None | Unset):
     """

    mfa: int | Unset = UNSET
    user: User | Unset = UNSET
    user_groups: list[UGroup] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.u_group import UGroup
        from ..models.user import User
        mfa = self.mfa

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        user_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.user_groups, Unset):
            user_groups = UNSET
        elif isinstance(self.user_groups, list):
            user_groups = []
            for user_groups_type_0_item_data in self.user_groups:
                user_groups_type_0_item = user_groups_type_0_item_data.to_dict()
                user_groups.append(user_groups_type_0_item)


        else:
            user_groups = self.user_groups


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mfa is not UNSET:
            field_dict["mfa"] = mfa
        if user is not UNSET:
            field_dict["user"] = user
        if user_groups is not UNSET:
            field_dict["user_groups"] = user_groups

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.u_group import UGroup
        from ..models.user import User
        d = dict(src_dict)
        mfa = d.pop("mfa", UNSET)

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)




        def _parse_user_groups(data: object) -> list[UGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_groups_type_0 = []
                _user_groups_type_0 = data
                for user_groups_type_0_item_data in (_user_groups_type_0):
                    user_groups_type_0_item = UGroup.from_dict(user_groups_type_0_item_data)



                    user_groups_type_0.append(user_groups_type_0_item)

                return user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UGroup] | None | Unset, data)

        user_groups = _parse_user_groups(d.pop("user_groups", UNSET))


        user_with_u_groups = cls(
            mfa=mfa,
            user=user,
            user_groups=user_groups,
        )


        user_with_u_groups.additional_properties = d
        return user_with_u_groups

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
