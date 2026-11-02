from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_account_index_response_200 import GetAccountIndexResponse200
from ...models.get_account_index_response_401 import GetAccountIndexResponse401
from ...models.get_account_index_response_500 import GetAccountIndexResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    name: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    account_type: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["name"] = name

    params["alias"] = alias

    params["account_type"] = account_type

    params["label"] = label

    params["label_key"] = label_key

    params["label_value"] = label_value

    params["label_id"] = label_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/account",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAccountIndexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetAccountIndexResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = GetAccountIndexResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    account_type: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> Response[GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500]:
    """ Returns a list of accounts from the application.

    Args:
        name (str | Unset):
        alias (str | Unset):
        account_type (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500]
     """


    kwargs = _get_kwargs(
        name=name,
alias=alias,
account_type=account_type,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    account_type: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500 | None:
    """ Returns a list of accounts from the application.

    Args:
        name (str | Unset):
        alias (str | Unset):
        account_type (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500
     """


    return sync_detailed(
        client=client,
name=name,
alias=alias,
account_type=account_type,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    account_type: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> Response[GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500]:
    """ Returns a list of accounts from the application.

    Args:
        name (str | Unset):
        alias (str | Unset):
        account_type (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500]
     """


    kwargs = _get_kwargs(
        name=name,
alias=alias,
account_type=account_type,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    account_type: str | Unset = UNSET,
    label: str | Unset = UNSET,
    label_key: str | Unset = UNSET,
    label_value: str | Unset = UNSET,
    label_id: str | Unset = UNSET,

) -> GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500 | None:
    """ Returns a list of accounts from the application.

    Args:
        name (str | Unset):
        alias (str | Unset):
        account_type (str | Unset):
        label (str | Unset):
        label_key (str | Unset):
        label_value (str | Unset):
        label_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAccountIndexResponse200 | GetAccountIndexResponse401 | GetAccountIndexResponse500
     """


    return (await asyncio_detailed(
        client=client,
name=name,
alias=alias,
account_type=account_type,
label=label,
label_key=label_key,
label_value=label_value,
label_id=label_id,

    )).parsed
