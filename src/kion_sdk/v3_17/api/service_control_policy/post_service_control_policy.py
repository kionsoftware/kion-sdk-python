from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_service_control_policy_response_201 import PostServiceControlPolicyResponse201
from ...models.post_service_control_policy_response_400 import PostServiceControlPolicyResponse400
from ...models.post_service_control_policy_response_401 import PostServiceControlPolicyResponse401
from ...models.post_service_control_policy_response_403 import PostServiceControlPolicyResponse403
from ...models.post_service_control_policy_response_422 import PostServiceControlPolicyResponse422
from ...models.post_service_control_policy_response_500 import PostServiceControlPolicyResponse500
from ...models.service_control_policy_create import ServiceControlPolicyCreate
from typing import cast



def _get_kwargs(
    *,
    body: ServiceControlPolicyCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/service-control-policy",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500 | None:
    if response.status_code == 201:
        response_201 = PostServiceControlPolicyResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostServiceControlPolicyResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostServiceControlPolicyResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostServiceControlPolicyResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostServiceControlPolicyResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostServiceControlPolicyResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceControlPolicyCreate,

) -> Response[PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500]:
    """ Creates an Service Control Policy in the application.

    Args:
        body (ServiceControlPolicyCreate): ServiceControlPolicyCreate defines an Service Control
            policy creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500]
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
    body: ServiceControlPolicyCreate,

) -> PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500 | None:
    """ Creates an Service Control Policy in the application.

    Args:
        body (ServiceControlPolicyCreate): ServiceControlPolicyCreate defines an Service Control
            policy creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ServiceControlPolicyCreate,

) -> Response[PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500]:
    """ Creates an Service Control Policy in the application.

    Args:
        body (ServiceControlPolicyCreate): ServiceControlPolicyCreate defines an Service Control
            policy creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500]
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
    body: ServiceControlPolicyCreate,

) -> PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500 | None:
    """ Creates an Service Control Policy in the application.

    Args:
        body (ServiceControlPolicyCreate): ServiceControlPolicyCreate defines an Service Control
            policy creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostServiceControlPolicyResponse201 | PostServiceControlPolicyResponse400 | PostServiceControlPolicyResponse401 | PostServiceControlPolicyResponse403 | PostServiceControlPolicyResponse422 | PostServiceControlPolicyResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
