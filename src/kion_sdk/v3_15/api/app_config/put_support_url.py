from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.put_support_url_response_200 import PutSupportURLResponse200
from ...models.put_support_url_response_401 import PutSupportURLResponse401
from ...models.put_support_url_response_403 import PutSupportURLResponse403
from ...models.put_support_url_response_500 import PutSupportURLResponse500
from ...models.support_url import SupportURL
from typing import cast



def _get_kwargs(
    *,
    body: SupportURL,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/app-config/support-url",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500 | None:
    if response.status_code == 200:
        response_200 = PutSupportURLResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = PutSupportURLResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PutSupportURLResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = PutSupportURLResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SupportURL,

) -> Response[PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500]:
    """ Sets the support URL

    Args:
        body (SupportURL): SupportURL represents the support URL for the application

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500]
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
    body: SupportURL,

) -> PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500 | None:
    """ Sets the support URL

    Args:
        body (SupportURL): SupportURL represents the support URL for the application

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SupportURL,

) -> Response[PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500]:
    """ Sets the support URL

    Args:
        body (SupportURL): SupportURL represents the support URL for the application

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500]
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
    body: SupportURL,

) -> PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500 | None:
    """ Sets the support URL

    Args:
        body (SupportURL): SupportURL represents the support URL for the application

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutSupportURLResponse200 | PutSupportURLResponse401 | PutSupportURLResponse403 | PutSupportURLResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
