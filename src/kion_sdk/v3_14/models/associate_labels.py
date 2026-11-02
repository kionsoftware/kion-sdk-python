from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.associate_label import AssociateLabel





T = TypeVar("T", bound="AssociateLabels")



@_attrs_define
class AssociateLabels:
    """ 
        Attributes:
            labels (list[AssociateLabel] | None | Unset):
     """

    labels: list[AssociateLabel] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.associate_label import AssociateLabel
        labels: list[dict[str, Any]] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, list):
            labels = []
            for labels_type_0_item_data in self.labels:
                labels_type_0_item = labels_type_0_item_data.to_dict()
                labels.append(labels_type_0_item)


        else:
            labels = self.labels


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.associate_label import AssociateLabel
        d = dict(src_dict)
        def _parse_labels(data: object) -> list[AssociateLabel] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                labels_type_0 = []
                _labels_type_0 = data
                for labels_type_0_item_data in (_labels_type_0):
                    labels_type_0_item = AssociateLabel.from_dict(labels_type_0_item_data)



                    labels_type_0.append(labels_type_0_item)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AssociateLabel] | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))


        associate_labels = cls(
            labels=labels,
        )


        associate_labels.additional_properties = d
        return associate_labels

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
