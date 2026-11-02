from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.ami_create import AMICreate
from ...models.post_ami_response_201 import PostAMIResponse201
from ...models.post_ami_response_400 import PostAMIResponse400
from ...models.post_ami_response_401 import PostAMIResponse401
from ...models.post_ami_response_403 import PostAMIResponse403
from ...models.post_ami_response_422 import PostAMIResponse422
from ...models.post_ami_response_500 import PostAMIResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AMICreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/ami",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAMIResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAMIResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAMIResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAMIResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAMIResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAMIResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AMICreate,

) -> Response[PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500]:
    """ Registers an AMI with the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        body (AMICreate): AMICreate defines an AMI creation where the AMI lives in an account
            managed by cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500]
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
    body: AMICreate,

) -> PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500 | None:
    """ Registers an AMI with the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        body (AMICreate): AMICreate defines an AMI creation where the AMI lives in an account
            managed by cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AMICreate,

) -> Response[PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500]:
    """ Registers an AMI with the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        body (AMICreate): AMICreate defines an AMI creation where the AMI lives in an account
            managed by cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500]
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
    body: AMICreate,

) -> PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500 | None:
    """ Registers an AMI with the application.

     AMIs exist in AWS accounts that are attached to a project.

    Args:
        body (AMICreate): AMICreate defines an AMI creation where the AMI lives in an account
            managed by cloudtamer.io.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAMIResponse201 | PostAMIResponse400 | PostAMIResponse401 | PostAMIResponse403 | PostAMIResponse422 | PostAMIResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
