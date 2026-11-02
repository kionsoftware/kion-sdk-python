from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.funding_source_clone import FundingSourceClone
from ...models.post_funding_source_clone_response_201 import PostFundingSourceCloneResponse201
from ...models.post_funding_source_clone_response_400 import PostFundingSourceCloneResponse400
from ...models.post_funding_source_clone_response_401 import PostFundingSourceCloneResponse401
from ...models.post_funding_source_clone_response_403 import PostFundingSourceCloneResponse403
from ...models.post_funding_source_clone_response_422 import PostFundingSourceCloneResponse422
from ...models.post_funding_source_clone_response_500 import PostFundingSourceCloneResponse500
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: FundingSourceClone,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/funding-source/{id}/clone".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500 | None:
    if response.status_code == 201:
        response_201 = PostFundingSourceCloneResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = PostFundingSourceCloneResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostFundingSourceCloneResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = PostFundingSourceCloneResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PostFundingSourceCloneResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostFundingSourceCloneResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500]:
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
    body: FundingSourceClone,

) -> Response[PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500]:
    """ Clones a funding source in the application.

    Args:
        id (int):
        body (FundingSourceClone): FundingSourceClone defines the structure used for cloning an
            existing funding source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500]
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
    body: FundingSourceClone,

) -> PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500 | None:
    """ Clones a funding source in the application.

    Args:
        id (int):
        body (FundingSourceClone): FundingSourceClone defines the structure used for cloning an
            existing funding source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500
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
    body: FundingSourceClone,

) -> Response[PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500]:
    """ Clones a funding source in the application.

    Args:
        id (int):
        body (FundingSourceClone): FundingSourceClone defines the structure used for cloning an
            existing funding source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500]
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
    body: FundingSourceClone,

) -> PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500 | None:
    """ Clones a funding source in the application.

    Args:
        id (int):
        body (FundingSourceClone): FundingSourceClone defines the structure used for cloning an
            existing funding source.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostFundingSourceCloneResponse201 | PostFundingSourceCloneResponse400 | PostFundingSourceCloneResponse401 | PostFundingSourceCloneResponse403 | PostFundingSourceCloneResponse422 | PostFundingSourceCloneResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
