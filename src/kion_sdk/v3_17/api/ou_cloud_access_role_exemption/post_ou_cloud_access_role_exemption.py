from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ou_cloud_access_role_exemption import OUCloudAccessRoleExemption
from ...models.post_ou_cloud_access_role_exemption_response_201 import PostOUCloudAccessRoleExemptionResponse201
from ...models.post_ou_cloud_access_role_exemption_response_400 import PostOUCloudAccessRoleExemptionResponse400
from ...models.post_ou_cloud_access_role_exemption_response_401 import PostOUCloudAccessRoleExemptionResponse401
from ...models.post_ou_cloud_access_role_exemption_response_403 import PostOUCloudAccessRoleExemptionResponse403
from ...models.post_ou_cloud_access_role_exemption_response_422 import PostOUCloudAccessRoleExemptionResponse422
from ...models.post_ou_cloud_access_role_exemption_response_500 import PostOUCloudAccessRoleExemptionResponse500
from typing import cast



def _get_kwargs(
    *,
    body: OUCloudAccessRoleExemption,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ou-cloud-access-role-exemption",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500 | None:
    if response.status_code == 201:
        response_201 = PostOUCloudAccessRoleExemptionResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostOUCloudAccessRoleExemptionResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostOUCloudAccessRoleExemptionResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostOUCloudAccessRoleExemptionResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostOUCloudAccessRoleExemptionResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostOUCloudAccessRoleExemptionResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: OUCloudAccessRoleExemption,

) -> Response[PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500]:
    """ Creates a new Exemption of an OU from an inherited ou cloud access role in the application.

    Args:
        body (OUCloudAccessRoleExemption): OUCloudAccessRoleExemption defines an exemption of an
            ou cloud access role for an ou.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500]
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
    body: OUCloudAccessRoleExemption,

) -> PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500 | None:
    """ Creates a new Exemption of an OU from an inherited ou cloud access role in the application.

    Args:
        body (OUCloudAccessRoleExemption): OUCloudAccessRoleExemption defines an exemption of an
            ou cloud access role for an ou.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: OUCloudAccessRoleExemption,

) -> Response[PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500]:
    """ Creates a new Exemption of an OU from an inherited ou cloud access role in the application.

    Args:
        body (OUCloudAccessRoleExemption): OUCloudAccessRoleExemption defines an exemption of an
            ou cloud access role for an ou.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500]
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
    body: OUCloudAccessRoleExemption,

) -> PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500 | None:
    """ Creates a new Exemption of an OU from an inherited ou cloud access role in the application.

    Args:
        body (OUCloudAccessRoleExemption): OUCloudAccessRoleExemption defines an exemption of an
            ou cloud access role for an ou.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostOUCloudAccessRoleExemptionResponse201 | PostOUCloudAccessRoleExemptionResponse400 | PostOUCloudAccessRoleExemptionResponse401 | PostOUCloudAccessRoleExemptionResponse403 | PostOUCloudAccessRoleExemptionResponse422 | PostOUCloudAccessRoleExemptionResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
