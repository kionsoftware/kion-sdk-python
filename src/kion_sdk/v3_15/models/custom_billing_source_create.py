from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.custom_billing_source_aws_connection import CustomBillingSourceAWSConnection





T = TypeVar("T", bound="CustomBillingSourceCreate")



@_attrs_define
class CustomBillingSourceCreate:
    """ 
        Attributes:
            aws_connection (CustomBillingSourceAWSConnection | Unset):
            billing_start_date (str | Unset): Start date of billing source (YYYY-MM). Example: 2019-01.
            id (int | Unset): ID of the billing source. Example: 254.
            name (str | Unset): Name of the billing source. Example: My Master Payer.
            skip_validation (bool | None | Unset): When true, will skip validating the connection to defined bucket.
     """

    aws_connection: CustomBillingSourceAWSConnection | Unset = UNSET
    billing_start_date: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    skip_validation: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_billing_source_aws_connection import CustomBillingSourceAWSConnection
        aws_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_connection, Unset):
            aws_connection = self.aws_connection.to_dict()

        billing_start_date = self.billing_start_date

        id = self.id

        name = self.name

        skip_validation: bool | None | Unset
        if isinstance(self.skip_validation, Unset):
            skip_validation = UNSET
        else:
            skip_validation = self.skip_validation


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aws_connection is not UNSET:
            field_dict["aws_connection"] = aws_connection
        if billing_start_date is not UNSET:
            field_dict["billing_start_date"] = billing_start_date
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if skip_validation is not UNSET:
            field_dict["skip_validation"] = skip_validation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_billing_source_aws_connection import CustomBillingSourceAWSConnection
        d = dict(src_dict)
        _aws_connection = d.pop("aws_connection", UNSET)
        aws_connection: CustomBillingSourceAWSConnection | Unset
        if isinstance(_aws_connection,  Unset):
            aws_connection = UNSET
        else:
            aws_connection = CustomBillingSourceAWSConnection.from_dict(_aws_connection)




        billing_start_date = d.pop("billing_start_date", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_skip_validation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        skip_validation = _parse_skip_validation(d.pop("skip_validation", UNSET))


        custom_billing_source_create = cls(
            aws_connection=aws_connection,
            billing_start_date=billing_start_date,
            id=id,
            name=name,
            skip_validation=skip_validation,
        )


        custom_billing_source_create.additional_properties = d
        return custom_billing_source_create

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
