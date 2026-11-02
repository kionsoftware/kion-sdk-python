from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="OpenIDAccessRuleUpdate")



@_attrs_define
class OpenIDAccessRuleUpdate:
    """ OpenIDAccessRuleUpdate defines the expected payload for updating an OpenID access rule in the application.

        Attributes:
            assertion_name (str | Unset): AssertionName name of the assertion in OpenID. Example: username.
            assertion_regex (str | Unset): AssertionRegex is the regular expression used to determine a match. Example:
                ^cloudtamer-admins.
            cloudtamer_access_level_id (int | None | Unset): CloudtamerAccessLevelID is the ID that represents access level.
                1 represents full access, 2 represents no cloud account access and 3 represents no access. Example: 1.
     """

    assertion_name: str | Unset = UNSET
    assertion_regex: str | Unset = UNSET
    cloudtamer_access_level_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        assertion_name = self.assertion_name

        assertion_regex = self.assertion_regex

        cloudtamer_access_level_id: int | None | Unset
        if isinstance(self.cloudtamer_access_level_id, Unset):
            cloudtamer_access_level_id = UNSET
        else:
            cloudtamer_access_level_id = self.cloudtamer_access_level_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if assertion_name is not UNSET:
            field_dict["assertion_name"] = assertion_name
        if assertion_regex is not UNSET:
            field_dict["assertion_regex"] = assertion_regex
        if cloudtamer_access_level_id is not UNSET:
            field_dict["cloudtamer_access_level_id"] = cloudtamer_access_level_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assertion_name = d.pop("assertion_name", UNSET)

        assertion_regex = d.pop("assertion_regex", UNSET)

        def _parse_cloudtamer_access_level_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloudtamer_access_level_id = _parse_cloudtamer_access_level_id(d.pop("cloudtamer_access_level_id", UNSET))


        open_id_access_rule_update = cls(
            assertion_name=assertion_name,
            assertion_regex=assertion_regex,
            cloudtamer_access_level_id=cloudtamer_access_level_id,
        )


        open_id_access_rule_update.additional_properties = d
        return open_id_access_rule_update

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
