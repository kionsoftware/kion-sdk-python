from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_all_user_aws_keys_response_200 import GetAllUserAwsKeysResponse200
from ...models.get_all_user_aws_keys_response_400 import GetAllUserAwsKeysResponse400
from ...models.get_all_user_aws_keys_response_401 import GetAllUserAwsKeysResponse401
from ...models.get_all_user_aws_keys_response_403 import GetAllUserAwsKeysResponse403
from ...models.get_all_user_aws_keys_response_500 import GetAllUserAwsKeysResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    include_all: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["include_all"] = include_all


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/user-aws-key",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500 | None:
    if response.status_code == 200:
        response_200 = GetAllUserAwsKeysResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = GetAllUserAwsKeysResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = GetAllUserAwsKeysResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetAllUserAwsKeysResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = GetAllUserAwsKeysResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    include_all: bool | Unset = UNSET,

) -> Response[GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500]:
    """ Gets a list of user AWS keys.

    Args:
        include_all (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500]
     """


    kwargs = _get_kwargs(
        include_all=include_all,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    include_all: bool | Unset = UNSET,

) -> GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500 | None:
    """ Gets a list of user AWS keys.

    Args:
        include_all (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500
     """


    return sync_detailed(
        client=client,
include_all=include_all,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    include_all: bool | Unset = UNSET,

) -> Response[GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500]:
    """ Gets a list of user AWS keys.

    Args:
        include_all (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500]
     """


    kwargs = _get_kwargs(
        include_all=include_all,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    include_all: bool | Unset = UNSET,

) -> GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500 | None:
    """ Gets a list of user AWS keys.

    Args:
        include_all (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllUserAwsKeysResponse200 | GetAllUserAwsKeysResponse400 | GetAllUserAwsKeysResponse401 | GetAllUserAwsKeysResponse403 | GetAllUserAwsKeysResponse500
     """


    return (await asyncio_detailed(
        client=client,
include_all=include_all,

    )).parsed
