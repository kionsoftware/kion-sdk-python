from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_custom_variable_create_or_update import AccountCustomVariableCreateOrUpdate
from ...models.create_or_update_account_custom_variable_response_400 import CreateOrUpdateAccountCustomVariableResponse400
from ...models.create_or_update_account_custom_variable_response_401 import CreateOrUpdateAccountCustomVariableResponse401
from ...models.create_or_update_account_custom_variable_response_403 import CreateOrUpdateAccountCustomVariableResponse403
from ...models.create_or_update_account_custom_variable_response_404 import CreateOrUpdateAccountCustomVariableResponse404
from ...models.create_or_update_account_custom_variable_response_422 import CreateOrUpdateAccountCustomVariableResponse422
from ...models.create_or_update_account_custom_variable_response_500 import CreateOrUpdateAccountCustomVariableResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    account_id: int,
    custom_variable_id: int,
    *,
    body: AccountCustomVariableCreateOrUpdate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/account/{account_id}/custom-variable/{custom_variable_id}".format(account_id=quote(str(account_id), safe=""),custom_variable_id=quote(str(custom_variable_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = CreateOrUpdateAccountCustomVariableResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateOrUpdateAccountCustomVariableResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateOrUpdateAccountCustomVariableResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = CreateOrUpdateAccountCustomVariableResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = CreateOrUpdateAccountCustomVariableResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = CreateOrUpdateAccountCustomVariableResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500]:
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
    body: AccountCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Response[Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500]:
    """ Creates or updates an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):
        body (AccountCustomVariableCreateOrUpdate | Unset): AccountCustomVariableCreateOrUpdate
            represents the fields necessary to create or update an account custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
custom_variable_id=custom_variable_id,
body=body,

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
    body: AccountCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500 | None:
    """ Creates or updates an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):
        body (AccountCustomVariableCreateOrUpdate | Unset): AccountCustomVariableCreateOrUpdate
            represents the fields necessary to create or update an account custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500
     """


    return sync_detailed(
        account_id=account_id,
custom_variable_id=custom_variable_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    account_id: int,
    custom_variable_id: int,
    *,
    client: AuthenticatedClient,
    body: AccountCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Response[Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500]:
    """ Creates or updates an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):
        body (AccountCustomVariableCreateOrUpdate | Unset): AccountCustomVariableCreateOrUpdate
            represents the fields necessary to create or update an account custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
custom_variable_id=custom_variable_id,
body=body,

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
    body: AccountCustomVariableCreateOrUpdate | Unset = UNSET,

) -> Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500 | None:
    """ Creates or updates an account custom variable override.

    Args:
        account_id (int):
        custom_variable_id (int):
        body (AccountCustomVariableCreateOrUpdate | Unset): AccountCustomVariableCreateOrUpdate
            represents the fields necessary to create or update an account custom variable override.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateOrUpdateAccountCustomVariableResponse400 | CreateOrUpdateAccountCustomVariableResponse401 | CreateOrUpdateAccountCustomVariableResponse403 | CreateOrUpdateAccountCustomVariableResponse404 | CreateOrUpdateAccountCustomVariableResponse422 | CreateOrUpdateAccountCustomVariableResponse500
     """


    return (await asyncio_detailed(
        account_id=account_id,
custom_variable_id=custom_variable_id,
client=client,
body=body,

    )).parsed
