from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_csp_consent_status_response_200 import GetCSPConsentStatusResponse200
from ...models.get_csp_consent_status_response_400 import GetCSPConsentStatusResponse400
from ...models.get_csp_consent_status_response_401 import GetCSPConsentStatusResponse401
from ...models.get_csp_consent_status_response_403 import GetCSPConsentStatusResponse403
from ...models.get_csp_consent_status_response_404 import GetCSPConsentStatusResponse404
from ...models.get_csp_consent_status_response_500 import GetCSPConsentStatusResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/azure-csp/{id}/consent/status".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500 | None:
    if response.status_code == 200:
        response_200 = GetCSPConsentStatusResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetCSPConsentStatusResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetCSPConsentStatusResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetCSPConsentStatusResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetCSPConsentStatusResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetCSPConsentStatusResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500]:
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

) -> Response[GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500]:
    """ Returns the partner consent status of the CSP - either Outdated Auth Version (1), Pending Partner
    Consent (2),

     or CSP Ready (3)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500]
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

) -> GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500 | None:
    """ Returns the partner consent status of the CSP - either Outdated Auth Version (1), Pending Partner
    Consent (2),

     or CSP Ready (3)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500]:
    """ Returns the partner consent status of the CSP - either Outdated Auth Version (1), Pending Partner
    Consent (2),

     or CSP Ready (3)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500]
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

) -> GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500 | None:
    """ Returns the partner consent status of the CSP - either Outdated Auth Version (1), Pending Partner
    Consent (2),

     or CSP Ready (3)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCSPConsentStatusResponse200 | GetCSPConsentStatusResponse400 | GetCSPConsentStatusResponse401 | GetCSPConsentStatusResponse403 | GetCSPConsentStatusResponse404 | GetCSPConsentStatusResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
