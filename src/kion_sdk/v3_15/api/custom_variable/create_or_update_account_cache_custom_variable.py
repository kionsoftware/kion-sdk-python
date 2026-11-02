from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_cache_custom_variable_create_or_update import AccountCacheCustomVariableCreateOrUpdate
from ...models.create_or_update_account_cache_custom_variable_response_400 import CreateOrUpdateAccountCacheCustomVariableResponse400
from ...models.create_or_update_account_cache_custom_variable_response_401 import CreateOrUpdateAccountCacheCustomVariableResponse401
from ...models.create_or_update_account_cache_custom_variable_response_403 import CreateOrUpdateAccountCacheCustomVariableResponse403
from ...models.create_or_update_account_cache_custom_variable_response_404 import CreateOrUpdateAccountCacheCustomVariableResponse404
from ...models.create_or_update_account_cache_custom_variable_response_422 import CreateOrUpdateAccountCacheCustomVariableResponse422
from ...models.create_or_update_account_cache_custom_variable_response_500 import CreateOrUpdateAccountCacheCustomVariableResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    account_cache_id: int,
    custom_variable_id: int,
    *,
    body: AccountCacheCustomVariableCreateOrUpdate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/account-cache/{account_cache_id}/custom-variable/{custom_variable_id}".format(account_cache_id=quote(str(account_cache_id), safe=""),custom_variable_id=quote(str(custom_variable_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = CreateOrUpdateAccountCacheCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateOrUpdateAccountCacheCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateOrUpdateAccountCacheCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CreateOrUpdateAccountCacheCustomVariableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = CreateOrUpdateAccountCacheCustomVariableResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = CreateOrUpdateAccountCacheCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_cache_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: AccountCacheCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Response[Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500]:
    """ Creates or updates an account cache custom variable override.

    Args:
        account_cache_id (int):
        custom_variable_id (int):
        body (AccountCacheCustomVariableCreateOrUpdate | Unset):
            AccountCacheCustomVariableCreateOrUpdate represents the fields necessary to create or
            update an account cache custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        account_cache_id=account_cache_id,
custom_variable_id=custom_variable_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    account_cache_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: AccountCacheCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500 | None:
    """ Creates or updates an account cache custom variable override.

    Args:
        account_cache_id (int):
        custom_variable_id (int):
        body (AccountCacheCustomVariableCreateOrUpdate | Unset):
            AccountCacheCustomVariableCreateOrUpdate represents the fields necessary to create or
            update an account cache custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500
     """


    return sync_detailed(
        account_cache_id=account_cache_id,
custom_variable_id=custom_variable_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    account_cache_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: AccountCacheCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Response[Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500]:
    """ Creates or updates an account cache custom variable override.

    Args:
        account_cache_id (int):
        custom_variable_id (int):
        body (AccountCacheCustomVariableCreateOrUpdate | Unset):
            AccountCacheCustomVariableCreateOrUpdate represents the fields necessary to create or
            update an account cache custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        account_cache_id=account_cache_id,
custom_variable_id=custom_variable_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    account_cache_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: AccountCacheCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500 | None:
    """ Creates or updates an account cache custom variable override.

    Args:
        account_cache_id (int):
        custom_variable_id (int):
        body (AccountCacheCustomVariableCreateOrUpdate | Unset):
            AccountCacheCustomVariableCreateOrUpdate represents the fields necessary to create or
            update an account cache custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateOrUpdateAccountCacheCustomVariableResponse400 | CreateOrUpdateAccountCacheCustomVariableResponse401 | CreateOrUpdateAccountCacheCustomVariableResponse403 | CreateOrUpdateAccountCacheCustomVariableResponse404 | CreateOrUpdateAccountCacheCustomVariableResponse422 | CreateOrUpdateAccountCacheCustomVariableResponse500
     """


    return (await asyncio_detailed(
        account_cache_id=account_cache_id,
custom_variable_id=custom_variable_id,
client=client,
body=body,

    )).parsed
