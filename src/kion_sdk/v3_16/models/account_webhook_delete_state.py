from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccountWebhookDeleteState")



@_attrs_define
class AccountWebhookDeleteState:
    """ AccountWebhookDeleteState defines the state of an account webhook delete.

        Attributes:
            account_id (int | None | Unset): Account ID. Example: 1.
            cloud_rule_id (int | None | Unset): Cloud Rule ID. Example: 1.
            end (str | Unset): Date when the pre webhook finished. Example: 2019-02-12T22:57:10+0000.
            id (int | Unset): ID Example: 1.
            needs_reattempt (bool | None | Unset): If the webhook delete has failed and needs to be reattempted.
            start (str | Unset): Date when the pre webhook was started. Example: 2019-02-12T22:57:10+0000.
            type_id (int | None | Unset): Type ID. (1 = pre-rule webhook, 2 = post-rule webhook) Example: 1.
            webhook_id (int | None | Unset): Webhook ID. Example: 1.
     """

    account_id: int | None | Unset = UNSET
    cloud_rule_id: int | None | Unset = UNSET
    end: str | Unset = UNSET
    id: int | Unset = UNSET
    needs_reattempt: bool | None | Unset = UNSET
    start: str | Unset = UNSET
    type_id: int | None | Unset = UNSET
    webhook_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        cloud_rule_id: int | None | Unset
        if isinstance(self.cloud_rule_id, Unset):
            cloud_rule_id = UNSET
        else:
            cloud_rule_id = self.cloud_rule_id

        end = self.end

        id = self.id

        needs_reattempt: bool | None | Unset
        if isinstance(self.needs_reattempt, Unset):
            needs_reattempt = UNSET
        else:
            needs_reattempt = self.needs_reattempt

        start = self.start

        type_id: int | None | Unset
        if isinstance(self.type_id, Unset):
            type_id = UNSET
        else:
            type_id = self.type_id

        webhook_id: int | None | Unset
        if isinstance(self.webhook_id, Unset):
            webhook_id = UNSET
        else:
            webhook_id = self.webhook_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if cloud_rule_id is not UNSET:
            field_dict["cloud_rule_id"] = cloud_rule_id
        if end is not UNSET:
            field_dict["end"] = end
        if id is not UNSET:
            field_dict["id"] = id
        if needs_reattempt is not UNSET:
            field_dict["needs_reattempt"] = needs_reattempt
        if start is not UNSET:
            field_dict["start"] = start
        if type_id is not UNSET:
            field_dict["type_id"] = type_id
        if webhook_id is not UNSET:
            field_dict["webhook_id"] = webhook_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_account_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        account_id = _parse_account_id(d.pop("account_id", UNSET))


        def _parse_cloud_rule_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_rule_id = _parse_cloud_rule_id(d.pop("cloud_rule_id", UNSET))


        end = d.pop("end", UNSET)

        id = d.pop("id", UNSET)

        def _parse_needs_reattempt(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        needs_reattempt = _parse_needs_reattempt(d.pop("needs_reattempt", UNSET))


        start = d.pop("start", UNSET)

        def _parse_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        type_id = _parse_type_id(d.pop("type_id", UNSET))


        def _parse_webhook_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        webhook_id = _parse_webhook_id(d.pop("webhook_id", UNSET))


        account_webhook_delete_state = cls(
            account_id=account_id,
            cloud_rule_id=cloud_rule_id,
            end=end,
            id=id,
            needs_reattempt=needs_reattempt,
            start=start,
            type_id=type_id,
            webhook_id=webhook_id,
        )


        account_webhook_delete_state.additional_properties = d
        return account_webhook_delete_state

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
