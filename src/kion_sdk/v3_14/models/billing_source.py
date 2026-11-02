from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.aws_payer import AWSPayer
  from ..models.azure_payer import AzurePayer
  from ..models.custom_billing_source import CustomBillingSource
  from ..models.gcp_billing_account_augmented import GCPBillingAccountAugmented
  from ..models.oci_billing_source import OCIBillingSource





T = TypeVar("T", bound="BillingSource")



@_attrs_define
class BillingSource:
    """ BillingSource defines the contents of a billing source.

        Attributes:
            account_creation (bool | None | Unset): When true, cloudtamer is able to create accounts on this payer. Example:
                True.
            aws_payer (AWSPayer | Unset): AWSPayer defines the contents of an AWS payer.
            azure_payer (AzurePayer | Unset): AzurePayer defines the contents of an Azure payer.
            custom_billing_source (CustomBillingSource | Unset): CustomBillingSource defines a custom billing source.
            gcp_payer (GCPBillingAccountAugmented | Unset): GCPBillingAccountAugmented contains information about retrieving
                billing data from GCP
            id (int | Unset): ID of the record in the application. Example: 1.
            oci_payer (OCIBillingSource | Unset): OCIBillingSource defines a billing source used for testing and creation.
            use_focus_reports (bool | None | Unset): true if billing source is configured to read FOCUS reports Example:
                True.
            use_proprietary_reports (bool | None | Unset): true if billing source is configured to read proprietary billing
                reports from the CSP
                (CUR, DBRRT, Azure Export Reports, Google Cloud Billing Export, Oracle Cost Report) Example: True.
     """

    account_creation: bool | None | Unset = UNSET
    aws_payer: AWSPayer | Unset = UNSET
    azure_payer: AzurePayer | Unset = UNSET
    custom_billing_source: CustomBillingSource | Unset = UNSET
    gcp_payer: GCPBillingAccountAugmented | Unset = UNSET
    id: int | Unset = UNSET
    oci_payer: OCIBillingSource | Unset = UNSET
    use_focus_reports: bool | None | Unset = UNSET
    use_proprietary_reports: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.aws_payer import AWSPayer
        from ..models.azure_payer import AzurePayer
        from ..models.custom_billing_source import CustomBillingSource
        from ..models.gcp_billing_account_augmented import GCPBillingAccountAugmented
        from ..models.oci_billing_source import OCIBillingSource
        account_creation: bool | None | Unset
        if isinstance(self.account_creation, Unset):
            account_creation = UNSET
        else:
            account_creation = self.account_creation

        aws_payer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.aws_payer, Unset):
            aws_payer = self.aws_payer.to_dict()

        azure_payer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.azure_payer, Unset):
            azure_payer = self.azure_payer.to_dict()

        custom_billing_source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_billing_source, Unset):
            custom_billing_source = self.custom_billing_source.to_dict()

        gcp_payer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.gcp_payer, Unset):
            gcp_payer = self.gcp_payer.to_dict()

        id = self.id

        oci_payer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.oci_payer, Unset):
            oci_payer = self.oci_payer.to_dict()

        use_focus_reports: bool | None | Unset
        if isinstance(self.use_focus_reports, Unset):
            use_focus_reports = UNSET
        else:
            use_focus_reports = self.use_focus_reports

        use_proprietary_reports: bool | None | Unset
        if isinstance(self.use_proprietary_reports, Unset):
            use_proprietary_reports = UNSET
        else:
            use_proprietary_reports = self.use_proprietary_reports


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_creation is not UNSET:
            field_dict["account_creation"] = account_creation
        if aws_payer is not UNSET:
            field_dict["aws_payer"] = aws_payer
        if azure_payer is not UNSET:
            field_dict["azure_payer"] = azure_payer
        if custom_billing_source is not UNSET:
            field_dict["custom_billing_source"] = custom_billing_source
        if gcp_payer is not UNSET:
            field_dict["gcp_payer"] = gcp_payer
        if id is not UNSET:
            field_dict["id"] = id
        if oci_payer is not UNSET:
            field_dict["oci_payer"] = oci_payer
        if use_focus_reports is not UNSET:
            field_dict["use_focus_reports"] = use_focus_reports
        if use_proprietary_reports is not UNSET:
            field_dict["use_proprietary_reports"] = use_proprietary_reports

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.aws_payer import AWSPayer
        from ..models.azure_payer import AzurePayer
        from ..models.custom_billing_source import CustomBillingSource
        from ..models.gcp_billing_account_augmented import GCPBillingAccountAugmented
        from ..models.oci_billing_source import OCIBillingSource
        d = dict(src_dict)
        def _parse_account_creation(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        account_creation = _parse_account_creation(d.pop("account_creation", UNSET))


        _aws_payer = d.pop("aws_payer", UNSET)
        aws_payer: AWSPayer | Unset
        if isinstance(_aws_payer,  Unset):
            aws_payer = UNSET
        else:
            aws_payer = AWSPayer.from_dict(_aws_payer)




        _azure_payer = d.pop("azure_payer", UNSET)
        azure_payer: AzurePayer | Unset
        if isinstance(_azure_payer,  Unset):
            azure_payer = UNSET
        else:
            azure_payer = AzurePayer.from_dict(_azure_payer)




        _custom_billing_source = d.pop("custom_billing_source", UNSET)
        custom_billing_source: CustomBillingSource | Unset
        if isinstance(_custom_billing_source,  Unset):
            custom_billing_source = UNSET
        else:
            custom_billing_source = CustomBillingSource.from_dict(_custom_billing_source)




        _gcp_payer = d.pop("gcp_payer", UNSET)
        gcp_payer: GCPBillingAccountAugmented | Unset
        if isinstance(_gcp_payer,  Unset):
            gcp_payer = UNSET
        else:
            gcp_payer = GCPBillingAccountAugmented.from_dict(_gcp_payer)




        id = d.pop("id", UNSET)

        _oci_payer = d.pop("oci_payer", UNSET)
        oci_payer: OCIBillingSource | Unset
        if isinstance(_oci_payer,  Unset):
            oci_payer = UNSET
        else:
            oci_payer = OCIBillingSource.from_dict(_oci_payer)




        def _parse_use_focus_reports(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_focus_reports = _parse_use_focus_reports(d.pop("use_focus_reports", UNSET))


        def _parse_use_proprietary_reports(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_proprietary_reports = _parse_use_proprietary_reports(d.pop("use_proprietary_reports", UNSET))


        billing_source = cls(
            account_creation=account_creation,
            aws_payer=aws_payer,
            azure_payer=azure_payer,
            custom_billing_source=custom_billing_source,
            gcp_payer=gcp_payer,
            id=id,
            oci_payer=oci_payer,
            use_focus_reports=use_focus_reports,
            use_proprietary_reports=use_proprietary_reports,
        )


        billing_source.additional_properties = d
        return billing_source

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
