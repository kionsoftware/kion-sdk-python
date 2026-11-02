from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_get_parse_params_response_200 import PostGETParseParamsResponse200
from ...models.post_get_parse_params_response_400 import PostGETParseParamsResponse400
from ...models.post_get_parse_params_response_401 import PostGETParseParamsResponse401
from ...models.post_get_parse_params_response_422 import PostGETParseParamsResponse422
from ...models.post_get_parse_params_response_500 import PostGETParseParamsResponse500
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/cft/parse-params",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500 | None:
    if response.status_code == 200:
        response_200 = PostGETParseParamsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PostGETParseParamsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PostGETParseParamsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = PostGETParseParamsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PostGETParseParamsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500]:
    """ Parses the parameters from an existing template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500 | None:
    """ Parses the parameters from an existing template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500]:
    """ Parses the parameters from an existing template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500 | None:
    """ Parses the parameters from an existing template.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostGETParseParamsResponse200 | PostGETParseParamsResponse400 | PostGETParseParamsResponse401 | PostGETParseParamsResponse422 | PostGETParseParamsResponse500
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
