from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.master_key_settings_valid import MasterKeySettingsValid





T = TypeVar("T", bound="TestMasterKeySettingsResponse200")



@_attrs_define
class TestMasterKeySettingsResponse200:
    """ 
        Attributes:
            data (MasterKeySettingsValid | Unset):
            status (int | Unset): HTTP status code. Example: 200.
     """

    data: MasterKeySettingsValid | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.master_key_settings_valid import MasterKeySettingsValid
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.master_key_settings_valid import MasterKeySettingsValid
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: MasterKeySettingsValid | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = MasterKeySettingsValid.from_dict(_data)




        status = d.pop("status", UNSET)

        test_master_key_settings_response_200 = cls(
            data=data,
            status=status,
        )


        test_master_key_settings_response_200.additional_properties = d
        return test_master_key_settings_response_200

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
