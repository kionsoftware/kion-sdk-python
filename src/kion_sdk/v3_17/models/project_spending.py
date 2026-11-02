from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ProjectSpending")



@_attrs_define
class ProjectSpending:
    """ ProjectSpending defines the spend for a project.

        Attributes:
            credit (float | Unset): Amount of spend covered by cloid provider credits. Use of `credits` is deprecated, use
                `credit` instead.
            credits_ (float | Unset):
            end_datecode (str | Unset): The last date of the reported spending (YYYY-MM). Example: 2019-01.
            lapsed_datecode (str | Unset): The first date of spending not covered by a funding source (YYYY-MM).
                An empty string means there is no lapsed funding. Example: 2019-01.
            planned (float | Unset): Amount added to the project's spend plan.
            previous_month_spend (float | Unset): The amount of money spent in cloud prviders during the previous month. Use
                of `previous_month_spent` is deprecated, use `previous_month_spend`
            previous_month_spent (float | Unset):
            spend (float | Unset): The amount of money spent in cloud prviders.
            start_datecode (str | Unset): The first date of the reported spending (YYYY-MM). Example: 2019-01.
            time_percentage (float | Unset): Percentage the current time is between the start date and end date.
     """

    credit: float | Unset = UNSET
    credits_: float | Unset = UNSET
    end_datecode: str | Unset = UNSET
    lapsed_datecode: str | Unset = UNSET
    planned: float | Unset = UNSET
    previous_month_spend: float | Unset = UNSET
    previous_month_spent: float | Unset = UNSET
    spend: float | Unset = UNSET
    start_datecode: str | Unset = UNSET
    time_percentage: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        credit = self.credit

        credits_ = self.credits_

        end_datecode = self.end_datecode

        lapsed_datecode = self.lapsed_datecode

        planned = self.planned

        previous_month_spend = self.previous_month_spend

        previous_month_spent = self.previous_month_spent

        spend = self.spend

        start_datecode = self.start_datecode

        time_percentage = self.time_percentage


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if credit is not UNSET:
            field_dict["credit"] = credit
        if credits_ is not UNSET:
            field_dict["credits"] = credits_
        if end_datecode is not UNSET:
            field_dict["end_datecode"] = end_datecode
        if lapsed_datecode is not UNSET:
            field_dict["lapsed_datecode"] = lapsed_datecode
        if planned is not UNSET:
            field_dict["planned"] = planned
        if previous_month_spend is not UNSET:
            field_dict["previous_month_spend"] = previous_month_spend
        if previous_month_spent is not UNSET:
            field_dict["previous_month_spent"] = previous_month_spent
        if spend is not UNSET:
            field_dict["spend"] = spend
        if start_datecode is not UNSET:
            field_dict["start_datecode"] = start_datecode
        if time_percentage is not UNSET:
            field_dict["time_percentage"] = time_percentage

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credit = d.pop("credit", UNSET)

        credits_ = d.pop("credits", UNSET)

        end_datecode = d.pop("end_datecode", UNSET)

        lapsed_datecode = d.pop("lapsed_datecode", UNSET)

        planned = d.pop("planned", UNSET)

        previous_month_spend = d.pop("previous_month_spend", UNSET)

        previous_month_spent = d.pop("previous_month_spent", UNSET)

        spend = d.pop("spend", UNSET)

        start_datecode = d.pop("start_datecode", UNSET)

        time_percentage = d.pop("time_percentage", UNSET)

        project_spending = cls(
            credit=credit,
            credits_=credits_,
            end_datecode=end_datecode,
            lapsed_datecode=lapsed_datecode,
            planned=planned,
            previous_month_spend=previous_month_spend,
            previous_month_spent=previous_month_spent,
            spend=spend,
            start_datecode=start_datecode,
            time_percentage=time_percentage,
        )


        project_spending.additional_properties = d
        return project_spending

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
