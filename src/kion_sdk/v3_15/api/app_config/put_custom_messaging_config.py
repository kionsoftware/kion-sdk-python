from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.custom_messaging_config import CustomMessagingConfig
from ...models.put_custom_messaging_config_response_200 import PutCustomMessagingConfigResponse200
from ...models.put_custom_messaging_config_response_401 import PutCustomMessagingConfigResponse401
from ...models.put_custom_messaging_config_response_403 import PutCustomMessagingConfigResponse403
from ...models.put_custom_messaging_config_response_500 import PutCustomMessagingConfigResponse500
from typing import cast



def _get_kwargs(
    *,
    body: CustomMessagingConfig,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/app-config/custom-messaging",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500 | None:
    if response.status_code == 200:
        response_200 = PutCustomMessagingConfigResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PutCustomMessagingConfigResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutCustomMessagingConfigResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PutCustomMessagingConfigResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomMessagingConfig,

) -> Response[PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500]:
    """ Sets the custom messaging config settings

    Args:
        body (CustomMessagingConfig): CustomMessagingConfig represents the system settings for
            custom messaging in the app

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500]
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
    body: CustomMessagingConfig,

) -> PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500 | None:
    """ Sets the custom messaging config settings

    Args:
        body (CustomMessagingConfig): CustomMessagingConfig represents the system settings for
            custom messaging in the app

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CustomMessagingConfig,

) -> Response[PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500]:
    """ Sets the custom messaging config settings

    Args:
        body (CustomMessagingConfig): CustomMessagingConfig represents the system settings for
            custom messaging in the app

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500]
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
    body: CustomMessagingConfig,

) -> PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500 | None:
    """ Sets the custom messaging config settings

    Args:
        body (CustomMessagingConfig): CustomMessagingConfig represents the system settings for
            custom messaging in the app

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutCustomMessagingConfigResponse200 | PutCustomMessagingConfigResponse401 | PutCustomMessagingConfigResponse403 | PutCustomMessagingConfigResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
