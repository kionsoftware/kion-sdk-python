from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_ou_exemption_response_200 import DeleteOUExemptionResponse200
from ...models.delete_ou_exemption_response_400 import DeleteOUExemptionResponse400
from ...models.delete_ou_exemption_response_401 import DeleteOUExemptionResponse401
from ...models.delete_ou_exemption_response_403 import DeleteOUExemptionResponse403
from ...models.delete_ou_exemption_response_404 import DeleteOUExemptionResponse404
from ...models.delete_ou_exemption_response_500 import DeleteOUExemptionResponse500
from typing import cast



def _get_kwargs(
    id: int,
    exemption_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/ou/{id}/cloud-rule/exemption/{exemption_id}".format(id=quote(str(id), safe=""),exemption_id=quote(str(exemption_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500 | None:
    if response.status_code == 200:
        response_200 = DeleteOUExemptionResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = DeleteOUExemptionResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteOUExemptionResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteOUExemptionResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteOUExemptionResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteOUExemptionResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    exemption_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500]:
    """ Removes a cloud rule exemption from an OU, causing the cloud rule to be reapplied to the OU.

    Args:
        id (int):
        exemption_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
exemption_id=exemption_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    exemption_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500 | None:
    """ Removes a cloud rule exemption from an OU, causing the cloud rule to be reapplied to the OU.

    Args:
        id (int):
        exemption_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500
     """


    return sync_detailed(
        id=id,
exemption_id=exemption_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    exemption_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500]:
    """ Removes a cloud rule exemption from an OU, causing the cloud rule to be reapplied to the OU.

    Args:
        id (int):
        exemption_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
exemption_id=exemption_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    exemption_id: int,
    *,
    client: AuthenticatedClient,

) -> DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500 | None:
    """ Removes a cloud rule exemption from an OU, causing the cloud rule to be reapplied to the OU.

    Args:
        id (int):
        exemption_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteOUExemptionResponse200 | DeleteOUExemptionResponse400 | DeleteOUExemptionResponse401 | DeleteOUExemptionResponse403 | DeleteOUExemptionResponse404 | DeleteOUExemptionResponse500
     """


    return (await asyncio_detailed(
        id=id,
exemption_id=exemption_id,
client=client,

    )).parsed
