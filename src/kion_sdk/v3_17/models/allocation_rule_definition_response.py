from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.allocation_rule_definition_response_criteria import AllocationRuleDefinitionResponseCriteria
  from ..models.billing_rule_destination_response import BillingRuleDestinationResponse





T = TypeVar("T", bound="AllocationRuleDefinitionResponse")



@_attrs_define
class AllocationRuleDefinitionResponse:
    """ AllocationRuleDefinitionResponse is the public read shape of an allocation-rule definition.

        Attributes:
            criteria (AllocationRuleDefinitionResponseCriteria | Unset):
            destinations (list[BillingRuleDestinationResponse] | None | Unset):
            distribution_type_id (int | None | Unset):
            proportion_basis (str | Unset):
     """

    criteria: AllocationRuleDefinitionResponseCriteria | Unset = UNSET
    destinations: list[BillingRuleDestinationResponse] | None | Unset = UNSET
    distribution_type_id: int | None | Unset = UNSET
    proportion_basis: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.allocation_rule_definition_response_criteria import AllocationRuleDefinitionResponseCriteria
        from ..models.billing_rule_destination_response import BillingRuleDestinationResponse
        criteria: dict[str, Any] | Unset = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.to_dict()

        destinations: list[dict[str, Any]] | None | Unset
        if isinstance(self.destinations, Unset):
            destinations = UNSET
        elif isinstance(self.destinations, list):
            destinations = []
            for destinations_type_0_item_data in self.destinations:
                destinations_type_0_item = destinations_type_0_item_data.to_dict()
                destinations.append(destinations_type_0_item)


        else:
            destinations = self.destinations

        distribution_type_id: int | None | Unset
        if isinstance(self.distribution_type_id, Unset):
            distribution_type_id = UNSET
        else:
            distribution_type_id = self.distribution_type_id

        proportion_basis = self.proportion_basis


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if destinations is not UNSET:
            field_dict["destinations"] = destinations
        if distribution_type_id is not UNSET:
            field_dict["distribution_type_id"] = distribution_type_id
        if proportion_basis is not UNSET:
            field_dict["proportion_basis"] = proportion_basis

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allocation_rule_definition_response_criteria import AllocationRuleDefinitionResponseCriteria
        from ..models.billing_rule_destination_response import BillingRuleDestinationResponse
        d = dict(src_dict)
        _criteria = d.pop("criteria", UNSET)
        criteria: AllocationRuleDefinitionResponseCriteria | Unset
        if isinstance(_criteria,  Unset):
            criteria = UNSET
        else:
            criteria = AllocationRuleDefinitionResponseCriteria.from_dict(_criteria)




        def _parse_destinations(data: object) -> list[BillingRuleDestinationResponse] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                destinations_type_0 = []
                _destinations_type_0 = data
                for destinations_type_0_item_data in (_destinations_type_0):
                    destinations_type_0_item = BillingRuleDestinationResponse.from_dict(destinations_type_0_item_data)



                    destinations_type_0.append(destinations_type_0_item)

                return destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BillingRuleDestinationResponse] | None | Unset, data)

        destinations = _parse_destinations(d.pop("destinations", UNSET))


        def _parse_distribution_type_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        distribution_type_id = _parse_distribution_type_id(d.pop("distribution_type_id", UNSET))


        proportion_basis = d.pop("proportion_basis", UNSET)

        allocation_rule_definition_response = cls(
            criteria=criteria,
            destinations=destinations,
            distribution_type_id=distribution_type_id,
            proportion_basis=proportion_basis,
        )


        allocation_rule_definition_response.additional_properties = d
        return allocation_rule_definition_response

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
