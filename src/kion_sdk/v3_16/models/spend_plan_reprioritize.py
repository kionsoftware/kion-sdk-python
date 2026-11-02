from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SpendPlanReprioritize")



@_attrs_define
class SpendPlanReprioritize:
    """ SpendPlanReprioritize defines a list of funding source IDs for reprioritizing a spend plan.

        Attributes:
            new_order (list[int] | None | Unset):
     """

    new_order: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        new_order: list[int] | None | Unset
        if isinstance(self.new_order, Unset):
            new_order = UNSET
        elif isinstance(self.new_order, list):
            new_order = self.new_order


        else:
            new_order = self.new_order


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if new_order is not UNSET:
            field_dict["new-order"] = new_order

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_new_order(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                new_order_type_0 = cast(list[int], data)

                return new_order_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        new_order = _parse_new_order(d.pop("new-order", UNSET))


        spend_plan_reprioritize = cls(
            new_order=new_order,
        )


        spend_plan_reprioritize.additional_properties = d
        return spend_plan_reprioritize

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
