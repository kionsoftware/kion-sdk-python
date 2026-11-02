from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_account_custom_variable_response_400 import DeleteAccountCustomVariableResponse400
from ...models.delete_account_custom_variable_response_401 import DeleteAccountCustomVariableResponse401
from ...models.delete_account_custom_variable_response_403 import DeleteAccountCustomVariableResponse403
from ...models.delete_account_custom_variable_response_404 import DeleteAccountCustomVariableResponse404
from ...models.delete_account_custom_variable_response_500 import DeleteAccountCustomVariableResponse500
from typing import cast



def _get_kwargs(
    account_id: int,
    custom_variable_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v3/account/{account_id}/custom-variable/{custom_variable_id}".format(account_id=quote(str(account_id), safe=""),custom_variable_id=quote(str(custom_variable_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = DeleteAccountCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = DeleteAccountCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = DeleteAccountCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = DeleteAccountCustomVariableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = DeleteAccountCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500]:
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

) -> Response[Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500]:
    """ Deletes an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500]
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

) -> Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500 | None:
    """ Deletes an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500
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

) -> Response[Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500]:
    """ Deletes an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500]
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

) -> Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500 | None:
    """ Deletes an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteAccountCustomVariableResponse400 | DeleteAccountCustomVariableResponse401 | DeleteAccountCustomVariableResponse403 | DeleteAccountCustomVariableResponse404 | DeleteAccountCustomVariableResponse500
     """


    return (await asyncio_detailed(
        account_id=account_id,
custom_variable_id=custom_variable_id,
client=client,

    )).parsed
