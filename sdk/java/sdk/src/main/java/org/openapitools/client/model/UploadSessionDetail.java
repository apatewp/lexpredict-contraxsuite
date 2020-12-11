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


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.UUID;
import org.openapitools.client.model.TaskQueueReviewersData;
import org.openapitools.client.model.UploadSessionDetailProject;
import org.threeten.bp.OffsetDateTime;

/**
 * UploadSessionDetail
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2020-12-11T16:57:55.511+03:00[Europe/Moscow]")
public class UploadSessionDetail {
  public static final String SERIALIZED_NAME_UID = "uid";
  @SerializedName(SERIALIZED_NAME_UID)
  private UUID uid;

  public static final String SERIALIZED_NAME_PROJECT = "project";
  @SerializedName(SERIALIZED_NAME_PROJECT)
  private UploadSessionDetailProject project;

  public static final String SERIALIZED_NAME_CREATED_BY = "created_by";
  @SerializedName(SERIALIZED_NAME_CREATED_BY)
  private TaskQueueReviewersData createdBy;

  public static final String SERIALIZED_NAME_CREATED_DATE = "created_date";
  @SerializedName(SERIALIZED_NAME_CREATED_DATE)
  private OffsetDateTime createdDate;

  public static final String SERIALIZED_NAME_DOCUMENT_TYPE = "document_type";
  @SerializedName(SERIALIZED_NAME_DOCUMENT_TYPE)
  private String documentType;

  public static final String SERIALIZED_NAME_PROGRESS = "progress";
  @SerializedName(SERIALIZED_NAME_PROGRESS)
  private String progress;


   /**
   * Get uid
   * @return uid
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public UUID getUid() {
    return uid;
  }




  public UploadSessionDetail project(UploadSessionDetailProject project) {
    
    this.project = project;
    return this;
  }

   /**
   * Get project
   * @return project
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public UploadSessionDetailProject getProject() {
    return project;
  }


  public void setProject(UploadSessionDetailProject project) {
    this.project = project;
  }


  public UploadSessionDetail createdBy(TaskQueueReviewersData createdBy) {
    
    this.createdBy = createdBy;
    return this;
  }

   /**
   * Get createdBy
   * @return createdBy
  **/
  @ApiModelProperty(required = true, value = "")

  public TaskQueueReviewersData getCreatedBy() {
    return createdBy;
  }


  public void setCreatedBy(TaskQueueReviewersData createdBy) {
    this.createdBy = createdBy;
  }


   /**
   * Get createdDate
   * @return createdDate
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public OffsetDateTime getCreatedDate() {
    return createdDate;
  }




   /**
   * Get documentType
   * @return documentType
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getDocumentType() {
    return documentType;
  }




   /**
   * Get progress
   * @return progress
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getProgress() {
    return progress;
  }




  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    UploadSessionDetail uploadSessionDetail = (UploadSessionDetail) o;
    return Objects.equals(this.uid, uploadSessionDetail.uid) &&
        Objects.equals(this.project, uploadSessionDetail.project) &&
        Objects.equals(this.createdBy, uploadSessionDetail.createdBy) &&
        Objects.equals(this.createdDate, uploadSessionDetail.createdDate) &&
        Objects.equals(this.documentType, uploadSessionDetail.documentType) &&
        Objects.equals(this.progress, uploadSessionDetail.progress);
  }

  @Override
  public int hashCode() {
    return Objects.hash(uid, project, createdBy, createdDate, documentType, progress);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class UploadSessionDetail {\n");
    sb.append("    uid: ").append(toIndentedString(uid)).append("\n");
    sb.append("    project: ").append(toIndentedString(project)).append("\n");
    sb.append("    createdBy: ").append(toIndentedString(createdBy)).append("\n");
    sb.append("    createdDate: ").append(toIndentedString(createdDate)).append("\n");
    sb.append("    documentType: ").append(toIndentedString(documentType)).append("\n");
    sb.append("    progress: ").append(toIndentedString(progress)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
