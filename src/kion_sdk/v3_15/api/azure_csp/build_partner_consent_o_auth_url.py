from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.build_partner_consent_o_auth_url_response_201 import BuildPartnerConsentOAuthURLResponse201
from ...models.build_partner_consent_o_auth_url_response_400 import BuildPartnerConsentOAuthURLResponse400
from ...models.build_partner_consent_o_auth_url_response_401 import BuildPartnerConsentOAuthURLResponse401
from ...models.build_partner_consent_o_auth_url_response_403 import BuildPartnerConsentOAuthURLResponse403
from ...models.build_partner_consent_o_auth_url_response_422 import BuildPartnerConsentOAuthURLResponse422
from ...models.build_partner_consent_o_auth_url_response_500 import BuildPartnerConsentOAuthURLResponse500
from ...models.partner_consent_initiate import PartnerConsentInitiate
from typing import cast



def _get_kwargs(
    *,
    body: PartnerConsentInitiate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/azure-csp/initiate-service-account-registration",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500 | None:
    if response.status_code == 201:
        response_201 = BuildPartnerConsentOAuthURLResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = BuildPartnerConsentOAuthURLResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = BuildPartnerConsentOAuthURLResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = BuildPartnerConsentOAuthURLResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = BuildPartnerConsentOAuthURLResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = BuildPartnerConsentOAuthURLResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PartnerConsentInitiate,

) -> Response[BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500]:
    """ Requires a CSP Auth token. Accepts app registration data in exchange for an OAuth URL for partner
    consent.

    Args:
        body (PartnerConsentInitiate): PartnerConsentInitiate contains data about the web app
            registration and azure AD domain that should be used to authenticate the CSP service user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: PartnerConsentInitiate,

) -> BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500 | None:
    """ Requires a CSP Auth token. Accepts app registration data in exchange for an OAuth URL for partner
    consent.

    Args:
        body (PartnerConsentInitiate): PartnerConsentInitiate contains data about the web app
            registration and azure AD domain that should be used to authenticate the CSP service user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PartnerConsentInitiate,

) -> Response[BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500]:
    """ Requires a CSP Auth token. Accepts app registration data in exchange for an OAuth URL for partner
    consent.

    Args:
        body (PartnerConsentInitiate): PartnerConsentInitiate contains data about the web app
            registration and azure AD domain that should be used to authenticate the CSP service user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PartnerConsentInitiate,

) -> BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500 | None:
    """ Requires a CSP Auth token. Accepts app registration data in exchange for an OAuth URL for partner
    consent.

    Args:
        body (PartnerConsentInitiate): PartnerConsentInitiate contains data about the web app
            registration and azure AD domain that should be used to authenticate the CSP service user

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BuildPartnerConsentOAuthURLResponse201 | BuildPartnerConsentOAuthURLResponse400 | BuildPartnerConsentOAuthURLResponse401 | BuildPartnerConsentOAuthURLResponse403 | BuildPartnerConsentOAuthURLResponse422 | BuildPartnerConsentOAuthURLResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
