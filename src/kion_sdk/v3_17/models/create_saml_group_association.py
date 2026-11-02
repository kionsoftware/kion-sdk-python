from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreateSAMLGroupAssociation")



@_attrs_define
class CreateSAMLGroupAssociation:
    """ CreateSAMLGroupAssociation defines an saml group association creation.

        Attributes:
            assertion_name (str | Unset): AssertionName of the assertion in saml. Example: memberOf.
            assertion_regex (str | Unset): Regular expression used to determine a match. Example: ^cloudtamer-admins.
            idms_id (int | None | Unset): ID of the idms the group association will apply to. Example: 1.
            update_on_login (bool | None | Unset): If the group associations should be updated every time a user logs in.
                Example: True.
            user_group_id (int | None | Unset): ID of the user group this assertion will map to. Example: 1.
     """

    assertion_name: str | Unset = UNSET
    assertion_regex: str | Unset = UNSET
    idms_id: int | None | Unset = UNSET
    update_on_login: bool | None | Unset = UNSET
    user_group_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        assertion_name = self.assertion_name

        assertion_regex = self.assertion_regex

        idms_id: int | None | Unset
        if isinstance(self.idms_id, Unset):
            idms_id = UNSET
        else:
            idms_id = self.idms_id

        update_on_login: bool | None | Unset
        if isinstance(self.update_on_login, Unset):
            update_on_login = UNSET
        else:
            update_on_login = self.update_on_login

        user_group_id: int | None | Unset
        if isinstance(self.user_group_id, Unset):
            user_group_id = UNSET
        else:
            user_group_id = self.user_group_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if assertion_name is not UNSET:
            field_dict["assertion_name"] = assertion_name
        if assertion_regex is not UNSET:
            field_dict["assertion_regex"] = assertion_regex
        if idms_id is not UNSET:
            field_dict["idms_id"] = idms_id
        if update_on_login is not UNSET:
            field_dict["update_on_login"] = update_on_login
        if user_group_id is not UNSET:
            field_dict["user_group_id"] = user_group_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assertion_name = d.pop("assertion_name", UNSET)

        assertion_regex = d.pop("assertion_regex", UNSET)

        def _parse_idms_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        idms_id = _parse_idms_id(d.pop("idms_id", UNSET))


        def _parse_update_on_login(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        update_on_login = _parse_update_on_login(d.pop("update_on_login", UNSET))


        def _parse_user_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        user_group_id = _parse_user_group_id(d.pop("user_group_id", UNSET))


        create_saml_group_association = cls(
            assertion_name=assertion_name,
            assertion_regex=assertion_regex,
            idms_id=idms_id,
            update_on_login=update_on_login,
            user_group_id=user_group_id,
        )


        create_saml_group_association.additional_properties = d
        return create_saml_group_association

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
