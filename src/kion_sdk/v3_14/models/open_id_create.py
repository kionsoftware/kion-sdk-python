from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.open_id_access_rule_create import OpenIDAccessRuleCreate





T = TypeVar("T", bound="OpenIDCreate")



@_attrs_define
class OpenIDCreate:
    """ OpenIDCreate defines the expected payload for creating an OpenID IDMS entity in the application.

        Attributes:
            access_rules (list[OpenIDAccessRuleCreate] | None | Unset): AccessRules defines the console access defined for
                matching users in Kion
            authorization_endpoint (str | Unset): AuthorizationEndpoint is the endpoint the OpenID provider determines to
                kick off the authentication process Example: https://accounts.google.com/o/oauth2/v2/auth.
            client_id (str | Unset): ClientID that links Kion to the OpenID Provider, determined when configuring OpenID
                Example: 55548-3410afd-d.
            email_claim (str | Unset): EmailClaim defines an optional mapping of an OpenID claim value to a user's email
                attribute in Kion Example: email.
            first_name_claim (str | Unset): FirstNameClaim defines an optional mapping of an OpenID claim value to a user's
                first name attribute in Kion Example: given_name.
            issuer (str | Unset): Issuer is the URL for the OpenID Provider Example: https://cloudtamer-io-dev.onelogin.com.
            jwks_uri (str | Unset): JwksURI describes the endpoint of an OpenID provider used to retrieve token security
                information for validation Example: https://www.googleapis.com/oauth2/v3/certs.
            last_name_claim (str | Unset): LastNameClaim defines an optional mapping of an OpenID claim value to a user's
                last name attribute in Kion Example: family_name.
            name (str | Unset): Name of the OpenID in the application. Example: Internal Directory.
            phone_claim (str | Unset): PhoneClaim defines an optional mapping of an OpenID claim value to a user's phone
                attribute in Kion Example: phone_number.
            scopes (list[str] | None | Unset): Scopes define the claim variables that an OpenID provider will include in an
                auth request. Specifics depend on the OpenID provider. Example: ['openai', 'profile'].
            username_claim (str | Unset): UsernameClaim defines an optional mapping of an OpenID claim value to a user's
                username attribute in Kion. Required to uniquely identify users Example: preferred_username.
     """

    access_rules: list[OpenIDAccessRuleCreate] | None | Unset = UNSET
    authorization_endpoint: str | Unset = UNSET
    client_id: str | Unset = UNSET
    email_claim: str | Unset = UNSET
    first_name_claim: str | Unset = UNSET
    issuer: str | Unset = UNSET
    jwks_uri: str | Unset = UNSET
    last_name_claim: str | Unset = UNSET
    name: str | Unset = UNSET
    phone_claim: str | Unset = UNSET
    scopes: list[str] | None | Unset = UNSET
    username_claim: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.open_id_access_rule_create import OpenIDAccessRuleCreate
        access_rules: list[dict[str, Any]] | None | Unset
        if isinstance(self.access_rules, Unset):
            access_rules = UNSET
        elif isinstance(self.access_rules, list):
            access_rules = []
            for access_rules_type_0_item_data in self.access_rules:
                access_rules_type_0_item = access_rules_type_0_item_data.to_dict()
                access_rules.append(access_rules_type_0_item)


        else:
            access_rules = self.access_rules

        authorization_endpoint = self.authorization_endpoint

        client_id = self.client_id

        email_claim = self.email_claim

        first_name_claim = self.first_name_claim

        issuer = self.issuer

        jwks_uri = self.jwks_uri

        last_name_claim = self.last_name_claim

        name = self.name

        phone_claim = self.phone_claim

        scopes: list[str] | None | Unset
        if isinstance(self.scopes, Unset):
            scopes = UNSET
        elif isinstance(self.scopes, list):
            scopes = self.scopes


        else:
            scopes = self.scopes

        username_claim = self.username_claim


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_rules is not UNSET:
            field_dict["access_rules"] = access_rules
        if authorization_endpoint is not UNSET:
            field_dict["authorization_endpoint"] = authorization_endpoint
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if email_claim is not UNSET:
            field_dict["email_claim"] = email_claim
        if first_name_claim is not UNSET:
            field_dict["first_name_claim"] = first_name_claim
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if jwks_uri is not UNSET:
            field_dict["jwks_uri"] = jwks_uri
        if last_name_claim is not UNSET:
            field_dict["last_name_claim"] = last_name_claim
        if name is not UNSET:
            field_dict["name"] = name
        if phone_claim is not UNSET:
            field_dict["phone_claim"] = phone_claim
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if username_claim is not UNSET:
            field_dict["username_claim"] = username_claim

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.open_id_access_rule_create import OpenIDAccessRuleCreate
        d = dict(src_dict)
        def _parse_access_rules(data: object) -> list[OpenIDAccessRuleCreate] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_rules_type_0 = []
                _access_rules_type_0 = data
                for access_rules_type_0_item_data in (_access_rules_type_0):
                    access_rules_type_0_item = OpenIDAccessRuleCreate.from_dict(access_rules_type_0_item_data)



                    access_rules_type_0.append(access_rules_type_0_item)

                return access_rules_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OpenIDAccessRuleCreate] | None | Unset, data)

        access_rules = _parse_access_rules(d.pop("access_rules", UNSET))


        authorization_endpoint = d.pop("authorization_endpoint", UNSET)

        client_id = d.pop("client_id", UNSET)

        email_claim = d.pop("email_claim", UNSET)

        first_name_claim = d.pop("first_name_claim", UNSET)

        issuer = d.pop("issuer", UNSET)

        jwks_uri = d.pop("jwks_uri", UNSET)

        last_name_claim = d.pop("last_name_claim", UNSET)

        name = d.pop("name", UNSET)

        phone_claim = d.pop("phone_claim", UNSET)

        def _parse_scopes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                scopes_type_0 = cast(list[str], data)

                return scopes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        scopes = _parse_scopes(d.pop("scopes", UNSET))


        username_claim = d.pop("username_claim", UNSET)

        open_id_create = cls(
            access_rules=access_rules,
            authorization_endpoint=authorization_endpoint,
            client_id=client_id,
            email_claim=email_claim,
            first_name_claim=first_name_claim,
            issuer=issuer,
            jwks_uri=jwks_uri,
            last_name_claim=last_name_claim,
            name=name,
            phone_claim=phone_claim,
            scopes=scopes,
            username_claim=username_claim,
        )


        open_id_create.additional_properties = d
        return open_id_create

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
