from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.spend_plan_v4_put import SpendPlanV4Put





T = TypeVar("T", bound="SpendPlanV4PutList")



@_attrs_define
class SpendPlanV4PutList:
    """ SpendPlanV4PutList defines a full update for a spend plan.

        Attributes:
            spend_plan (list[SpendPlanV4Put] | None | Unset):
     """

    spend_plan: list[SpendPlanV4Put] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.spend_plan_v4_put import SpendPlanV4Put
        spend_plan: list[dict[str, Any]] | None | Unset
        if isinstance(self.spend_plan, Unset):
            spend_plan = UNSET
        elif isinstance(self.spend_plan, list):
            spend_plan = []
            for spend_plan_type_0_item_data in self.spend_plan:
                spend_plan_type_0_item = spend_plan_type_0_item_data.to_dict()
                spend_plan.append(spend_plan_type_0_item)


        else:
            spend_plan = self.spend_plan


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if spend_plan is not UNSET:
            field_dict["spend-plan"] = spend_plan

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spend_plan_v4_put import SpendPlanV4Put
        d = dict(src_dict)
        def _parse_spend_plan(data: object) -> list[SpendPlanV4Put] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                spend_plan_type_0 = []
                _spend_plan_type_0 = data
                for spend_plan_type_0_item_data in (_spend_plan_type_0):
                    spend_plan_type_0_item = SpendPlanV4Put.from_dict(spend_plan_type_0_item_data)



                    spend_plan_type_0.append(spend_plan_type_0_item)

                return spend_plan_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SpendPlanV4Put] | None | Unset, data)

        spend_plan = _parse_spend_plan(d.pop("spend-plan", UNSET))


        spend_plan_v4_put_list = cls(
            spend_plan=spend_plan,
        )


        spend_plan_v4_put_list.additional_properties = d
        return spend_plan_v4_put_list

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
