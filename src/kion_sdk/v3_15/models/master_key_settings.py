from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.master_key_settings_master_key_storage_mode import MasterKeySettingsMasterKeyStorageMode
from ..types import UNSET, Unset






T = TypeVar("T", bound="MasterKeySettings")



@_attrs_define
class MasterKeySettings:
    """ MasterKeySettings represents master key configurations

        Attributes:
            master_key_storage_mode (MasterKeySettingsMasterKeyStorageMode): Sets the storage mode for where the master key
                is stored
                database DB
                aws AWS Example: aws.
            master_key_auto_rotate_period (str | Unset): The auto rotate period. Example: 30.
            secret_id (str | Unset): Full ARN path to the secret. Required if storage mode is not database. Example:
                arn:aws:secretsmanager:us-east-1:111122223333:secret:KionMasterKey.
     """

    master_key_storage_mode: MasterKeySettingsMasterKeyStorageMode
    master_key_auto_rotate_period: str | Unset = UNSET
    secret_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        master_key_storage_mode = self.master_key_storage_mode.value

        master_key_auto_rotate_period = self.master_key_auto_rotate_period

        secret_id = self.secret_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "master_key_storage_mode": master_key_storage_mode,
        })
        if master_key_auto_rotate_period is not UNSET:
            field_dict["master_key_auto_rotate_period"] = master_key_auto_rotate_period
        if secret_id is not UNSET:
            field_dict["secret_id"] = secret_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        master_key_storage_mode = MasterKeySettingsMasterKeyStorageMode(d.pop("master_key_storage_mode"))




        master_key_auto_rotate_period = d.pop("master_key_auto_rotate_period", UNSET)

        secret_id = d.pop("secret_id", UNSET)

        master_key_settings = cls(
            master_key_storage_mode=master_key_storage_mode,
            master_key_auto_rotate_period=master_key_auto_rotate_period,
            secret_id=secret_id,
        )


        master_key_settings.additional_properties = d
        return master_key_settings

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
