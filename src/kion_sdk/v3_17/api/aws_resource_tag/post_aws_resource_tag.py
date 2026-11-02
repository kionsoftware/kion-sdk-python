from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.aws_resource_tag_create import AWSResourceTagCreate
from ...models.post_aws_resource_tag_response_201 import PostAWSResourceTagResponse201
from ...models.post_aws_resource_tag_response_400 import PostAWSResourceTagResponse400
from ...models.post_aws_resource_tag_response_401 import PostAWSResourceTagResponse401
from ...models.post_aws_resource_tag_response_403 import PostAWSResourceTagResponse403
from ...models.post_aws_resource_tag_response_422 import PostAWSResourceTagResponse422
from ...models.post_aws_resource_tag_response_500 import PostAWSResourceTagResponse500
from typing import cast



def _get_kwargs(
    *,
    body: AWSResourceTagCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/aws-resource-tag",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500 | None:
    if response.status_code == 201:
        response_201 = PostAWSResourceTagResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostAWSResourceTagResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostAWSResourceTagResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostAWSResourceTagResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostAWSResourceTagResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostAWSResourceTagResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSResourceTagCreate,

) -> Response[PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500]:
    """ Creates an AWS Resource Tag in the application.

    Args:
        body (AWSResourceTagCreate): AWSResourceTagCreate defines an AWS Resource Tag creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500]
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
    body: AWSResourceTagCreate,

) -> PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500 | None:
    """ Creates an AWS Resource Tag in the application.

    Args:
        body (AWSResourceTagCreate): AWSResourceTagCreate defines an AWS Resource Tag creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: AWSResourceTagCreate,

) -> Response[PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500]:
    """ Creates an AWS Resource Tag in the application.

    Args:
        body (AWSResourceTagCreate): AWSResourceTagCreate defines an AWS Resource Tag creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500]
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
    body: AWSResourceTagCreate,

) -> PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500 | None:
    """ Creates an AWS Resource Tag in the application.

    Args:
        body (AWSResourceTagCreate): AWSResourceTagCreate defines an AWS Resource Tag creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostAWSResourceTagResponse201 | PostAWSResourceTagResponse400 | PostAWSResourceTagResponse401 | PostAWSResourceTagResponse403 | PostAWSResourceTagResponse422 | PostAWSResourceTagResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
