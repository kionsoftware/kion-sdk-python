from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.criteria_item import CriteriaItem





T = TypeVar("T", bound="BillingRuleCriteria")



@_attrs_define
class BillingRuleCriteria:
    """ 
        Attributes:
            payers (list[CriteriaItem] | None | Unset):
     """

    payers: list[CriteriaItem] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.criteria_item import CriteriaItem
        payers: list[dict[str, Any]] | None | Unset
        if isinstance(self.payers, Unset):
            payers = UNSET
        elif isinstance(self.payers, list):
            payers = []
            for payers_type_0_item_data in self.payers:
                payers_type_0_item = payers_type_0_item_data.to_dict()
                payers.append(payers_type_0_item)


        else:
            payers = self.payers


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if payers is not UNSET:
            field_dict["payers"] = payers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criteria_item import CriteriaItem
        d = dict(src_dict)
        def _parse_payers(data: object) -> list[CriteriaItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                payers_type_0 = []
                _payers_type_0 = data
                for payers_type_0_item_data in (_payers_type_0):
                    payers_type_0_item = CriteriaItem.from_dict(payers_type_0_item_data)



                    payers_type_0.append(payers_type_0_item)

                return payers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CriteriaItem] | None | Unset, data)

        payers = _parse_payers(d.pop("payers", UNSET))


        billing_rule_criteria = cls(
            payers=payers,
        )


        billing_rule_criteria.additional_properties = d
        return billing_rule_criteria

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
