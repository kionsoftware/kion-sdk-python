from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.account_cloud_rule_state import AccountCloudRuleState
  from ..models.account_webhook_delete_state import AccountWebhookDeleteState





T = TypeVar("T", bound="ReattemptsNeeded")



@_attrs_define
class ReattemptsNeeded:
    """ ReattemptsNeeded contains lists of failed webhook and CFT triggers.

        Attributes:
            failed_adds (list[AccountCloudRuleState] | None | Unset): Failed adds of a cloud rule to an account.
            failed_removes (list[AccountWebhookDeleteState] | None | Unset): Failed deletes of cloud rule webhooks from an
                account.
     """

    failed_adds: list[AccountCloudRuleState] | None | Unset = UNSET
    failed_removes: list[AccountWebhookDeleteState] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_cloud_rule_state import AccountCloudRuleState
        from ..models.account_webhook_delete_state import AccountWebhookDeleteState
        failed_adds: list[dict[str, Any]] | None | Unset
        if isinstance(self.failed_adds, Unset):
            failed_adds = UNSET
        elif isinstance(self.failed_adds, list):
            failed_adds = []
            for failed_adds_type_0_item_data in self.failed_adds:
                failed_adds_type_0_item = failed_adds_type_0_item_data.to_dict()
                failed_adds.append(failed_adds_type_0_item)


        else:
            failed_adds = self.failed_adds

        failed_removes: list[dict[str, Any]] | None | Unset
        if isinstance(self.failed_removes, Unset):
            failed_removes = UNSET
        elif isinstance(self.failed_removes, list):
            failed_removes = []
            for failed_removes_type_0_item_data in self.failed_removes:
                failed_removes_type_0_item = failed_removes_type_0_item_data.to_dict()
                failed_removes.append(failed_removes_type_0_item)


        else:
            failed_removes = self.failed_removes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if failed_adds is not UNSET:
            field_dict["failed_adds"] = failed_adds
        if failed_removes is not UNSET:
            field_dict["failed_removes"] = failed_removes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_cloud_rule_state import AccountCloudRuleState
        from ..models.account_webhook_delete_state import AccountWebhookDeleteState
        d = dict(src_dict)
        def _parse_failed_adds(data: object) -> list[AccountCloudRuleState] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                failed_adds_type_0 = []
                _failed_adds_type_0 = data
                for failed_adds_type_0_item_data in (_failed_adds_type_0):
                    failed_adds_type_0_item = AccountCloudRuleState.from_dict(failed_adds_type_0_item_data)



                    failed_adds_type_0.append(failed_adds_type_0_item)

                return failed_adds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AccountCloudRuleState] | None | Unset, data)

        failed_adds = _parse_failed_adds(d.pop("failed_adds", UNSET))


        def _parse_failed_removes(data: object) -> list[AccountWebhookDeleteState] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                failed_removes_type_0 = []
                _failed_removes_type_0 = data
                for failed_removes_type_0_item_data in (_failed_removes_type_0):
                    failed_removes_type_0_item = AccountWebhookDeleteState.from_dict(failed_removes_type_0_item_data)



                    failed_removes_type_0.append(failed_removes_type_0_item)

                return failed_removes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AccountWebhookDeleteState] | None | Unset, data)

        failed_removes = _parse_failed_removes(d.pop("failed_removes", UNSET))


        reattempts_needed = cls(
            failed_adds=failed_adds,
            failed_removes=failed_removes,
        )


        reattempts_needed.additional_properties = d
        return reattempts_needed

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
