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
  from ..models.custom_billing_source_azure_connection import CustomBillingSourceAzureConnection





T = TypeVar("T", bound="CustomBillingSourceTestRequest")



@_attrs_define
class CustomBillingSourceTestRequest:
    """ CustomBillingSourceTestRequest defines a request to test a custom billing source.

        Attributes:
            aws_connection (CustomBillingSourceAWSConnection | Unset):
            azure_connection (CustomBillingSourceAzureConnection | Unset): CustomBillingSourceAzureConnection defines the
                Azure storage connection for a custom
                billing source. Provide either credentialed_billing_source_id (reuse an existing Azure
                billing source's tenant credentials) or the tenant credential fields, not both.
            billing_source_id (int | None | Unset): ID of an existing billing source. Provide to test a saved custom billing
                source using its stored credentials. Example: 254.
            billing_start_date (str | Unset): Start date of billing source (YYYY-MM). Example: 2019-01.
            name (str | Unset): Name of the billing source. Example: My Master Payer.
     """

    aws_connection: CustomBillingSourceAWSConnection | Unset = UNSET
    azure_connection: CustomBillingSourceAzureConnection | Unset = UNSET
    billing_source_id: int | None | Unset = UNSET
    billing_start_date: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.custom_billing_source_aws_connection import CustomBillingSourceAWSConnection
        from ..models.custom_billing_source_azure_connection import CustomBillingSourceAzureConnection
        aws_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_connection, Unset):
            aws_connection = self.aws_connection.to_dict()

        azure_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_connection, Unset):
            azure_connection = self.azure_connection.to_dict()

        billing_source_id: int | None | Unset
        if isinstance(self.billing_source_id, Unset):
            billing_source_id = UNSET
        else:
            billing_source_id = self.billing_source_id

        billing_start_date = self.billing_start_date

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aws_connection is not UNSET:
            field_dict["aws_connection"] = aws_connection
        if azure_connection is not UNSET:
            field_dict["azure_connection"] = azure_connection
        if billing_source_id is not UNSET:
            field_dict["billing_source_id"] = billing_source_id
        if billing_start_date is not UNSET:
            field_dict["billing_start_date"] = billing_start_date
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_billing_source_aws_connection import CustomBillingSourceAWSConnection
        from ..models.custom_billing_source_azure_connection import CustomBillingSourceAzureConnection
        d = dict(src_dict)
        _aws_connection = d.pop("aws_connection", UNSET)
        aws_connection: CustomBillingSourceAWSConnection | Unset
        if isinstance(_aws_connection,  Unset):
            aws_connection = UNSET
        else:
            aws_connection = CustomBillingSourceAWSConnection.from_dict(_aws_connection)




        _azure_connection = d.pop("azure_connection", UNSET)
        azure_connection: CustomBillingSourceAzureConnection | Unset
        if isinstance(_azure_connection,  Unset):
            azure_connection = UNSET
        else:
            azure_connection = CustomBillingSourceAzureConnection.from_dict(_azure_connection)




        def _parse_billing_source_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        billing_source_id = _parse_billing_source_id(d.pop("billing_source_id", UNSET))


        billing_start_date = d.pop("billing_start_date", UNSET)

        name = d.pop("name", UNSET)

        custom_billing_source_test_request = cls(
            aws_connection=aws_connection,
            azure_connection=azure_connection,
            billing_source_id=billing_source_id,
            billing_start_date=billing_start_date,
            name=name,
        )


        custom_billing_source_test_request.additional_properties = d
        return custom_billing_source_test_request

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
