import { AxiosResponse } from "axios"

export type Detail = {
    "type": string,
    "loc": string[],
    "msg": string,
    "input": string,
    "url": string
}

export type Data = {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    "data": any,
    "message": string,
    "status_code": number
}

export function GetBody(response: AxiosResponse) {
    return response.data
}
export function GetDetail(data: object): Detail {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    return (data as any).detail[0]
}

export function GetData(response: AxiosResponse): Data{
    return response.data
}