from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.feature_flag_data_features import FeatureFlagDataFeatures





T = TypeVar("T", bound="FeatureFlagData")



@_attrs_define
class FeatureFlagData:
    """ 
        Attributes:
            enabled (bool | None | Unset): Whether the feature flag is enabled or not Example: True.
            features (FeatureFlagDataFeatures | Unset): Whether the feature flag is enabled or not Example: {'subFeature1':
                {'enabled': True, 'features': {'subSubFeature1': {'enabled': True}, 'subSubFeature2': {'enabled': True}}},
                'subFeature2': {'enabled': True}}.
     """

    enabled: bool | None | Unset = UNSET
    features: FeatureFlagDataFeatures | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.feature_flag_data_features import FeatureFlagDataFeatures
        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        features: dict[str, Any] | Unset = UNSET
        if not isinstance(self.features, Unset):
            features = self.features.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if features is not UNSET:
            field_dict["features"] = features

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.feature_flag_data_features import FeatureFlagDataFeatures
        d = dict(src_dict)
        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        _features = d.pop("features", UNSET)
        features: FeatureFlagDataFeatures | Unset
        if isinstance(_features,  Unset):
            features = UNSET
        else:
            features = FeatureFlagDataFeatures.from_dict(_features)




        feature_flag_data = cls(
            enabled=enabled,
            features=features,
        )


        feature_flag_data.additional_properties = d
        return feature_flag_data

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
