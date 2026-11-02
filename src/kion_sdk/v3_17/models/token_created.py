from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.auth_token import AuthToken





T = TypeVar("T", bound="TokenCreated")



@_attrs_define
class TokenCreated:
    """ TokenCreated defines a Token created response.

        Attributes:
            access (AuthToken | Unset): AuthToken defines a user token.
            id (int | Unset): ID of the record in the application Example: 1.
            refresh (AuthToken | Unset): AuthToken defines a user token.
            user_id (int | None | Unset): ID of the authenticated user Example: 1.
     """

    access: AuthToken | Unset = UNSET
    id: int | Unset = UNSET
    refresh: AuthToken | Unset = UNSET
    user_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.auth_token import AuthToken
        access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.to_dict()

        id = self.id

        refresh: dict[str, Any] | Unset = UNSET
        if not isinstance(self.refresh, Unset):
            refresh = self.refresh.to_dict()

        user_id: int | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access is not UNSET:
            field_dict["access"] = access
        if id is not UNSET:
            field_dict["id"] = id
        if refresh is not UNSET:
            field_dict["refresh"] = refresh
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_token import AuthToken
        d = dict(src_dict)
        _access = d.pop("access", UNSET)
        access: AuthToken | Unset
        if isinstance(_access,  Unset):
            access = UNSET
        else:
            access = AuthToken.from_dict(_access)




        id = d.pop("id", UNSET)

        _refresh = d.pop("refresh", UNSET)
        refresh: AuthToken | Unset
        if isinstance(_refresh,  Unset):
            refresh = UNSET
        else:
            refresh = AuthToken.from_dict(_refresh)




        def _parse_user_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))


        token_created = cls(
            access=access,
            id=id,
            refresh=refresh,
            user_id=user_id,
        )


        token_created.additional_properties = d
        return token_created

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
