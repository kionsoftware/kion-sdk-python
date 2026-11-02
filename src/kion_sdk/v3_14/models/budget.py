from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.budget_config import BudgetConfig
  from ..models.budget_data import BudgetData





T = TypeVar("T", bound="Budget")



@_attrs_define
class Budget:
    """ Budget holds the configuration and data entries for a budget.

        Attributes:
            config (BudgetConfig | Unset): BudgetConfig defines a budget configuration.
            data (list[BudgetData] | None | Unset):
     """

    config: BudgetConfig | Unset = UNSET
    data: list[BudgetData] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.budget_config import BudgetConfig
        from ..models.budget_data import BudgetData
        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        data: list[dict[str, Any]] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)


        else:
            data = self.data


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if config is not UNSET:
            field_dict["config"] = config
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.budget_config import BudgetConfig
        from ..models.budget_data import BudgetData
        d = dict(src_dict)
        _config = d.pop("config", UNSET)
        config: BudgetConfig | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = BudgetConfig.from_dict(_config)




        def _parse_data(data: object) -> list[BudgetData] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in (_data_type_0):
                    data_type_0_item = BudgetData.from_dict(data_type_0_item_data)



                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BudgetData] | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))


        budget = cls(
            config=config,
            data=data,
        )


        budget.additional_properties = d
        return budget

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
