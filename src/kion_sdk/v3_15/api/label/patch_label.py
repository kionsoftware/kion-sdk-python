from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.patch_label_response_200 import PatchLabelResponse200
from ...models.patch_label_response_400 import PatchLabelResponse400
from ...models.patch_label_response_403 import PatchLabelResponse403
from ...models.patch_label_response_422 import PatchLabelResponse422
from ...models.patch_label_response_500 import PatchLabelResponse500
from ...models.update_label import UpdateLabel
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: UpdateLabel | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v3/label/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500 | None:
    if response.status_code == 200:
        response_200 = PatchLabelResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PatchLabelResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = PatchLabelResponse403.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = PatchLabelResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PatchLabelResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500]:
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
    body: UpdateLabel | Unset = UNSET,

) -> Response[PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500]:
    """ Updates an app label in the application.

     Can also be used as /v3/label?key={key}&value={value}.

    Args:
        id (int):
        body (UpdateLabel | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500]
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
    body: UpdateLabel | Unset = UNSET,

) -> PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500 | None:
    """ Updates an app label in the application.

     Can also be used as /v3/label?key={key}&value={value}.

    Args:
        id (int):
        body (UpdateLabel | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500
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
    body: UpdateLabel | Unset = UNSET,

) -> Response[PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500]:
    """ Updates an app label in the application.

     Can also be used as /v3/label?key={key}&value={value}.

    Args:
        id (int):
        body (UpdateLabel | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500]
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
    body: UpdateLabel | Unset = UNSET,

) -> PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500 | None:
    """ Updates an app label in the application.

     Can also be used as /v3/label?key={key}&value={value}.

    Args:
        id (int):
        body (UpdateLabel | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PatchLabelResponse200 | PatchLabelResponse400 | PatchLabelResponse403 | PatchLabelResponse422 | PatchLabelResponse500
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
