from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.fs_project_funding import FSProjectFunding





T = TypeVar("T", bound="FSProjectFundingWithTotals")



@_attrs_define
class FSProjectFundingWithTotals:
    """ FSProjectFundingWithTotals defines the funding for a project with total planned & total spent.

        Attributes:
            project_funding (list[FSProjectFunding] | None | Unset): A list of project fundings
            total_planned (float | Unset): The total amount of money already planned for the project's funding sources.
            total_remaining (float | Unset): The total amount of money remaining for the project to use from its funding
                sources.
            total_spent (float | Unset): The total amount of money spent on the project from its funding sources.
     """

    project_funding: list[FSProjectFunding] | None | Unset = UNSET
    total_planned: float | Unset = UNSET
    total_remaining: float | Unset = UNSET
    total_spent: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.fs_project_funding import FSProjectFunding
        project_funding: list[dict[str, Any]] | None | Unset
        if isinstance(self.project_funding, Unset):
            project_funding = UNSET
        elif isinstance(self.project_funding, list):
            project_funding = []
            for project_funding_type_0_item_data in self.project_funding:
                project_funding_type_0_item = project_funding_type_0_item_data.to_dict()
                project_funding.append(project_funding_type_0_item)


        else:
            project_funding = self.project_funding

        total_planned = self.total_planned

        total_remaining = self.total_remaining

        total_spent = self.total_spent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if project_funding is not UNSET:
            field_dict["project_funding"] = project_funding
        if total_planned is not UNSET:
            field_dict["total_planned"] = total_planned
        if total_remaining is not UNSET:
            field_dict["total_remaining"] = total_remaining
        if total_spent is not UNSET:
            field_dict["total_spent"] = total_spent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fs_project_funding import FSProjectFunding
        d = dict(src_dict)
        def _parse_project_funding(data: object) -> list[FSProjectFunding] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                project_funding_type_0 = []
                _project_funding_type_0 = data
                for project_funding_type_0_item_data in (_project_funding_type_0):
                    project_funding_type_0_item = FSProjectFunding.from_dict(project_funding_type_0_item_data)



                    project_funding_type_0.append(project_funding_type_0_item)

                return project_funding_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FSProjectFunding] | None | Unset, data)

        project_funding = _parse_project_funding(d.pop("project_funding", UNSET))


        total_planned = d.pop("total_planned", UNSET)

        total_remaining = d.pop("total_remaining", UNSET)

        total_spent = d.pop("total_spent", UNSET)

        fs_project_funding_with_totals = cls(
            project_funding=project_funding,
            total_planned=total_planned,
            total_remaining=total_remaining,
            total_spent=total_spent,
        )


        fs_project_funding_with_totals.additional_properties = d
        return fs_project_funding_with_totals

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
