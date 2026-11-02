from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AccountCloudRuleState")



@_attrs_define
class AccountCloudRuleState:
    """ AccountCloudRuleState defines the state of an account cloud rule.

        Attributes:
            account_id (int | None | Unset): Account ID. Example: 1.
            cft_end (str | Unset): Date when the cft finished. Example: 2019-02-12T22:57:10+0000.
            cft_failure_count (int | Unset): The amount of times the CFT has failed. Example: 1.
            cft_needs_reattempt (bool | None | Unset): If the cft has failed and needs to be reattempted.
            cft_start (str | Unset): Date when the cft was started. Example: 2019-02-12T22:57:10+0000.
            cloud_rule_id (int | None | Unset): Cloud Rule ID. Example: 1.
            post_needs_reattempt (bool | None | Unset): If the post-rule webhook has failed and needs to be reattempted.
            post_webhook_end (str | Unset): Date when the post webhook finished. Example: 2019-02-12T22:57:10+0000.
            post_webhook_start (str | Unset): Date when the post webhook was started. Example: 2019-02-12T22:57:10+0000.
            pre_needs_reattempt (bool | None | Unset): If the pre-rule webhook has failed and needs to be reattempted.
            pre_webhook_end (str | Unset): Date when the pre webhook finished. Example: 2019-02-12T22:57:10+0000.
            pre_webhook_start (str | Unset): Date when the pre webhook was started. Example: 2019-02-12T22:57:10+0000.
     """

    account_id: int | None | Unset = UNSET
    cft_end: str | Unset = UNSET
    cft_failure_count: int | Unset = UNSET
    cft_needs_reattempt: bool | None | Unset = UNSET
    cft_start: str | Unset = UNSET
    cloud_rule_id: int | None | Unset = UNSET
    post_needs_reattempt: bool | None | Unset = UNSET
    post_webhook_end: str | Unset = UNSET
    post_webhook_start: str | Unset = UNSET
    pre_needs_reattempt: bool | None | Unset = UNSET
    pre_webhook_end: str | Unset = UNSET
    pre_webhook_start: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id: int | None | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        cft_end = self.cft_end

        cft_failure_count = self.cft_failure_count

        cft_needs_reattempt: bool | None | Unset
        if isinstance(self.cft_needs_reattempt, Unset):
            cft_needs_reattempt = UNSET
        else:
            cft_needs_reattempt = self.cft_needs_reattempt

        cft_start = self.cft_start

        cloud_rule_id: int | None | Unset
        if isinstance(self.cloud_rule_id, Unset):
            cloud_rule_id = UNSET
        else:
            cloud_rule_id = self.cloud_rule_id

        post_needs_reattempt: bool | None | Unset
        if isinstance(self.post_needs_reattempt, Unset):
            post_needs_reattempt = UNSET
        else:
            post_needs_reattempt = self.post_needs_reattempt

        post_webhook_end = self.post_webhook_end

        post_webhook_start = self.post_webhook_start

        pre_needs_reattempt: bool | None | Unset
        if isinstance(self.pre_needs_reattempt, Unset):
            pre_needs_reattempt = UNSET
        else:
            pre_needs_reattempt = self.pre_needs_reattempt

        pre_webhook_end = self.pre_webhook_end

        pre_webhook_start = self.pre_webhook_start


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if cft_end is not UNSET:
            field_dict["cft_end"] = cft_end
        if cft_failure_count is not UNSET:
            field_dict["cft_failure_count"] = cft_failure_count
        if cft_needs_reattempt is not UNSET:
            field_dict["cft_needs_reattempt"] = cft_needs_reattempt
        if cft_start is not UNSET:
            field_dict["cft_start"] = cft_start
        if cloud_rule_id is not UNSET:
            field_dict["cloud_rule_id"] = cloud_rule_id
        if post_needs_reattempt is not UNSET:
            field_dict["post_needs_reattempt"] = post_needs_reattempt
        if post_webhook_end is not UNSET:
            field_dict["post_webhook_end"] = post_webhook_end
        if post_webhook_start is not UNSET:
            field_dict["post_webhook_start"] = post_webhook_start
        if pre_needs_reattempt is not UNSET:
            field_dict["pre_needs_reattempt"] = pre_needs_reattempt
        if pre_webhook_end is not UNSET:
            field_dict["pre_webhook_end"] = pre_webhook_end
        if pre_webhook_start is not UNSET:
            field_dict["pre_webhook_start"] = pre_webhook_start

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


        cft_end = d.pop("cft_end", UNSET)

        cft_failure_count = d.pop("cft_failure_count", UNSET)

        def _parse_cft_needs_reattempt(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        cft_needs_reattempt = _parse_cft_needs_reattempt(d.pop("cft_needs_reattempt", UNSET))


        cft_start = d.pop("cft_start", UNSET)

        def _parse_cloud_rule_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        cloud_rule_id = _parse_cloud_rule_id(d.pop("cloud_rule_id", UNSET))


        def _parse_post_needs_reattempt(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        post_needs_reattempt = _parse_post_needs_reattempt(d.pop("post_needs_reattempt", UNSET))


        post_webhook_end = d.pop("post_webhook_end", UNSET)

        post_webhook_start = d.pop("post_webhook_start", UNSET)

        def _parse_pre_needs_reattempt(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        pre_needs_reattempt = _parse_pre_needs_reattempt(d.pop("pre_needs_reattempt", UNSET))


        pre_webhook_end = d.pop("pre_webhook_end", UNSET)

        pre_webhook_start = d.pop("pre_webhook_start", UNSET)

        account_cloud_rule_state = cls(
            account_id=account_id,
            cft_end=cft_end,
            cft_failure_count=cft_failure_count,
            cft_needs_reattempt=cft_needs_reattempt,
            cft_start=cft_start,
            cloud_rule_id=cloud_rule_id,
            post_needs_reattempt=post_needs_reattempt,
            post_webhook_end=post_webhook_end,
            post_webhook_start=post_webhook_start,
            pre_needs_reattempt=pre_needs_reattempt,
            pre_webhook_end=pre_webhook_end,
            pre_webhook_start=pre_webhook_start,
        )


        account_cloud_rule_state.additional_properties = d
        return account_cloud_rule_state

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
