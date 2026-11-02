from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.budget_create import BudgetCreate





T = TypeVar("T", bound="ProjectCreateWithBudgets")



@_attrs_define
class ProjectCreateWithBudgets:
    """ ProjectCreateWithBudgets defines a project creation.

        Attributes:
            name (str): Name of the Project in the application. Example: Tech Project 1.
            ou_id (int | None): ID of the OU containing the project. Example: 1.
            permission_scheme_id (int | None): ID of the permission scheme applied to the project. Example: 3.
            auto_pay (bool | None | Unset): True means the application can use the spend plan to process payments from
                the account. Should be true unless using a custom module. Example: True.
            budget (list[BudgetCreate] | None | Unset):
            default_aws_region (str | Unset): Default AWS region that the project will use for assuming into accounts.
                Example: us-east-1.
            description (str | Unset): Description for the project in the application. Example: Project being used to test
                cloud migration..
            owner_user_group_ids (list[int] | None | Unset): List of groups IDs who will own the project. Is required if no
                owner user IDs are listed. Example: [1, 2].
            owner_user_ids (list[int] | None | Unset): List of user IDs who will own the project. Is required if no owner
                group IDs are listed. Example: [1, 2].
     """

    name: str
    ou_id: int | None
    permission_scheme_id: int | None
    auto_pay: bool | None | Unset = UNSET
    budget: list[BudgetCreate] | None | Unset = UNSET
    default_aws_region: str | Unset = UNSET
    description: str | Unset = UNSET
    owner_user_group_ids: list[int] | None | Unset = UNSET
    owner_user_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.budget_create import BudgetCreate
        name = self.name

        ou_id: int | None
        ou_id = self.ou_id

        permission_scheme_id: int | None
        permission_scheme_id = self.permission_scheme_id

        auto_pay: bool | None | Unset
        if isinstance(self.auto_pay, Unset):
            auto_pay = UNSET
        else:
            auto_pay = self.auto_pay

        budget: list[dict[str, Any]] | None | Unset
        if isinstance(self.budget, Unset):
            budget = UNSET
        elif isinstance(self.budget, list):
            budget = []
            for budget_type_0_item_data in self.budget:
                budget_type_0_item = budget_type_0_item_data.to_dict()
                budget.append(budget_type_0_item)


        else:
            budget = self.budget

        default_aws_region = self.default_aws_region

        description = self.description

        owner_user_group_ids: list[int] | None | Unset
        if isinstance(self.owner_user_group_ids, Unset):
            owner_user_group_ids = UNSET
        elif isinstance(self.owner_user_group_ids, list):
            owner_user_group_ids = self.owner_user_group_ids


        else:
            owner_user_group_ids = self.owner_user_group_ids

        owner_user_ids: list[int] | None | Unset
        if isinstance(self.owner_user_ids, Unset):
            owner_user_ids = UNSET
        elif isinstance(self.owner_user_ids, list):
            owner_user_ids = self.owner_user_ids


        else:
            owner_user_ids = self.owner_user_ids


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "ou_id": ou_id,
            "permission_scheme_id": permission_scheme_id,
        })
        if auto_pay is not UNSET:
            field_dict["auto_pay"] = auto_pay
        if budget is not UNSET:
            field_dict["budget"] = budget
        if default_aws_region is not UNSET:
            field_dict["default_aws_region"] = default_aws_region
        if description is not UNSET:
            field_dict["description"] = description
        if owner_user_group_ids is not UNSET:
            field_dict["owner_user_group_ids"] = owner_user_group_ids
        if owner_user_ids is not UNSET:
            field_dict["owner_user_ids"] = owner_user_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_create import BudgetCreate
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_ou_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        ou_id = _parse_ou_id(d.pop("ou_id"))


        def _parse_permission_scheme_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        permission_scheme_id = _parse_permission_scheme_id(d.pop("permission_scheme_id"))


        def _parse_auto_pay(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_pay = _parse_auto_pay(d.pop("auto_pay", UNSET))


        def _parse_budget(data: object) -> list[BudgetCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                budget_type_0 = []
                _budget_type_0 = data
                for budget_type_0_item_data in (_budget_type_0):
                    budget_type_0_item = BudgetCreate.from_dict(budget_type_0_item_data)



                    budget_type_0.append(budget_type_0_item)

                return budget_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BudgetCreate] | None | Unset, data)

        budget = _parse_budget(d.pop("budget", UNSET))


        default_aws_region = d.pop("default_aws_region", UNSET)

        description = d.pop("description", UNSET)

        def _parse_owner_user_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_group_ids_type_0 = cast(list[int], data)

                return owner_user_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_group_ids = _parse_owner_user_group_ids(d.pop("owner_user_group_ids", UNSET))


        def _parse_owner_user_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                owner_user_ids_type_0 = cast(list[int], data)

                return owner_user_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        owner_user_ids = _parse_owner_user_ids(d.pop("owner_user_ids", UNSET))


        project_create_with_budgets = cls(
            name=name,
            ou_id=ou_id,
            permission_scheme_id=permission_scheme_id,
            auto_pay=auto_pay,
            budget=budget,
            default_aws_region=default_aws_region,
            description=description,
            owner_user_group_ids=owner_user_group_ids,
            owner_user_ids=owner_user_ids,
        )


        project_create_with_budgets.additional_properties = d
        return project_create_with_budgets

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
