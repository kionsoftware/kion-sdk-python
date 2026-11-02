from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_destination_url import CreateDestinationURL
from ...models.post_destination_url_response_201 import PostDestinationURLResponse201
from ...models.post_destination_url_response_400 import PostDestinationURLResponse400
from ...models.post_destination_url_response_401 import PostDestinationURLResponse401
from ...models.post_destination_url_response_403 import PostDestinationURLResponse403
from ...models.post_destination_url_response_422 import PostDestinationURLResponse422
from ...models.post_destination_url_response_500 import PostDestinationURLResponse500
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CreateDestinationURL | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/idms/{id}/destination-url".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500 | None:
    if response.status_code == 201:
        response_201 = PostDestinationURLResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostDestinationURLResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostDestinationURLResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostDestinationURLResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostDestinationURLResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostDestinationURLResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500]:
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
    body: CreateDestinationURL | Unset = UNSET,

) -> Response[PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500]:
    """ Adds a new supported destination url for a saml idms.

    Args:
        id (int):
        body (CreateDestinationURL | Unset): CreateDestinationURL defines an additional
            destination url to validate a saml idms against

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500]
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
    body: CreateDestinationURL | Unset = UNSET,

) -> PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500 | None:
    """ Adds a new supported destination url for a saml idms.

    Args:
        id (int):
        body (CreateDestinationURL | Unset): CreateDestinationURL defines an additional
            destination url to validate a saml idms against

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500
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
    body: CreateDestinationURL | Unset = UNSET,

) -> Response[PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500]:
    """ Adds a new supported destination url for a saml idms.

    Args:
        id (int):
        body (CreateDestinationURL | Unset): CreateDestinationURL defines an additional
            destination url to validate a saml idms against

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500]
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
    body: CreateDestinationURL | Unset = UNSET,

) -> PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500 | None:
    """ Adds a new supported destination url for a saml idms.

    Args:
        id (int):
        body (CreateDestinationURL | Unset): CreateDestinationURL defines an additional
            destination url to validate a saml idms against

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostDestinationURLResponse201 | PostDestinationURLResponse400 | PostDestinationURLResponse401 | PostDestinationURLResponse403 | PostDestinationURLResponse422 | PostDestinationURLResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
