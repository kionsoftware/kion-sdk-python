from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_consent_link_response_201 import GetConsentLinkResponse201
from ...models.get_consent_link_response_400 import GetConsentLinkResponse400
from ...models.get_consent_link_response_401 import GetConsentLinkResponse401
from ...models.get_consent_link_response_403 import GetConsentLinkResponse403
from ...models.get_consent_link_response_404 import GetConsentLinkResponse404
from ...models.get_consent_link_response_500 import GetConsentLinkResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/azure-csp/{id}/consent/link".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500 | None:
    if response.status_code == 201:
        response_201 = GetConsentLinkResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = GetConsentLinkResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetConsentLinkResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetConsentLinkResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetConsentLinkResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetConsentLinkResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500]:
    """ Generates a link for the given CSP which can be delivered to a member of the CSP to fill in
    authentication information.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500 | None:
    """ Generates a link for the given CSP which can be delivered to a member of the CSP to fill in
    authentication information.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500]:
    """ Generates a link for the given CSP which can be delivered to a member of the CSP to fill in
    authentication information.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500 | None:
    """ Generates a link for the given CSP which can be delivered to a member of the CSP to fill in
    authentication information.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConsentLinkResponse201 | GetConsentLinkResponse400 | GetConsentLinkResponse401 | GetConsentLinkResponse403 | GetConsentLinkResponse404 | GetConsentLinkResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
