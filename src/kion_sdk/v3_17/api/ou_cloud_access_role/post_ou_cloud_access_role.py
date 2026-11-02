from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ou_cloud_access_role_create import OUCloudAccessRoleCreate
from ...models.post_ou_cloud_access_role_response_201 import PostOUCloudAccessRoleResponse201
from ...models.post_ou_cloud_access_role_response_400 import PostOUCloudAccessRoleResponse400
from ...models.post_ou_cloud_access_role_response_401 import PostOUCloudAccessRoleResponse401
from ...models.post_ou_cloud_access_role_response_403 import PostOUCloudAccessRoleResponse403
from ...models.post_ou_cloud_access_role_response_422 import PostOUCloudAccessRoleResponse422
from ...models.post_ou_cloud_access_role_response_500 import PostOUCloudAccessRoleResponse500
from typing import cast



def _get_kwargs(
    *,
    body: OUCloudAccessRoleCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ou-cloud-access-role",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOUCloudAccessRoleResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOUCloudAccessRoleResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOUCloudAccessRoleResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOUCloudAccessRoleResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostOUCloudAccessRoleResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOUCloudAccessRoleResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OUCloudAccessRoleCreate,

) -> Response[PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500]:
    """ Creates a new ou cloud access role in the application.

     The optional `cloud_access_role_type_id` field selects the role type:
    1 = User (default, multi-cloud, assumable by Kion users/groups),
    2 = Custom Trust (AWS-only; requires `aws_iam_role_trust_policy`),
    3 = Account (AWS-only; requires `aws_trusted_account_numbers`),
    4 = Service (AWS-only; requires `aws_trusted_services`).
    Non-User CAR types are AWS-only and reject user/group, Azure, or GCP
    associations. `web_access`, `short_term_access_keys`, and `long_term_access_keys`
    are forced to false for non-User types.

    Args:
        body (OUCloudAccessRoleCreate): OUCloudAccessRoleCreate defines the json structure for the
            ou cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: OUCloudAccessRoleCreate,

) -> PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500 | None:
    """ Creates a new ou cloud access role in the application.

     The optional `cloud_access_role_type_id` field selects the role type:
    1 = User (default, multi-cloud, assumable by Kion users/groups),
    2 = Custom Trust (AWS-only; requires `aws_iam_role_trust_policy`),
    3 = Account (AWS-only; requires `aws_trusted_account_numbers`),
    4 = Service (AWS-only; requires `aws_trusted_services`).
    Non-User CAR types are AWS-only and reject user/group, Azure, or GCP
    associations. `web_access`, `short_term_access_keys`, and `long_term_access_keys`
    are forced to false for non-User types.

    Args:
        body (OUCloudAccessRoleCreate): OUCloudAccessRoleCreate defines the json structure for the
            ou cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OUCloudAccessRoleCreate,

) -> Response[PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500]:
    """ Creates a new ou cloud access role in the application.

     The optional `cloud_access_role_type_id` field selects the role type:
    1 = User (default, multi-cloud, assumable by Kion users/groups),
    2 = Custom Trust (AWS-only; requires `aws_iam_role_trust_policy`),
    3 = Account (AWS-only; requires `aws_trusted_account_numbers`),
    4 = Service (AWS-only; requires `aws_trusted_services`).
    Non-User CAR types are AWS-only and reject user/group, Azure, or GCP
    associations. `web_access`, `short_term_access_keys`, and `long_term_access_keys`
    are forced to false for non-User types.

    Args:
        body (OUCloudAccessRoleCreate): OUCloudAccessRoleCreate defines the json structure for the
            ou cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: OUCloudAccessRoleCreate,

) -> PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500 | None:
    """ Creates a new ou cloud access role in the application.

     The optional `cloud_access_role_type_id` field selects the role type:
    1 = User (default, multi-cloud, assumable by Kion users/groups),
    2 = Custom Trust (AWS-only; requires `aws_iam_role_trust_policy`),
    3 = Account (AWS-only; requires `aws_trusted_account_numbers`),
    4 = Service (AWS-only; requires `aws_trusted_services`).
    Non-User CAR types are AWS-only and reject user/group, Azure, or GCP
    associations. `web_access`, `short_term_access_keys`, and `long_term_access_keys`
    are forced to false for non-User types.

    Args:
        body (OUCloudAccessRoleCreate): OUCloudAccessRoleCreate defines the json structure for the
            ou cloud access role's create action.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOUCloudAccessRoleResponse201 | PostOUCloudAccessRoleResponse400 | PostOUCloudAccessRoleResponse401 | PostOUCloudAccessRoleResponse403 | PostOUCloudAccessRoleResponse422 | PostOUCloudAccessRoleResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
