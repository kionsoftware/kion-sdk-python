from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GCPRoleValidationResult")



@_attrs_define
class GCPRoleValidationResult:
    """ GCPRoleValidationResult defines the result of role validation

        Attributes:
            denial_errors (list[str] | None | Unset): Whether or not the permissions and denials are valid Example: ['The
                permission `iam.role.create` would be excluded by `iam.role.*`'].
            permission_errors (list[str] | None | Unset): Whether or not the permissions and denials are valid Example:
                ['The permission `iam.role.create` would be excluded by `iam.role.*`'].
            valid (bool | None | Unset): Whether or not the permissions and denials are valid Example: True.
     """

    denial_errors: list[str] | None | Unset = UNSET
    permission_errors: list[str] | None | Unset = UNSET
    valid: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        denial_errors: list[str] | None | Unset
        if isinstance(self.denial_errors, Unset):
            denial_errors = UNSET
        elif isinstance(self.denial_errors, list):
            denial_errors = self.denial_errors


        else:
            denial_errors = self.denial_errors

        permission_errors: list[str] | None | Unset
        if isinstance(self.permission_errors, Unset):
            permission_errors = UNSET
        elif isinstance(self.permission_errors, list):
            permission_errors = self.permission_errors


        else:
            permission_errors = self.permission_errors

        valid: bool | None | Unset
        if isinstance(self.valid, Unset):
            valid = UNSET
        else:
            valid = self.valid


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if denial_errors is not UNSET:
            field_dict["denial_errors"] = denial_errors
        if permission_errors is not UNSET:
            field_dict["permission_errors"] = permission_errors
        if valid is not UNSET:
            field_dict["valid"] = valid

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_denial_errors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                denial_errors_type_0 = cast(list[str], data)

                return denial_errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        denial_errors = _parse_denial_errors(d.pop("denial_errors", UNSET))


        def _parse_permission_errors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permission_errors_type_0 = cast(list[str], data)

                return permission_errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        permission_errors = _parse_permission_errors(d.pop("permission_errors", UNSET))


        def _parse_valid(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        valid = _parse_valid(d.pop("valid", UNSET))


        gcp_role_validation_result = cls(
            denial_errors=denial_errors,
            permission_errors=permission_errors,
            valid=valid,
        )


        gcp_role_validation_result.additional_properties = d
        return gcp_role_validation_result

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
