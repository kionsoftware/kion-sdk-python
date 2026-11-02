from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_account_custom_variable_response_200 import GetAccountCustomVariableResponse200
from ...models.get_account_custom_variable_response_400 import GetAccountCustomVariableResponse400
from ...models.get_account_custom_variable_response_401 import GetAccountCustomVariableResponse401
from ...models.get_account_custom_variable_response_403 import GetAccountCustomVariableResponse403
from ...models.get_account_custom_variable_response_404 import GetAccountCustomVariableResponse404
from ...models.get_account_custom_variable_response_500 import GetAccountCustomVariableResponse500
from typing import cast



def _get_kwargs(
    account_id: int,
    custom_variable_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/account/{account_id}/custom-variable/{custom_variable_id}".format(account_id=quote(str(account_id), safe=""),custom_variable_id=quote(str(custom_variable_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAccountCustomVariableResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAccountCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAccountCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAccountCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetAccountCustomVariableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetAccountCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500]:
    """ Returns an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
custom_variable_id=custom_variable_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500 | None:
    """ Returns an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500
     """


    return sync_detailed(
        account_id=account_id,
custom_variable_id=custom_variable_id,
client=client,

    ).parsed

async def asyncio_detailed(
    account_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500]:
    """ Returns an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
custom_variable_id=custom_variable_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,

) -> GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500 | None:
    """ Returns an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountCustomVariableResponse200 | GetAccountCustomVariableResponse400 | GetAccountCustomVariableResponse401 | GetAccountCustomVariableResponse403 | GetAccountCustomVariableResponse404 | GetAccountCustomVariableResponse500
     """


    return (await asyncio_detailed(
        account_id=account_id,
custom_variable_id=custom_variable_id,
client=client,

    )).parsed
