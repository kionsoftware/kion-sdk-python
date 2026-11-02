from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.billing_rule_destination import BillingRuleDestination





T = TypeVar("T", bound="AllocationRuleDefinition")



@_attrs_define
class AllocationRuleDefinition:
    """ 
        Attributes:
            criteria (Any): The criteria for the allocation rule, stored as raw JSON. Example: {'account_id': 1, 'tag':
                'repo:Prod'}.
            destinations (list[BillingRuleDestination] | None): The destination list for which scopes should be added to
                this billing rule.
                It can include a list of scope IDs or a list of OU or Project IDs, from which all descendent scopes are
                included.
                Project and OU ID lists can also include scope IDs to be excluded from the descendent scope list.
            distribution_type_id (int | None): The value of the distribution type for an allocation rule. The allowed values
                are:

                1 - Even Distribution
                2 - Proportional (to spend) Distribution
                3 - Percentage-based Distribution Example: 1.
            proportion_basis (str | Unset): The basis used to compute proportions when DistributionTypeID is 2
                (Proportional).
                Allowed values: "scope", "parent_project".

                "scope": share is proportional to each destination scope's own spend
                "parent_project": share is proportional to spend on each destination scope's parent project

                Required only when DistributionTypeID is 2; ignored otherwise. Example: scope.
     """

    criteria: Any
    destinations: list[BillingRuleDestination] | None
    distribution_type_id: int | None
    proportion_basis: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.billing_rule_destination import BillingRuleDestination
        criteria = self.criteria

        destinations: list[dict[str, Any]] | None
        if isinstance(self.destinations, list):
            destinations = []
            for destinations_type_0_item_data in self.destinations:
                destinations_type_0_item = destinations_type_0_item_data.to_dict()
                destinations.append(destinations_type_0_item)


        else:
            destinations = self.destinations

        distribution_type_id: int | None
        distribution_type_id = self.distribution_type_id

        proportion_basis = self.proportion_basis


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "criteria": criteria,
            "destinations": destinations,
            "distribution_type_id": distribution_type_id,
        })
        if proportion_basis is not UNSET:
            field_dict["proportion_basis"] = proportion_basis

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.billing_rule_destination import BillingRuleDestination
        d = dict(src_dict)
        criteria = d.pop("criteria")

        def _parse_destinations(data: object) -> list[BillingRuleDestination] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                destinations_type_0 = []
                _destinations_type_0 = data
                for destinations_type_0_item_data in (_destinations_type_0):
                    destinations_type_0_item = BillingRuleDestination.from_dict(destinations_type_0_item_data)



                    destinations_type_0.append(destinations_type_0_item)

                return destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BillingRuleDestination] | None, data)

        destinations = _parse_destinations(d.pop("destinations"))


        def _parse_distribution_type_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        distribution_type_id = _parse_distribution_type_id(d.pop("distribution_type_id"))


        proportion_basis = d.pop("proportion_basis", UNSET)

        allocation_rule_definition = cls(
            criteria=criteria,
            destinations=destinations,
            distribution_type_id=distribution_type_id,
            proportion_basis=proportion_basis,
        )


        allocation_rule_definition.additional_properties = d
        return allocation_rule_definition

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
