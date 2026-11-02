from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_account_labels_response_200 import GetAccountLabelsResponse200
from ...models.get_account_labels_response_400 import GetAccountLabelsResponse400
from ...models.get_account_labels_response_401 import GetAccountLabelsResponse401
from ...models.get_account_labels_response_403 import GetAccountLabelsResponse403
from ...models.get_account_labels_response_500 import GetAccountLabelsResponse500
from typing import cast



def _get_kwargs(
    account_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/account/{account_id}/labels".format(account_id=quote(str(account_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAccountLabelsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAccountLabelsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAccountLabelsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAccountLabelsResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetAccountLabelsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500]:
    """ Gets all labels associated with a given account ID.

    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: int,
    *,
    client: AuthenticatedClient,

) -> GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500 | None:
    """ Gets all labels associated with a given account ID.

    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500
     """


    return sync_detailed(
        account_id=account_id,
client=client,

    ).parsed

async def asyncio_detailed(
    account_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500]:
    """ Gets all labels associated with a given account ID.

    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: int,
    *,
    client: AuthenticatedClient,

) -> GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500 | None:
    """ Gets all labels associated with a given account ID.

    Args:
        account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountLabelsResponse200 | GetAccountLabelsResponse400 | GetAccountLabelsResponse401 | GetAccountLabelsResponse403 | GetAccountLabelsResponse500
     """


    return (await asyncio_detailed(
        account_id=account_id,
client=client,

    )).parsed
