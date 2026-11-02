from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_project_line_item_response_200 import PostProjectLineItemResponse200
from ...models.post_project_line_item_response_400 import PostProjectLineItemResponse400
from ...models.post_project_line_item_response_401 import PostProjectLineItemResponse401
from ...models.post_project_line_item_response_403 import PostProjectLineItemResponse403
from ...models.post_project_line_item_response_422 import PostProjectLineItemResponse422
from ...models.post_project_line_item_response_500 import PostProjectLineItemResponse500
from ...models.project_line_item_create import ProjectLineItemCreate
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ProjectLineItemCreate | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/project-line-item",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500 | None:
    if response.status_code == 200:
        response_200 = PostProjectLineItemResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostProjectLineItemResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostProjectLineItemResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostProjectLineItemResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostProjectLineItemResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostProjectLineItemResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectLineItemCreate | Unset = UNSET,

) -> Response[PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500]:
    """ inserts one project line item.

    Args:
        body (ProjectLineItemCreate | Unset): ProjectLineItemCreate defines a project line item
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500]
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
    body: ProjectLineItemCreate | Unset = UNSET,

) -> PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500 | None:
    """ inserts one project line item.

    Args:
        body (ProjectLineItemCreate | Unset): ProjectLineItemCreate defines a project line item
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectLineItemCreate | Unset = UNSET,

) -> Response[PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500]:
    """ inserts one project line item.

    Args:
        body (ProjectLineItemCreate | Unset): ProjectLineItemCreate defines a project line item
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500]
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
    body: ProjectLineItemCreate | Unset = UNSET,

) -> PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500 | None:
    """ inserts one project line item.

    Args:
        body (ProjectLineItemCreate | Unset): ProjectLineItemCreate defines a project line item
            creation.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostProjectLineItemResponse200 | PostProjectLineItemResponse400 | PostProjectLineItemResponse401 | PostProjectLineItemResponse403 | PostProjectLineItemResponse422 | PostProjectLineItemResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
