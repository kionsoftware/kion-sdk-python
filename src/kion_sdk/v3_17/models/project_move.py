from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.project_funding import ProjectFunding





T = TypeVar("T", bound="ProjectMove")



@_attrs_define
class ProjectMove:
    """ ProjectMove defines a project move operation.

        Attributes:
            cloud_rule_setting (str): How to handle existing cloud rules when moving a project.
                One of:
                convert - Convert cloud rules to the destination OU
                remove - Remove cloud rules from the project Example: convert.
            destination_ou_id (int | None): The ID of the OU to move the project to. Example: 5.
            financial_setting (str): How to handle existing financial data when moving a project.
                One of:
                preserve - Preserve financial history on the current OU
                move - Move financial history to the new OU Example: move.
            spend_plan_setting (str): How to handle existing project budgets when moving a project.
                One of:
                keep - Move all past, current, and future budgets with the project
                create - Create a new budget; existing budgets will not carry over Example: keep.
            project_funding (list[ProjectFunding] | None | Unset): Optional project funding configuration for the move.
                Each entry defines a funding source allocation with amount and date range.
     """

    cloud_rule_setting: str
    destination_ou_id: int | None
    financial_setting: str
    spend_plan_setting: str
    project_funding: list[ProjectFunding] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.project_funding import ProjectFunding
        cloud_rule_setting = self.cloud_rule_setting

        destination_ou_id: int | None
        destination_ou_id = self.destination_ou_id

        financial_setting = self.financial_setting

        spend_plan_setting = self.spend_plan_setting

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cloud_rule_setting": cloud_rule_setting,
            "destination_ou_id": destination_ou_id,
            "financial_setting": financial_setting,
            "spend_plan_setting": spend_plan_setting,
        })
        if project_funding is not UNSET:
            field_dict["project_funding"] = project_funding

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_funding import ProjectFunding
        d = dict(src_dict)
        cloud_rule_setting = d.pop("cloud_rule_setting")

        def _parse_destination_ou_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        destination_ou_id = _parse_destination_ou_id(d.pop("destination_ou_id"))


        financial_setting = d.pop("financial_setting")

        spend_plan_setting = d.pop("spend_plan_setting")

        def _parse_project_funding(data: object) -> list[ProjectFunding] | None | Unset:
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
                    project_funding_type_0_item = ProjectFunding.from_dict(project_funding_type_0_item_data)



                    project_funding_type_0.append(project_funding_type_0_item)

                return project_funding_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProjectFunding] | None | Unset, data)

        project_funding = _parse_project_funding(d.pop("project_funding", UNSET))


        project_move = cls(
            cloud_rule_setting=cloud_rule_setting,
            destination_ou_id=destination_ou_id,
            financial_setting=financial_setting,
            spend_plan_setting=spend_plan_setting,
            project_funding=project_funding,
        )


        project_move.additional_properties = d
        return project_move

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
