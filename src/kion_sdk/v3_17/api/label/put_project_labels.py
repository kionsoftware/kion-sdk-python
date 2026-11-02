from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.associate_labels import AssociateLabels
from ...models.put_project_labels_response_200 import PutProjectLabelsResponse200
from ...models.put_project_labels_response_400 import PutProjectLabelsResponse400
from ...models.put_project_labels_response_401 import PutProjectLabelsResponse401
from ...models.put_project_labels_response_404 import PutProjectLabelsResponse404
from ...models.put_project_labels_response_422 import PutProjectLabelsResponse422
from ...models.put_project_labels_response_500 import PutProjectLabelsResponse500
from typing import cast



def _get_kwargs(
    project_id: int,
    *,
    body: AssociateLabels,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v3/project/{project_id}/labels".format(project_id=quote(str(project_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500 | None:
    if response.status_code == 200:
        response_200 = PutProjectLabelsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = PutProjectLabelsResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = PutProjectLabelsResponse401.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = PutProjectLabelsResponse404.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = PutProjectLabelsResponse422.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = PutProjectLabelsResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> Response[PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500]:
    """ Replaces labels on the given project.

     This replaces labels on the given project with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        project_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500 | None:
    """ Replaces labels on the given project.

     This replaces labels on the given project with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        project_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500
     """


    return sync_detailed(
        project_id=project_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    project_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> Response[PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500]:
    """ Replaces labels on the given project.

     This replaces labels on the given project with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        project_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id: int,
    *,
    client: AuthenticatedClient,
    body: AssociateLabels,

) -> PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500 | None:
    """ Replaces labels on the given project.

     This replaces labels on the given project with the provided labels.
    The labels must already exist.
    You may pass just the label ID, or just the key/value pair for each label.

    Args:
        project_id (int):
        body (AssociateLabels):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PutProjectLabelsResponse200 | PutProjectLabelsResponse400 | PutProjectLabelsResponse401 | PutProjectLabelsResponse404 | PutProjectLabelsResponse422 | PutProjectLabelsResponse500
     """


    return (await asyncio_detailed(
        project_id=project_id,
client=client,
body=body,

    )).parsed
