/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Get Item
     * @param skip
     * @param limit
     * @param q
     * @param type
     * @param exterior
     * @param quality
     * @param category
     * @param weaponType
     * @param collection
     * @param minPrice
     * @param maxPrice
     * @param minReleaseYear
     * @param maxReleaseYear
     * @param justReturnMatchCount
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getItemShopGet(
        skip?: number,
        limit: number = 100,
        q?: string,
        type?: Array<string>,
        exterior?: Array<string>,
        quality?: Array<string>,
        category?: Array<string>,
        weaponType?: Array<string>,
        collection?: Array<string>,
        minPrice?: number,
        maxPrice?: number,
        minReleaseYear?: number,
        maxReleaseYear?: number,
        justReturnMatchCount: boolean = false,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/shop/',
            query: {
                'skip': skip,
                'limit': limit,
                'q': q,
                'type': type,
                'exterior': exterior,
                'quality': quality,
                'category': category,
                'weapon_type': weaponType,
                'collection': collection,
                'min_price': minPrice,
                'max_price': maxPrice,
                'min_release_year': minReleaseYear,
                'max_release_year': maxReleaseYear,
                'just_return_match_count': justReturnMatchCount,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Get Inventory
     * @param steamid
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getInventoryDepotGetGet(
        steamid: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/depot/get/',
            query: {
                'steamid': steamid,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
