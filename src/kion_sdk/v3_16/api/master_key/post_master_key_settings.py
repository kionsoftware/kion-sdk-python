from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.master_key_settings import MasterKeySettings
from ...models.post_master_key_settings_response_200 import PostMasterKeySettingsResponse200
from ...models.post_master_key_settings_response_400 import PostMasterKeySettingsResponse400
from ...models.post_master_key_settings_response_403 import PostMasterKeySettingsResponse403
from ...models.post_master_key_settings_response_422 import PostMasterKeySettingsResponse422
from ...models.post_master_key_settings_response_500 import PostMasterKeySettingsResponse500
from typing import cast



def _get_kwargs(
    *,
    body: MasterKeySettings,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/master-key/settings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500 | None:
    if response.status_code == 200:
        response_200 = PostMasterKeySettingsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 304:
        response_304 = cast(Any, None)
        return response_304

    if response.status_code == 400:
        response_400 = PostMasterKeySettingsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = PostMasterKeySettingsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostMasterKeySettingsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostMasterKeySettingsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: MasterKeySettings,

) -> Response[Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500]:
    """ Sets storage mode settings for the master key.

    Args:
        body (MasterKeySettings): MasterKeySettings represents master key configurations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500]
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
    body: MasterKeySettings,

) -> Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500 | None:
    """ Sets storage mode settings for the master key.

    Args:
        body (MasterKeySettings): MasterKeySettings represents master key configurations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MasterKeySettings,

) -> Response[Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500]:
    """ Sets storage mode settings for the master key.

    Args:
        body (MasterKeySettings): MasterKeySettings represents master key configurations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500]
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
    body: MasterKeySettings,

) -> Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500 | None:
    """ Sets storage mode settings for the master key.

    Args:
        body (MasterKeySettings): MasterKeySettings represents master key configurations

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMasterKeySettingsResponse200 | PostMasterKeySettingsResponse400 | PostMasterKeySettingsResponse403 | PostMasterKeySettingsResponse422 | PostMasterKeySettingsResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
