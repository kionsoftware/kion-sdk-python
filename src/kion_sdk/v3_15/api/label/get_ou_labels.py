from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_ou_labels_response_200 import GetOULabelsResponse200
from ...models.get_ou_labels_response_400 import GetOULabelsResponse400
from ...models.get_ou_labels_response_401 import GetOULabelsResponse401
from ...models.get_ou_labels_response_403 import GetOULabelsResponse403
from ...models.get_ou_labels_response_500 import GetOULabelsResponse500
from typing import cast



def _get_kwargs(
    ou_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/ou/{ou_id}/labels".format(ou_id=quote(str(ou_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetOULabelsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetOULabelsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetOULabelsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetOULabelsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetOULabelsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ou_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500]:
    """ Gets all labels associated with a given OU ID.

    Args:
        ou_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    ou_id: int,
    *,
    client: AuthenticatedClient,

) -> GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500 | None:
    """ Gets all labels associated with a given OU ID.

    Args:
        ou_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500
     """


    return sync_detailed(
        ou_id=ou_id,
client=client,

    ).parsed

async def asyncio_detailed(
    ou_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500]:
    """ Gets all labels associated with a given OU ID.

    Args:
        ou_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500]
     """


    kwargs = _get_kwargs(
        ou_id=ou_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    ou_id: int,
    *,
    client: AuthenticatedClient,

) -> GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500 | None:
    """ Gets all labels associated with a given OU ID.

    Args:
        ou_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOULabelsResponse200 | GetOULabelsResponse400 | GetOULabelsResponse401 | GetOULabelsResponse403 | GetOULabelsResponse500
     """


    return (await asyncio_detailed(
        ou_id=ou_id,
client=client,

    )).parsed
