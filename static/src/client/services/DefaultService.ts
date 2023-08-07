/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { ItemWithVendorOffers } from '../models/ItemWithVendorOffers';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class DefaultService {

    /**
     * Get Item
     * @param marketHashName 
     * @returns ItemWithVendorOffers Successful Response
     * @throws ApiError
     */
    public static getItemItemsGetMarketHashNameGet(
marketHashName: string,
): CancelablePromise<ItemWithVendorOffers> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/items/get/{market_hash_name}',
            path: {
                'market_hash_name': marketHashName,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

    /**
     * Search
     * @param q Search query
     * @param rarity Rarity filter
     * @param discontinued Discontinued filter
     * @param minPrice Minimum price
     * @param maxPrice Maximum price
     * @param minYear Minimum release year
     * @param maxYear Maximum release year
     * @returns any Successful Response
     * @throws ApiError
     */
    public static searchItemsSearchGet(
q?: (string | null),
rarity?: (string | null),
discontinued?: (boolean | null),
minPrice?: (number | null),
maxPrice?: (number | null),
minYear?: (number | null),
maxYear?: (number | null),
): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/items/search/',
            query: {
                'q': q,
                'rarity': rarity,
                'discontinued': discontinued,
                'min_price': minPrice,
                'max_price': maxPrice,
                'min_year': minYear,
                'max_year': maxYear,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }

}
