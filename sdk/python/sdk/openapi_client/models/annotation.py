# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class Annotation(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pk': 'int',
        'document': 'int',
        'field': 'str',
        'value': 'object',
        'location_start': 'int',
        'location_end': 'int',
        'location_text': 'str',
        'modified_by': 'int',
        'modified_date': 'datetime'
    }

    attribute_map = {
        'pk': 'pk',
        'document': 'document',
        'field': 'field',
        'value': 'value',
        'location_start': 'location_start',
        'location_end': 'location_end',
        'location_text': 'location_text',
        'modified_by': 'modified_by',
        'modified_date': 'modified_date'
    }

    def __init__(self, pk=None, document=None, field=None, value=None, location_start=None, location_end=None, location_text=None, modified_by=None, modified_date=None, local_vars_configuration=None):  # noqa: E501
        """Annotation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pk = None
        self._document = None
        self._field = None
        self._value = None
        self._location_start = None
        self._location_end = None
        self._location_text = None
        self._modified_by = None
        self._modified_date = None
        self.discriminator = None

        if pk is not None:
            self.pk = pk
        self.document = document
        self.field = field
        self.value = value
        self.location_start = location_start
        self.location_end = location_end
        self.location_text = location_text
        self.modified_by = modified_by
        if modified_date is not None:
            self.modified_date = modified_date

    @property
    def pk(self):
        """Gets the pk of this Annotation.  # noqa: E501


        :return: The pk of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._pk

    @pk.setter
    def pk(self, pk):
        """Sets the pk of this Annotation.


        :param pk: The pk of this Annotation.  # noqa: E501
        :type pk: int
        """

        self._pk = pk

    @property
    def document(self):
        """Gets the document of this Annotation.  # noqa: E501


        :return: The document of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this Annotation.


        :param document: The document of this Annotation.  # noqa: E501
        :type document: int
        """
        if self.local_vars_configuration.client_side_validation and document is None:  # noqa: E501
            raise ValueError("Invalid value for `document`, must not be `None`")  # noqa: E501

        self._document = document

    @property
    def field(self):
        """Gets the field of this Annotation.  # noqa: E501


        :return: The field of this Annotation.  # noqa: E501
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """Sets the field of this Annotation.


        :param field: The field of this Annotation.  # noqa: E501
        :type field: str
        """
        if self.local_vars_configuration.client_side_validation and field is None:  # noqa: E501
            raise ValueError("Invalid value for `field`, must not be `None`")  # noqa: E501

        self._field = field

    @property
    def value(self):
        """Gets the value of this Annotation.  # noqa: E501


        :return: The value of this Annotation.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Annotation.


        :param value: The value of this Annotation.  # noqa: E501
        :type value: object
        """

        self._value = value

    @property
    def location_start(self):
        """Gets the location_start of this Annotation.  # noqa: E501


        :return: The location_start of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._location_start

    @location_start.setter
    def location_start(self, location_start):
        """Sets the location_start of this Annotation.


        :param location_start: The location_start of this Annotation.  # noqa: E501
        :type location_start: int
        """
        if (self.local_vars_configuration.client_side_validation and
                location_start is not None and location_start > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `location_start`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                location_start is not None and location_start < 0):  # noqa: E501
            raise ValueError("Invalid value for `location_start`, must be a value greater than or equal to `0`")  # noqa: E501

        self._location_start = location_start

    @property
    def location_end(self):
        """Gets the location_end of this Annotation.  # noqa: E501


        :return: The location_end of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._location_end

    @location_end.setter
    def location_end(self, location_end):
        """Sets the location_end of this Annotation.


        :param location_end: The location_end of this Annotation.  # noqa: E501
        :type location_end: int
        """
        if (self.local_vars_configuration.client_side_validation and
                location_end is not None and location_end > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `location_end`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                location_end is not None and location_end < 0):  # noqa: E501
            raise ValueError("Invalid value for `location_end`, must be a value greater than or equal to `0`")  # noqa: E501

        self._location_end = location_end

    @property
    def location_text(self):
        """Gets the location_text of this Annotation.  # noqa: E501


        :return: The location_text of this Annotation.  # noqa: E501
        :rtype: str
        """
        return self._location_text

    @location_text.setter
    def location_text(self, location_text):
        """Sets the location_text of this Annotation.


        :param location_text: The location_text of this Annotation.  # noqa: E501
        :type location_text: str
        """

        self._location_text = location_text

    @property
    def modified_by(self):
        """Gets the modified_by of this Annotation.  # noqa: E501


        :return: The modified_by of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Annotation.


        :param modified_by: The modified_by of this Annotation.  # noqa: E501
        :type modified_by: int
        """

        self._modified_by = modified_by

    @property
    def modified_date(self):
        """Gets the modified_date of this Annotation.  # noqa: E501


        :return: The modified_date of this Annotation.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this Annotation.


        :param modified_date: The modified_date of this Annotation.  # noqa: E501
        :type modified_date: datetime
        """

        self._modified_date = modified_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Annotation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Annotation):
            return True

        return self.to_dict() != other.to_dict()