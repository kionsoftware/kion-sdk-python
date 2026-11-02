from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.refresh_license_config import RefreshLicenseConfig
from ...models.refresh_license_config_response_200 import RefreshLicenseConfigResponse200
from ...models.refresh_license_config_response_400 import RefreshLicenseConfigResponse400
from ...models.refresh_license_config_response_422 import RefreshLicenseConfigResponse422
from ...models.refresh_license_config_response_500 import RefreshLicenseConfigResponse500
from typing import cast



def _get_kwargs(
    *,
    body: RefreshLicenseConfig,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/license",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = RefreshLicenseConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = RefreshLicenseConfigResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 422:
        response_422 = RefreshLicenseConfigResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = RefreshLicenseConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: RefreshLicenseConfig,

) -> Response[RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500]:
    """ Refreshes an expired license in the application.

    Args:
        body (RefreshLicenseConfig): RefreshLicenseConfig contains a license key to be used to
            refresh an expired license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500]
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
    body: RefreshLicenseConfig,

) -> RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500 | None:
    """ Refreshes an expired license in the application.

    Args:
        body (RefreshLicenseConfig): RefreshLicenseConfig contains a license key to be used to
            refresh an expired license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RefreshLicenseConfig,

) -> Response[RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500]:
    """ Refreshes an expired license in the application.

    Args:
        body (RefreshLicenseConfig): RefreshLicenseConfig contains a license key to be used to
            refresh an expired license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500]
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
    body: RefreshLicenseConfig,

) -> RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500 | None:
    """ Refreshes an expired license in the application.

    Args:
        body (RefreshLicenseConfig): RefreshLicenseConfig contains a license key to be used to
            refresh an expired license.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RefreshLicenseConfigResponse200 | RefreshLicenseConfigResponse400 | RefreshLicenseConfigResponse422 | RefreshLicenseConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
