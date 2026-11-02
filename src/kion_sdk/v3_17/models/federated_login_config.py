from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="FederatedLoginConfig")



@_attrs_define
class FederatedLoginConfig:
    """ FederatedLoginConfig represents the enabled status of federated logins

        Attributes:
            federated_login_enabled (bool | None | Unset): Federated Login enabled status
     """

    federated_login_enabled: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        federated_login_enabled: bool | None | Unset
        if isinstance(self.federated_login_enabled, Unset):
            federated_login_enabled = UNSET
        else:
            federated_login_enabled = self.federated_login_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if federated_login_enabled is not UNSET:
            field_dict["federated_login_enabled"] = federated_login_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_federated_login_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        federated_login_enabled = _parse_federated_login_enabled(d.pop("federated_login_enabled", UNSET))


        federated_login_config = cls(
            federated_login_enabled=federated_login_enabled,
        )


        federated_login_config.additional_properties = d
        return federated_login_config

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
