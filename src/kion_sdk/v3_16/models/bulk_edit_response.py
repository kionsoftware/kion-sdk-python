from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.errored_custom_line_item import ErroredCustomLineItem





T = TypeVar("T", bound="BulkEditResponse")



@_attrs_define
class BulkEditResponse:
    """ BulkEditResponse is the response for bulk upload

        Attributes:
            errored (list[ErroredCustomLineItem] | None | Unset):
     """

    errored: list[ErroredCustomLineItem] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.errored_custom_line_item import ErroredCustomLineItem
        errored: list[dict[str, Any]] | None | Unset
        if isinstance(self.errored, Unset):
            errored = UNSET
        elif isinstance(self.errored, list):
            errored = []
            for errored_type_0_item_data in self.errored:
                errored_type_0_item = errored_type_0_item_data.to_dict()
                errored.append(errored_type_0_item)


        else:
            errored = self.errored


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if errored is not UNSET:
            field_dict["errored"] = errored

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.errored_custom_line_item import ErroredCustomLineItem
        d = dict(src_dict)
        def _parse_errored(data: object) -> list[ErroredCustomLineItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errored_type_0 = []
                _errored_type_0 = data
                for errored_type_0_item_data in (_errored_type_0):
                    errored_type_0_item = ErroredCustomLineItem.from_dict(errored_type_0_item_data)



                    errored_type_0.append(errored_type_0_item)

                return errored_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ErroredCustomLineItem] | None | Unset, data)

        errored = _parse_errored(d.pop("errored", UNSET))


        bulk_edit_response = cls(
            errored=errored,
        )


        bulk_edit_response.additional_properties = d
        return bulk_edit_response

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
