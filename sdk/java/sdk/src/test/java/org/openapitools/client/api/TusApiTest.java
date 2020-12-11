/*
 * 
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.io.File;
import org.openapitools.client.model.InlineResponse400;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for TusApi
 */
@Ignore
public class TusApiTest {

    private final TusApi api = new TusApi();

    
    /**
     * 
     *
     * Transfer file data
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void tusUploadSessionUploadSessionIdUploadGuidPATCHTest() throws ApiException {
        String uploadSessionId = null;
        String guid = null;
        Integer uploadOffset = null;
        String tusResumable = null;
        Boolean force = null;
        File body = null;
        InlineResponse400 response = api.tusUploadSessionUploadSessionIdUploadGuidPATCH(uploadSessionId, guid, uploadOffset, tusResumable, force, body);

        // TODO: test validations
    }
    
    /**
     * 
     *
     * Create an Upload
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void tusUploadSessionUploadSessionIdUploadPOSTTest() throws ApiException {
        String uploadSessionId = null;
        Integer uploadLength = null;
        String uploadMetadata = null;
        String tusResumable = null;
        Boolean force = null;
        Object body = null;
        api.tusUploadSessionUploadSessionIdUploadPOST(uploadSessionId, uploadLength, uploadMetadata, tusResumable, force, body);

        // TODO: test validations
    }
    
}