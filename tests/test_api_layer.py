#!/usr/bin/env python
# -*- coding: utf-8 -*-


from unittest import TestCase
from util.tester import UtilTester


# https://realpython.com/blog/python/testing-third-party-apis-with-mocks/

class TestAPILayer(TestCase):

    def setUp(self):
        # create a tester passing the unittest self
        self.tester = UtilTester(self)

    # layer - get

    def test_get_api_layer_return_all_layers(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'properties': {'user_id_published_by': 1001, 'is_published': True, 'description': '',
                                   'name': 'Addresses in 1869', 'reference': [1001, 1002],
                                   'layer_id': 1001, 'f_table_name': 'layer_1001', 'source_description': '',
                                   'created_at': '2017-01-01 00:00:00', 'keyword': [1001, 1041]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': 1003, 'is_published': True, 'description': '',
                                   'name': 'Robberies between 1880 to 1900', 'reference': [1005],
                                   'layer_id': 1002, 'f_table_name': 'layer_1002', 'source_description': '',
                                   'created_at': '2017-03-05 00:00:00', 'keyword': [1010]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': None, 'is_published': False, 'description': '',
                                   'name': 'Streets in 1930', 'reference': [1010],
                                   'layer_id': 1003, 'f_table_name': 'layer_1003', 'source_description': '',
                                   'created_at': '2017-04-10 00:00:00', 'keyword': [1001, 1040]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': 1003, 'is_published': True, 'description': 'streets',
                                   'name': 'Streets in 1920', 'reference': None, 'layer_id': 1004,
                                   'f_table_name': 'layer_1004', 'source_description': '',
                                   'created_at': '2017-06-15 00:00:00', 'keyword': [1040]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': None, 'is_published': False, 'description': 'some hospitals',
                                   'name': 'Hospitals between 1800 to 1950', 'reference': None, 'layer_id': 1005,
                                   'f_table_name': 'layer_1005', 'source_description': None,
                                   'created_at': '2017-08-04 00:00:00', 'keyword': [1023]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': 1003, 'is_published': True, 'description': '',
                                   'name': 'Cinemas between 1900 to 1950', 'reference': [1025],
                                   'layer_id': 1006, 'f_table_name': 'layer_1006', 'source_description': None,
                                   'created_at': '2017-09-04 00:00:00', 'keyword': [1031]},
                    'type': 'Layer'
                }
            ]
        }

        self.tester.api_layer(expected)

    def test_get_api_layer_return_layer_by_layer_id(self):
        expected = {
            'features': [
                {
                    'properties': {'user_id_published_by': 1001, 'is_published': True, 'description': '',
                                   'name': 'Addresses in 1869', 'reference': [1001, 1002],
                                   'layer_id': 1001, 'f_table_name': 'layer_1001', 'source_description': '',
                                   'created_at': '2017-01-01 00:00:00', 'keyword': [1001, 1041]},
                    'type': 'Layer'
                },
            ],
            'type': 'FeatureCollection'
        }

        self.tester.api_layer(expected, layer_id="1001")

    def test_get_api_layer_return_layer_by_is_published(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'properties': {'user_id_published_by': 1001, 'is_published': True, 'description': '',
                                   'name': 'Addresses in 1869',
                                   'reference': [1001, 1002],
                                   'layer_id': 1001, 'f_table_name': 'layer_1001', 'source_description': '',
                                   'created_at': '2017-01-01 00:00:00', 'keyword': [1001, 1041]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': 1003, 'is_published': True, 'description': '',
                                   'name': 'Robberies between 1880 to 1900', 'reference': [1005],
                                   'layer_id': 1002, 'f_table_name': 'layer_1002', 'source_description': '',
                                   'created_at': '2017-03-05 00:00:00', 'keyword': [1010]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': 1003, 'is_published': True, 'description': 'streets',
                                   'name': 'Streets in 1920', 'reference': None, 'layer_id': 1004,
                                   'f_table_name': 'layer_1004', 'source_description': '',
                                   'created_at': '2017-06-15 00:00:00', 'keyword': [1040]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': 1003, 'is_published': True, 'description': '',
                                   'name': 'Cinemas between 1900 to 1950', 'reference': [1025],
                                   'layer_id': 1006, 'f_table_name': 'layer_1006', 'source_description': None,
                                   'created_at': '2017-09-04 00:00:00', 'keyword': [1031]},
                    'type': 'Layer'
                }
            ]
        }

        self.tester.api_layer(expected, is_published="TRUE")

        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'properties': {'user_id_published_by': None, 'is_published': False, 'description': '',
                                   'name': 'Streets in 1930', 'reference': [1010],
                                   'layer_id': 1003, 'f_table_name': 'layer_1003', 'source_description': '',
                                   'created_at': '2017-04-10 00:00:00', 'keyword': [1001, 1040]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': None, 'is_published': False, 'description': 'some hospitals',
                                   'name': 'Hospitals between 1800 to 1950', 'reference': None, 'layer_id': 1005,
                                   'f_table_name': 'layer_1005', 'source_description': None,
                                   'created_at': '2017-08-04 00:00:00', 'keyword': [1023]},
                    'type': 'Layer'
                },
            ]
        }

        self.tester.api_layer(expected, is_published="FALSE")

    def test_get_api_layer_return_layer_by_f_table_name(self):
        expected = {
            'features': [
                {
                    'properties': {'user_id_published_by': None, 'is_published': False, 'description': '',
                                   'name': 'Streets in 1930', 'reference': [1010],
                                   'layer_id': 1003, 'f_table_name': 'layer_1003', 'source_description': '',
                                   'created_at': '2017-04-10 00:00:00', 'keyword': [1001, 1040]},
                    'type': 'Layer'
                },
            ],
            'type': 'FeatureCollection'
        }

        self.tester.api_layer(expected, f_table_name="layer_1003")

    def test_get_api_layer_return_layer_by_keyword_id(self):
        expected = {
            'type': 'FeatureCollection',
            'features': [
                {
                    'properties': {'user_id_published_by': 1001, 'is_published': True, 'description': '',
                                   'name': 'Addresses in 1869', 'reference': [1001, 1002],
                                   'layer_id': 1001, 'f_table_name': 'layer_1001', 'source_description': '',
                                   'created_at': '2017-01-01 00:00:00', 'keyword': [1001, 1041]},
                    'type': 'Layer'
                },
                {
                    'properties': {'user_id_published_by': None, 'is_published': False, 'description': '',
                                   'name': 'Streets in 1930', 'reference': [1010],
                                   'layer_id': 1003, 'f_table_name': 'layer_1003', 'source_description': '',
                                   'created_at': '2017-04-10 00:00:00', 'keyword': [1001, 1040]},
                    'type': 'Layer'
                }
            ]
        }

        self.tester.api_layer(expected, keyword_id="1001")

    # layer - create, update and delete

    def test_api_layer_create_update_and_delete(self):
        # DO LOGIN
        self.tester.auth_login("rodrigo@admin.com", "rodrigo")

        ##################################################
        # create a layer
        ##################################################
        resource = {
            'type': 'Layer',
            'properties': {'layer_id': -1, 'f_table_name': 'addresses_1930', 'name': 'Addresses in 1930',
                           'description': '', 'source_description': '',
                           'reference': [1050, 1052], 'keyword': [1001, 1041]},
            'feature_table': {
                'properties': {'name': 'text', 'start_date': 'text', 'end_date': 'text'},
                'geometry': {"type": "MultiPoint"}
            }
        }
        resource = self.tester.api_layer_create(resource)

        ##################################################
        # update the layer
        ##################################################

        ##################################################
        # delete the layer
        ##################################################
        # get the id of layer to SEARCH AND REMOVE it
        resource_id = resource["properties"]["layer_id"]

        # REMOVE THE layer AFTER THE TESTS
        self.tester.api_layer_delete(resource_id)

        # it is not possible to find the layer that just deleted
        self.tester.api_layer_error_404_not_found(layer_id=resource_id)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()


class TestAPILayerErrors(TestCase):

    def setUp(self):
        # create a tester passing the unittest self
        self.tester = UtilTester(self)

    # layer errors - get

    def test_get_api_layer_error_400_bad_request(self):
        self.tester.api_layer_error_400_bad_request(layer_id="abc")
        self.tester.api_layer_error_400_bad_request(layer_id=0)
        self.tester.api_layer_error_400_bad_request(layer_id=-1)
        self.tester.api_layer_error_400_bad_request(layer_id="-1")
        self.tester.api_layer_error_400_bad_request(layer_id="0")

    def test_get_api_layer_error_404_not_found(self):
        self.tester.api_layer_error_404_not_found(layer_id="999")
        self.tester.api_layer_error_404_not_found(layer_id="998")

    # layer errors - create

    def test_post_api_layer_create_error_400_bad_request_attribute_already_exist(self):
        # DO LOGIN
        self.tester.auth_login("rodrigo@admin.com", "rodrigo")

        # create a layer
        resource = {
            'type': 'Layer',
            'properties': {'layer_id': -1, 'f_table_name': 'addresses_1930', 'name': 'Addresses in 1930',
                           'description': '', 'source_description': '',
                           'reference': [], 'keyword': [1041]},
            'feature_table': {
                'properties': {'name': 'text', 'start_date': 'text', 'end_date': 'text'},
                'geometry': {"type": "MultiPoint"}
            }
        }
        resource = self.tester.api_layer_create(resource)

        # get the id of layer to REMOVE it
        resource_id = resource["properties"]["layer_id"]

        ##################################################
        # try to insert the resource again, raising the 400
        ##################################################
        self.tester.api_layer_create_error_400_bad_request(resource)

        # remove the resource after the tests
        self.tester.api_layer_delete(resource_id)

        # it is not possible to find the layer that just deleted
        self.tester.api_layer_error_404_not_found(layer_id=resource_id)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_post_api_layer_create_error_400_bad_request_attribute_in_JSON_is_missing(self):
        # DO LOGIN
        self.tester.auth_login("rodrigo@admin.com", "rodrigo")

        # try to create a layer (without reference)
        resource = {
            'type': 'Layer',
            'properties': {'name': 'Addresses in 1869', 'table_name': 'addresses_1869', 'source': '',
                           'description': '', 'fk_keyword_id': 1041},
            'feature_table': {
                'properties': {'name': 'text', 'start_date': 'text', 'end_date': 'text'},
                'geometry': {"type": "MultiPoint"}
            }
        }
        self.tester.api_layer_create_error_400_bad_request(resource)

        # try to create a layer (without f_table_name)
        resource = {
            'type': 'Layer',
            'properties': {'layer_id': -1, 'name': 'Addresses in 1930', 'description': '', 'source_description': '',
                           'reference': [], 'keyword': [1041]},
            'feature_table': {
                'properties': {'name': 'text', 'start_date': 'text', 'end_date': 'text'},
                'geometry': {"type": "MultiPoint"}
            }
        }
        self.tester.api_layer_create_error_400_bad_request(resource)

        # try to create a layer (without description)
        resource = {
            'type': 'Layer',
            'properties': {'layer_id': -1, 'f_table_name': 'addresses_1930', 'name': 'Addresses in 1930',
                           'source_description': '',
                           'reference': [], 'keyword': [1041]},
            'feature_table': {
                'properties': {'name': 'text', 'start_date': 'text', 'end_date': 'text'},
                'geometry': {"type": "MultiPoint"}
            }
        }
        self.tester.api_layer_create_error_400_bad_request(resource)

        # try to create a layer (without feature_table)
        resource = {
            'type': 'Layer',
            'properties': {'layer_id': -1, 'f_table_name': 'addresses_1930', 'name': 'Addresses in 1930',
                           'description': '', 'source_description': '',
                           'reference': [], 'keyword': [1041]}
        }
        self.tester.api_layer_create_error_400_bad_request(resource)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_post_api_layer_create_error_401_unauthorized(self):
        feature = {
            'properties': {'name': 'Addresses in 1869', 'table_name': 'new_layer', 'source': '',
                           'description': '', 'fk_keyword_id': 1041},
            'type': 'Layer'
        }
        self.tester.api_layer_create_error_401_unauthorized(feature)

    # layer errors - delete

    def test_delete_api_layer_error_400_bad_request(self):
        # create a tester passing the unittest self
        self.tester = UtilTester(self)

        # DO LOGIN
        self.tester.auth_login("rodrigo@admin.com", "rodrigo")

        self.tester.api_layer_delete_error_400_bad_request("abc")
        self.tester.api_layer_delete_error_400_bad_request(0)
        self.tester.api_layer_delete_error_400_bad_request(-1)
        self.tester.api_layer_delete_error_400_bad_request("-1")
        self.tester.api_layer_delete_error_400_bad_request("0")

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_delete_api_layer_error_401_unauthorized_user_without_login(self):
        self.tester.api_layer_delete_error_401_unauthorized("abc")
        self.tester.api_layer_delete_error_401_unauthorized(0)
        self.tester.api_layer_delete_error_401_unauthorized(-1)
        self.tester.api_layer_delete_error_401_unauthorized("-1")
        self.tester.api_layer_delete_error_401_unauthorized("0")
        self.tester.api_layer_delete_error_401_unauthorized("1001")
    
    def test_delete_api_layer_error_403_forbidden_user_forbidden_to_delete(self):
        ########################################
        # create a layer with user admin
        ########################################

        self.tester.auth_login("admin@admin.com", "admin")

        # user_session = self.tester.get_session_user()
        # user_id = user_session["user"]["properties"]["user_id"]

        # create a layer
        resource = {
            'type': 'Layer',
            'properties': {'layer_id': -1, 'f_table_name': 'new_layer', 'name': 'Addresses in 1930',
                           'description': '', 'source_description': '',
                           'reference': [], 'keyword': [1041]},
            'feature_table': {
                'properties': {'name': 'text', 'start_date': 'text', 'end_date': 'text'},
                'geometry': {"type": "MultiPoint"}
            }
        }
        resource = self.tester.api_layer_create(resource)

        # logout with admin
        self.tester.auth_logout()

        ########################################
        # try to delete a layer with user rodrigo
        ########################################

        self.tester.auth_login("rodrigo@admin.com", "rodrigo")

        # get the id of layer to REMOVE it
        resource_id = resource["properties"]["layer_id"]

        # TRY TO REMOVE THE LAYER
        self.tester.api_layer_delete_error_403_forbidden(resource_id)

        # logout with user rodrigo
        self.tester.auth_logout()

        ########################################
        # really delete the layer with user admin
        ########################################
        self.tester.auth_login("admin@admin.com", "admin")

        # delete the layer
        self.tester.api_layer_delete(resource_id)

        # it is not possible to find the layer that just deleted
        self.tester.api_layer_error_404_not_found(layer_id=resource_id)

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()

    def test_delete_api_layer_error_404_not_found(self):
        # create a tester passing the unittest self
        self.tester = UtilTester(self)

        # DO LOGIN
        self.tester.auth_login("rodrigo@admin.com", "rodrigo")

        self.tester.api_layer_delete_error_404_not_found("5000")
        self.tester.api_layer_delete_error_404_not_found("5001")

        # DO LOGOUT AFTER THE TESTS
        self.tester.auth_logout()


# It is not necessary to pyt the main() of unittest here,
# because this file will be call by run_tests.py
