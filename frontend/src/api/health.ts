import { apiClient } from "./client";

type Health = {
    status: string;
}

export async function getHealth():Promise<Health>{
    const r = await apiClient.get("/health");
    return r.data;
}