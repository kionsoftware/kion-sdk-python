from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_admin_contact_email_response_200 import GetAdminContactEmailResponse200
from ...models.get_admin_contact_email_response_401 import GetAdminContactEmailResponse401
from ...models.get_admin_contact_email_response_403 import GetAdminContactEmailResponse403
from ...models.get_admin_contact_email_response_500 import GetAdminContactEmailResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/app-config/admin-contact-email",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAdminContactEmailResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetAdminContactEmailResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAdminContactEmailResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetAdminContactEmailResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500]:
    """ Gets the admin contact email

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500 | None:
    """ Gets the admin contact email

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500]:
    """ Gets the admin contact email

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500 | None:
    """ Gets the admin contact email

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAdminContactEmailResponse200 | GetAdminContactEmailResponse401 | GetAdminContactEmailResponse403 | GetAdminContactEmailResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
