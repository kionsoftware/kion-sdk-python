from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.hide_integrations_status import HideIntegrationsStatus
from ...models.put_hide_integrations_status_response_200 import PutHideIntegrationsStatusResponse200
from ...models.put_hide_integrations_status_response_401 import PutHideIntegrationsStatusResponse401
from ...models.put_hide_integrations_status_response_403 import PutHideIntegrationsStatusResponse403
from ...models.put_hide_integrations_status_response_500 import PutHideIntegrationsStatusResponse500
from typing import cast



def _get_kwargs(
    *,
    body: HideIntegrationsStatus,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/app-config/hide-integrations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500 | None:
    if response.status_code == 200:
        response_200 = PutHideIntegrationsStatusResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PutHideIntegrationsStatusResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutHideIntegrationsStatusResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PutHideIntegrationsStatusResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: HideIntegrationsStatus,

) -> Response[PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500]:
    """ Sets the Hide Integrations status

    Args:
        body (HideIntegrationsStatus): HideIntegrationsStatus represents whether the integrations
            settings page should be hidden from users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500]
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
    body: HideIntegrationsStatus,

) -> PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500 | None:
    """ Sets the Hide Integrations status

    Args:
        body (HideIntegrationsStatus): HideIntegrationsStatus represents whether the integrations
            settings page should be hidden from users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: HideIntegrationsStatus,

) -> Response[PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500]:
    """ Sets the Hide Integrations status

    Args:
        body (HideIntegrationsStatus): HideIntegrationsStatus represents whether the integrations
            settings page should be hidden from users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500]
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
    body: HideIntegrationsStatus,

) -> PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500 | None:
    """ Sets the Hide Integrations status

    Args:
        body (HideIntegrationsStatus): HideIntegrationsStatus represents whether the integrations
            settings page should be hidden from users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutHideIntegrationsStatusResponse200 | PutHideIntegrationsStatusResponse401 | PutHideIntegrationsStatusResponse403 | PutHideIntegrationsStatusResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
