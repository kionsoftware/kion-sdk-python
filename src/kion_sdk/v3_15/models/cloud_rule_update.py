from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CloudRuleUpdate")



@_attrs_define
class CloudRuleUpdate:
    """ CloudRuleUpdate defines a Cloud Rule update.

        Attributes:
            concurrent_cft_sync (bool | None | Unset): Whether to run CFTs concurrently or not.
                If true, the application will deploy all templates at once in any order. (Faster)
                If false, the application will deploy each template in order and wait for completion before advancing to the
                next. (Slower) Example: True.
            description (str | Unset): Description of the Cloud Rule in the application. Example: Default Company Policies
                which apply to most resources.
            name (str | Unset): Name of the Cloud Rule in the application. Example: Company Policies.
            post_webhook_id (int | None | Unset): ID of a post-rule webhook attached to the Cloud Rule. Example: 1.
            pre_webhook_id (int | None | Unset): ID of a pre-rule webhook attached to the Cloud Rule. Example: 1.
     """

    concurrent_cft_sync: bool | None | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET
    post_webhook_id: int | None | Unset = UNSET
    pre_webhook_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        concurrent_cft_sync: bool | None | Unset
        if isinstance(self.concurrent_cft_sync, Unset):
            concurrent_cft_sync = UNSET
        else:
            concurrent_cft_sync = self.concurrent_cft_sync

        description = self.description

        name = self.name

        post_webhook_id: int | None | Unset
        if isinstance(self.post_webhook_id, Unset):
            post_webhook_id = UNSET
        else:
            post_webhook_id = self.post_webhook_id

        pre_webhook_id: int | None | Unset
        if isinstance(self.pre_webhook_id, Unset):
            pre_webhook_id = UNSET
        else:
            pre_webhook_id = self.pre_webhook_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if concurrent_cft_sync is not UNSET:
            field_dict["concurrent_cft_sync"] = concurrent_cft_sync
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if post_webhook_id is not UNSET:
            field_dict["post_webhook_id"] = post_webhook_id
        if pre_webhook_id is not UNSET:
            field_dict["pre_webhook_id"] = pre_webhook_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_concurrent_cft_sync(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        concurrent_cft_sync = _parse_concurrent_cft_sync(d.pop("concurrent_cft_sync", UNSET))


        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        def _parse_post_webhook_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        post_webhook_id = _parse_post_webhook_id(d.pop("post_webhook_id", UNSET))


        def _parse_pre_webhook_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pre_webhook_id = _parse_pre_webhook_id(d.pop("pre_webhook_id", UNSET))


        cloud_rule_update = cls(
            concurrent_cft_sync=concurrent_cft_sync,
            description=description,
            name=name,
            post_webhook_id=post_webhook_id,
            pre_webhook_id=pre_webhook_id,
        )


        cloud_rule_update.additional_properties = d
        return cloud_rule_update

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
