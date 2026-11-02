from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.iam_policy_add_owners_response_200 import IAMPolicyAddOwnersResponse200
from ...models.iam_policy_add_owners_response_400 import IAMPolicyAddOwnersResponse400
from ...models.iam_policy_add_owners_response_401 import IAMPolicyAddOwnersResponse401
from ...models.iam_policy_add_owners_response_403 import IAMPolicyAddOwnersResponse403
from ...models.iam_policy_add_owners_response_404 import IAMPolicyAddOwnersResponse404
from ...models.iam_policy_add_owners_response_422 import IAMPolicyAddOwnersResponse422
from ...models.iam_policy_add_owners_response_500 import IAMPolicyAddOwnersResponse500
from ...models.policy_owners import PolicyOwners
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: PolicyOwners,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/iam-policy/{id}/owner".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500 | None:
    if response.status_code == 200:
        response_200 = IAMPolicyAddOwnersResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = IAMPolicyAddOwnersResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = IAMPolicyAddOwnersResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = IAMPolicyAddOwnersResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = IAMPolicyAddOwnersResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = IAMPolicyAddOwnersResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = IAMPolicyAddOwnersResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500]:
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
    body: PolicyOwners,

) -> Response[IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500]:
    """ Adds users and groups as owners of the IAM policy in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PolicyOwners,

) -> IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500 | None:
    """ Adds users and groups as owners of the IAM policy in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PolicyOwners,

) -> Response[IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500]:
    """ Adds users and groups as owners of the IAM policy in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PolicyOwners,

) -> IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500 | None:
    """ Adds users and groups as owners of the IAM policy in the application.

    Args:
        id (int):
        body (PolicyOwners): PolicyOwners defines user and group ID lists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IAMPolicyAddOwnersResponse200 | IAMPolicyAddOwnersResponse400 | IAMPolicyAddOwnersResponse401 | IAMPolicyAddOwnersResponse403 | IAMPolicyAddOwnersResponse404 | IAMPolicyAddOwnersResponse422 | IAMPolicyAddOwnersResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
