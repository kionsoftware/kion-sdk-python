from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_gcp_project_body import CreateGCPProjectBody
from ...models.create_gcp_project_response_200 import CreateGCPProjectResponse200
from ...models.create_gcp_project_response_400 import CreateGCPProjectResponse400
from ...models.create_gcp_project_response_401 import CreateGCPProjectResponse401
from ...models.create_gcp_project_response_403 import CreateGCPProjectResponse403
from ...models.create_gcp_project_response_500 import CreateGCPProjectResponse500
from typing import cast



def _get_kwargs(
    *,
    body: CreateGCPProjectBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v3/gcp-resources/project",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500 | None:
    if response.status_code == 200:
        response_200 = CreateGCPProjectResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = CreateGCPProjectResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = CreateGCPProjectResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = CreateGCPProjectResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 500:
        response_500 = CreateGCPProjectResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateGCPProjectBody,

) -> Response[CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500]:
    """ Creates a Google cloud project.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=google-cloud instead.

    Args:
        body (CreateGCPProjectBody): CreateGCPProjectBody represents the parameters required to
            create a new google cloud project

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500]
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
    body: CreateGCPProjectBody,

) -> CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500 | None:
    """ Creates a Google cloud project.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=google-cloud instead.

    Args:
        body (CreateGCPProjectBody): CreateGCPProjectBody represents the parameters required to
            create a new google cloud project

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateGCPProjectBody,

) -> Response[CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500]:
    """ Creates a Google cloud project.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=google-cloud instead.

    Args:
        body (CreateGCPProjectBody): CreateGCPProjectBody represents the parameters required to
            create a new google cloud project

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500]
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
    body: CreateGCPProjectBody,

) -> CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500 | None:
    """ Creates a Google cloud project.

     This is deprecated but retained for backwards compatibility.
    Use POST /v3/account-cache/create?account-type=google-cloud instead.

    Args:
        body (CreateGCPProjectBody): CreateGCPProjectBody represents the parameters required to
            create a new google cloud project

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateGCPProjectResponse200 | CreateGCPProjectResponse400 | CreateGCPProjectResponse401 | CreateGCPProjectResponse403 | CreateGCPProjectResponse500
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
