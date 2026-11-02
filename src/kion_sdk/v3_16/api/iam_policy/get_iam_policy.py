from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_iam_policy_response_200 import GetIAMPolicyResponse200
from ...models.get_iam_policy_response_401 import GetIAMPolicyResponse401
from ...models.get_iam_policy_response_403 import GetIAMPolicyResponse403
from ...models.get_iam_policy_response_404 import GetIAMPolicyResponse404
from ...models.get_iam_policy_response_500 import GetIAMPolicyResponse500
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v3/iam-policy/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500 | None:
    if response.status_code == 200:
        response_200 = GetIAMPolicyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = GetIAMPolicyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = GetIAMPolicyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = GetIAMPolicyResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = GetIAMPolicyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500]:
    """ Finds an IAM policy by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500 | None:
    """ Finds an IAM policy by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,

) -> Response[GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500]:
    """ Finds an IAM policy by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,

) -> GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500 | None:
    """ Finds an IAM policy by ID in the application.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetIAMPolicyResponse200 | GetIAMPolicyResponse401 | GetIAMPolicyResponse403 | GetIAMPolicyResponse404 | GetIAMPolicyResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
