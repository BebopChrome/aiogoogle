OAUTH2_V2_DISCVOCERY_DOC = {'auth': {'oauth2': {'scopes': {'https://www.googleapis.com/auth/plus.login': {'description': 'Know the list of people in your circles, your age range, and '
                                                                                              'language'},
                                'https://www.googleapis.com/auth/plus.me': {'description': 'Know who you are on Google'},
                                'https://www.googleapis.com/auth/userinfo.email': {'description': 'View your email address'},
                                'https://www.googleapis.com/auth/userinfo.profile': {'description': 'View your basic profile info'}}}},
 'basePath': '/',
 'baseUrl': 'https://www.googleapis.com/',
 'batchPath': 'batch/oauth2/v2',
 'description': 'Obtains end-user authorization grants for use with other Google APIs.',
 'discoveryVersion': 'v1',
 'documentationLink': 'https://developers.google.com/accounts/docs/OAuth2',
 'etag': '"J3WqvAcMk4eQjJXvfSI4Yr8VouA/fwW2utFkCnVanfAd4kn3jkF7-Z8"',
 'icons': {'x16': 'https://www.gstatic.com/images/branding/product/1x/googleg_16dp.png',
           'x32': 'https://www.gstatic.com/images/branding/product/1x/googleg_32dp.png'},
 'id': 'oauth2:v2',
 'kind': 'discovery#restDescription',
 'methods': {'getCertForOpenIdConnect': {'httpMethod': 'GET', 'id': 'oauth2.getCertForOpenIdConnect', 'path': 'oauth2/v2/certs', 'response': {'$ref': 'Jwk'}},
             'tokeninfo': {'httpMethod': 'POST',
                           'id': 'oauth2.tokeninfo',
                           'parameters': {'access_token': {'location': 'query', 'type': 'string'},
                                          'id_token': {'location': 'query', 'type': 'string'},
                                          'token_handle': {'location': 'query', 'type': 'string'}},
                           'path': 'oauth2/v2/tokeninfo',
                           'response': {'$ref': 'Tokeninfo'}}},
 'name': 'oauth2',
 'ownerDomain': 'google.com',
 'ownerName': 'Google',
 'parameters': {'alt': {'default': 'json',
                        'description': 'Data format for the response.',
                        'enum': ['json'],
                        'enumDescriptions': ['Responses with Content-Type of application/json'],
                        'location': 'query',
                        'type': 'string'},
                'fields': {'description': 'Selector specifying which fields to include in a partial response.', 'location': 'query', 'type': 'string'},
                'key': {'description': 'API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless '
                                       'you provide an OAuth 2.0 token.',
                        'location': 'query',
                        'type': 'string'},
                'oauth_token': {'description': 'OAuth 2.0 token for the current user.', 'location': 'query', 'type': 'string'},
                'prettyPrint': {'default': 'true',
                                'description': 'Returns response with indentations and line breaks.',
                                'location': 'query',
                                'type': 'boolean'},
                'quotaUser': {'description': 'An opaque string that represents a user for quota purposes. Must not exceed 40 characters.',
                              'location': 'query',
                              'type': 'string'},
                'userIp': {'description': 'Deprecated. Please use quotaUser instead.', 'location': 'query', 'type': 'string'}},
 'protocol': 'rest',
 'resources': {'userinfo': {'methods': {'get': {'httpMethod': 'GET',
                                                'id': 'oauth2.userinfo.get',
                                                'path': 'oauth2/v2/userinfo',
                                                'response': {'$ref': 'Userinfoplus'},
                                                'scopes': ['https://www.googleapis.com/auth/plus.login',
                                                           'https://www.googleapis.com/auth/plus.me',
                                                           'https://www.googleapis.com/auth/userinfo.email',
                                                           'https://www.googleapis.com/auth/userinfo.profile']}},
                            'resources': {'v2': {'resources': {'me': {'methods': {'get': {'httpMethod': 'GET',
                                                                                          'id': 'oauth2.userinfo.v2.me.get',
                                                                                          'path': 'userinfo/v2/me',
                                                                                          'response': {'$ref': 'Userinfoplus'},
                                                                                          'scopes': ['https://www.googleapis.com/auth/plus.login',
                                                                                                     'https://www.googleapis.com/auth/plus.me',
                                                                                                     'https://www.googleapis.com/auth/userinfo.email',
                                                                                                     'https://www.googleapis.com/auth/userinfo.profile']}}}}}}}},
 'revision': '20181105',
 'rootUrl': 'https://www.googleapis.com/',
 'schemas': {'Jwk': {'id': 'Jwk',
                     'properties': {'keys': {'items': {'properties': {'alg': {'default': 'RS256', 'type': 'string'},
                                                                      'e': {'type': 'string'},
                                                                      'kid': {'type': 'string'},
                                                                      'kty': {'default': 'RSA', 'type': 'string'},
                                                                      'n': {'type': 'string'},
                                                                      'use': {'default': 'sig', 'type': 'string'}},
                                                       'type': 'object'},
                                             'type': 'array'}},
                     'type': 'object'},
             'Tokeninfo': {'id': 'Tokeninfo',
                           'properties': {'access_type': {'description': 'The access type granted with this token. It can be offline or online.',
                                                          'type': 'string'},
                                          'audience': {'description': 'Who is the intended audience for this token. In general the same as issued_to.',
                                                       'type': 'string'},
                                          'email': {'description': 'The email address of the user. Present only if the email scope is present in the request.',
                                                    'type': 'string'},
                                          'expires_in': {'description': 'The expiry time of the token, as number of seconds left until expiry.',
                                                         'format': 'int32',
                                                         'type': 'integer'},
                                          'issued_to': {'description': 'To whom was the token issued to. In general the same as audience.', 'type': 'string'},
                                          'scope': {'description': 'The space separated list of scopes granted to this token.', 'type': 'string'},
                                          'token_handle': {'description': 'The token handle associated with this token.', 'type': 'string'},
                                          'user_id': {'description': 'The obfuscated user id.', 'type': 'string'},
                                          'verified_email': {'description': 'Boolean flag which is true if the email address is verified. Present only if the '
                                                                            'email scope is present in the request.',
                                                             'type': 'boolean'}},
                           'type': 'object'},
             'Userinfoplus': {'id': 'Userinfoplus',
                              'properties': {'email': {'description': "The user's email address.", 'type': 'string'},
                                             'family_name': {'description': "The user's last name.", 'type': 'string'},
                                             'gender': {'description': "The user's gender.", 'type': 'string'},
                                             'given_name': {'description': "The user's first name.", 'type': 'string'},
                                             'hd': {'description': 'The hosted domain e.g. example.com if the user is Google apps user.', 'type': 'string'},
                                             'id': {'description': 'The obfuscated ID of the user.', 'type': 'string'},
                                             'link': {'description': 'URL of the profile page.', 'type': 'string'},
                                             'locale': {'description': "The user's preferred locale.", 'type': 'string'},
                                             'name': {'description': "The user's full name.", 'type': 'string'},
                                             'picture': {'description': "URL of the user's picture image.", 'type': 'string'},
                                             'verified_email': {'default': 'true',
                                                                'description': 'Boolean flag which is true if the email address is verified. Always verified '
                                                                               "because we only return the user's primary email address.",
                                                                'type': 'boolean'}},
                              'type': 'object'}},
 'servicePath': '',
 'title': 'Google OAuth2 API',
 'version': 'v2'}

GOOGLE_PLUS_V1_DISCVOCERY_DOC = {'auth': {'oauth2': {'scopes': {'https://www.googleapis.com/auth/plus.login': {'description': 'Know the list of people in your circles, your age range, and '
                                                                                              'language'},
                                'https://www.googleapis.com/auth/plus.me': {'description': 'Know who you are on Google'},
                                'https://www.googleapis.com/auth/userinfo.email': {'description': 'View your email address'},
                                'https://www.googleapis.com/auth/userinfo.profile': {'description': 'View your basic profile info'}}}},
 'basePath': '/plus/v1/',
 'baseUrl': 'https://www.googleapis.com/plus/v1/',
 'batchPath': 'batch/plus/v1',
 'description': 'Builds on top of the Google+ platform.',
 'discoveryVersion': 'v1',
 'documentationLink': 'https://developers.google.com/+/api/',
 'etag': '"J3WqvAcMk4eQjJXvfSI4Yr8VouA/md-Mx_OqDEnSqiMNxd9p4dauplA"',
 'icons': {'x16': 'http://www.google.com/images/icons/product/gplus-16.png', 'x32': 'http://www.google.com/images/icons/product/gplus-32.png'},
 'id': 'plus:v1',
 'kind': 'discovery#restDescription',
 'name': 'plus',
 'ownerDomain': 'google.com',
 'ownerName': 'Google',
 'parameters': {'alt': {'default': 'json',
                        'description': 'Data format for the response.',
                        'enum': ['json'],
                        'enumDescriptions': ['Responses with Content-Type of application/json'],
                        'location': 'query',
                        'type': 'string'},
                'fields': {'description': 'Selector specifying which fields to include in a partial response.', 'location': 'query', 'type': 'string'},
                'key': {'description': 'API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless '
                                       'you provide an OAuth 2.0 token.',
                        'location': 'query',
                        'type': 'string'},
                'oauth_token': {'description': 'OAuth 2.0 token for the current user.', 'location': 'query', 'type': 'string'},
                'prettyPrint': {'default': 'true',
                                'description': 'Returns response with indentations and line breaks.',
                                'location': 'query',
                                'type': 'boolean'},
                'quotaUser': {'description': 'An opaque string that represents a user for quota purposes. Must not exceed 40 characters.',
                              'location': 'query',
                              'type': 'string'},
                'userIp': {'description': 'Deprecated. Please use quotaUser instead.', 'location': 'query', 'type': 'string'}},
 'protocol': 'rest',
 'resources': {'activities': {'methods': {'get': {'description': 'Get an activity.',
                                                  'httpMethod': 'GET',
                                                  'id': 'plus.activities.get',
                                                  'parameterOrder': ['activityId'],
                                                  'parameters': {'activityId': {'description': 'The ID of the activity to get.',
                                                                                'location': 'path',
                                                                                'required': True,
                                                                                'type': 'string'}},
                                                  'path': 'activities/{activityId}',
                                                  'response': {'$ref': 'Activity'},
                                                  'scopes': ['https://www.googleapis.com/auth/plus.login', 'https://www.googleapis.com/auth/plus.me']},
                                          'list': {'description': 'List all of the activities in the specified collection for a particular user.',
                                                   'httpMethod': 'GET',
                                                   'id': 'plus.activities.list',
                                                   'parameterOrder': ['userId', 'collection'],
                                                   'parameters': {'collection': {'description': 'The collection of activities to list.',
                                                                                 'enum': ['public'],
                                                                                 'enumDescriptions': ['All public activities created by the specified user.'],
                                                                                 'location': 'path',
                                                                                 'required': True,
                                                                                 'type': 'string'},
                                                                  'maxResults': {'default': '20',
                                                                                 'description': 'The maximum number of activities to include in the response, '
                                                                                                'which is used for paging. For any response, the actual number '
                                                                                                'returned might be less than the specified maxResults.',
                                                                                 'format': 'uint32',
                                                                                 'location': 'query',
                                                                                 'maximum': '100',
                                                                                 'minimum': '1',
                                                                                 'type': 'integer'},
                                                                  'pageToken': {'description': 'The continuation token, which is used to page through large '
                                                                                               'result sets. To get the next page of results, set this '
                                                                                               'parameter to the value of "nextPageToken" from the previous '
                                                                                               'response.',
                                                                                'location': 'query',
                                                                                'type': 'string'},
                                                                  'userId': {'description': 'The ID of the user to get activities for. The special value "me" '
                                                                                            'can be used to indicate the authenticated user.',
                                                                             'location': 'path',
                                                                             'required': True,
                                                                             'type': 'string'}},
                                                   'path': 'people/{userId}/activities/{collection}',
                                                   'response': {'$ref': 'ActivityFeed'},
                                                   'scopes': ['https://www.googleapis.com/auth/plus.login', 'https://www.googleapis.com/auth/plus.me']},
                                          'search': {'description': 'Search public activities.',
                                                     'httpMethod': 'GET',
                                                     'id': 'plus.activities.search',
                                                     'parameterOrder': ['query'],
                                                     'parameters': {'language': {'default': 'en-US',
                                                                                 'description': 'Specify the preferred language to search with. See search '
                                                                                                'language codes for available values.',
                                                                                 'location': 'query',
                                                                                 'type': 'string'},
                                                                    'maxResults': {'default': '10',
                                                                                   'description': 'The maximum number of activities to include in the '
                                                                                                  'response, which is used for paging. For any response, the '
                                                                                                  'actual number returned might be less than the specified '
                                                                                                  'maxResults.',
                                                                                   'format': 'uint32',
                                                                                   'location': 'query',
                                                                                   'maximum': '20',
                                                                                   'minimum': '1',
                                                                                   'type': 'integer'},
                                                                    'orderBy': {'default': 'recent',
                                                                                'description': 'Specifies how to order search results.',
                                                                                'enum': ['best', 'recent'],
                                                                                'enumDescriptions': ['Sort activities by relevance to the user, most relevant '
                                                                                                     'first.',
                                                                                                     'Sort activities by published date, most recent first.'],
                                                                                'location': 'query',
                                                                                'type': 'string'},
                                                                    'pageToken': {'description': 'The continuation token, which is used to page through large '
                                                                                                 'result sets. To get the next page of results, set this '
                                                                                                 'parameter to the value of "nextPageToken" from the previous '
                                                                                                 'response. This token can be of any length.',
                                                                                  'location': 'query',
                                                                                  'type': 'string'},
                                                                    'query': {'description': 'Full-text search query string.',
                                                                              'location': 'query',
                                                                              'required': True,
                                                                              'type': 'string'}},
                                                     'path': 'activities',
                                                     'response': {'$ref': 'ActivityFeed'},
                                                     'scopes': ['https://www.googleapis.com/auth/plus.login', 'https://www.googleapis.com/auth/plus.me']}}},
               'comments': {'methods': {'get': {'description': 'Get a comment.',
                                                'httpMethod': 'GET',
                                                'id': 'plus.comments.get',
                                                'parameterOrder': ['commentId'],
                                                'parameters': {'commentId': {'description': 'The ID of the comment to get.',
                                                                             'location': 'path',
                                                                             'required': True,
                                                                             'type': 'string'}},
                                                'path': 'comments/{commentId}',
                                                'response': {'$ref': 'Comment'},
                                                'scopes': ['https://www.googleapis.com/auth/plus.login', 'https://www.googleapis.com/auth/plus.me']},
                                        'list': {'description': 'List all of the comments for an activity.',
                                                 'httpMethod': 'GET',
                                                 'id': 'plus.comments.list',
                                                 'parameterOrder': ['activityId'],
                                                 'parameters': {'activityId': {'description': 'The ID of the activity to get comments for.',
                                                                               'location': 'path',
                                                                               'required': True,
                                                                               'type': 'string'},
                                                                'maxResults': {'default': '20',
                                                                               'description': 'The maximum number of comments to include in the response, '
                                                                                              'which is used for paging. For any response, the actual number '
                                                                                              'returned might be less than the specified maxResults.',
                                                                               'format': 'uint32',
                                                                               'location': 'query',
                                                                               'maximum': '500',
                                                                               'minimum': '0',
                                                                               'type': 'integer'},
                                                                'pageToken': {'description': 'The continuation token, which is used to page through large '
                                                                                             'result sets. To get the next page of results, set this parameter '
                                                                                             'to the value of "nextPageToken" from the previous response.',
                                                                              'location': 'query',
                                                                              'type': 'string'},
                                                                'sortOrder': {'default': 'ascending',
                                                                              'description': 'The order in which to sort the list of comments.',
                                                                              'enum': ['ascending', 'descending'],
                                                                              'enumDescriptions': ['Sort oldest comments first.',
                                                                                                   'Sort newest comments first.'],
                                                                              'location': 'query',
                                                                              'type': 'string'}},
                                                 'path': 'activities/{activityId}/comments',
                                                 'response': {'$ref': 'CommentFeed'},
                                                 'scopes': ['https://www.googleapis.com/auth/plus.login', 'https://www.googleapis.com/auth/plus.me']}}},
               'people': {'methods': {'get': {'description': "Get a person's profile. If your app uses scope https://www.googleapis.com/auth/plus.login, this "
                                                             'method is guaranteed to return ageRange and language.',
                                              'httpMethod': 'GET',
                                              'id': 'plus.people.get',
                                              'parameterOrder': ['userId'],
                                              'parameters': {'userId': {'description': 'The ID of the person to get the profile for. The special value "me" '
                                                                                       'can be used to indicate the authenticated user.',
                                                                        'location': 'path',
                                                                        'required': True,
                                                                        'type': 'string'}},
                                              'path': 'people/{userId}',
                                              'response': {'$ref': 'Person'},
                                              'scopes': ['https://www.googleapis.com/auth/plus.login',
                                                         'https://www.googleapis.com/auth/plus.me',
                                                         'https://www.googleapis.com/auth/userinfo.email',
                                                         'https://www.googleapis.com/auth/userinfo.profile']},
                                      'list': {'description': 'List all of the people in the specified collection.',
                                               'httpMethod': 'GET',
                                               'id': 'plus.people.list',
                                               'parameterOrder': ['userId', 'collection'],
                                               'parameters': {'collection': {'description': 'The collection of people to list.',
                                                                             'enum': ['connected', 'visible'],
                                                                             'enumDescriptions': ["The list of visible people in the authenticated user's "
                                                                                                  'circles who also use the requesting app. This list is '
                                                                                                  'limited to users who made their app activities visible to '
                                                                                                  'the authenticated user.',
                                                                                                  'The list of people who this user has added to one or more '
                                                                                                  'circles, limited to the circles visible to the requesting '
                                                                                                  'application.'],
                                                                             'location': 'path',
                                                                             'required': True,
                                                                             'type': 'string'},
                                                              'maxResults': {'default': '100',
                                                                             'description': 'The maximum number of people to include in the response, which is '
                                                                                            'used for paging. For any response, the actual number returned '
                                                                                            'might be less than the specified maxResults.',
                                                                             'format': 'uint32',
                                                                             'location': 'query',
                                                                             'maximum': '100',
                                                                             'minimum': '1',
                                                                             'type': 'integer'},
                                                              'orderBy': {'description': 'The order to return people in.',
                                                                          'enum': ['alphabetical', 'best'],
                                                                          'enumDescriptions': ['Order the people by their display name.',
                                                                                               'Order people based on the relevence to the viewer.'],
                                                                          'location': 'query',
                                                                          'type': 'string'},
                                                              'pageToken': {'description': 'The continuation token, which is used to page through large result '
                                                                                           'sets. To get the next page of results, set this parameter to the '
                                                                                           'value of "nextPageToken" from the previous response.',
                                                                            'location': 'query',
                                                                            'type': 'string'},
                                                              'userId': {'description': 'Get the collection of people for the person identified. Use "me" to '
                                                                                        'indicate the authenticated user.',
                                                                         'location': 'path',
                                                                         'required': True,
                                                                         'type': 'string'}},
                                               'path': 'people/{userId}/people/{collection}',
                                               'response': {'$ref': 'PeopleFeed'},
                                               'scopes': ['https://www.googleapis.com/auth/plus.login', 'https://www.googleapis.com/auth/plus.me']},
                                      'listByActivity': {'description': 'List all of the people in the specified collection for a particular activity.',
                                                         'httpMethod': 'GET',
                                                         'id': 'plus.people.listByActivity',
                                                         'parameterOrder': ['activityId', 'collection'],
                                                         'parameters': {'activityId': {'description': 'The ID of the activity to get the list of people for.',
                                                                                       'location': 'path',
                                                                                       'required': True,
                                                                                       'type': 'string'},
                                                                        'collection': {'description': 'The collection of people to list.',
                                                                                       'enum': ['plusoners', 'resharers'],
                                                                                       'enumDescriptions': ["List all people who have +1'd this activity.",
                                                                                                            'List all people who have reshared this activity.'],
                                                                                       'location': 'path',
                                                                                       'required': True,
                                                                                       'type': 'string'},
                                                                        'maxResults': {'default': '20',
                                                                                       'description': 'The maximum number of people to include in the '
                                                                                                      'response, which is used for paging. For any response, '
                                                                                                      'the actual number returned might be less than the '
                                                                                                      'specified maxResults.',
                                                                                       'format': 'uint32',
                                                                                       'location': 'query',
                                                                                       'maximum': '100',
                                                                                       'minimum': '1',
                                                                                       'type': 'integer'},
                                                                        'pageToken': {'description': 'The continuation token, which is used to page through '
                                                                                                     'large result sets. To get the next page of results, set '
                                                                                                     'this parameter to the value of "nextPageToken" from the '
                                                                                                     'previous response.',
                                                                                      'location': 'query',
                                                                                      'type': 'string'}},
                                                         'path': 'activities/{activityId}/people/{collection}',
                                                         'response': {'$ref': 'PeopleFeed'},
                                                         'scopes': ['https://www.googleapis.com/auth/plus.login', 'https://www.googleapis.com/auth/plus.me']},
                                      'search': {'description': 'Search all public profiles.',
                                                 'httpMethod': 'GET',
                                                 'id': 'plus.people.search',
                                                 'parameterOrder': ['query'],
                                                 'parameters': {'language': {'default': 'en-US',
                                                                             'description': 'Specify the preferred language to search with. See search '
                                                                                            'language codes for available values.',
                                                                             'location': 'query',
                                                                             'type': 'string'},
                                                                'maxResults': {'default': '25',
                                                                               'description': 'The maximum number of people to include in the response, which '
                                                                                              'is used for paging. For any response, the actual number '
                                                                                              'returned might be less than the specified maxResults.',
                                                                               'format': 'uint32',
                                                                               'location': 'query',
                                                                               'maximum': '50',
                                                                               'minimum': '1',
                                                                               'type': 'integer'},
                                                                'pageToken': {'description': 'The continuation token, which is used to page through large '
                                                                                             'result sets. To get the next page of results, set this parameter '
                                                                                             'to the value of "nextPageToken" from the previous response. This '
                                                                                             'token can be of any length.',
                                                                              'location': 'query',
                                                                              'type': 'string'},
                                                                'query': {'description': 'Specify a query string for full text search of public text in all '
                                                                                         'profiles.',
                                                                          'location': 'query',
                                                                          'required': True,
                                                                          'type': 'string'}},
                                                 'path': 'people',
                                                 'response': {'$ref': 'PeopleFeed'},
                                                 'scopes': ['https://www.googleapis.com/auth/plus.login', 'https://www.googleapis.com/auth/plus.me']}}}},
 'revision': '20181111',
 'rootUrl': 'https://www.googleapis.com/',
 'schemas': {'Acl': {'id': 'Acl',
                     'properties': {'description': {'description': 'Description of the access granted, suitable for display.', 'type': 'string'},
                                    'items': {'description': 'The list of access entries.', 'items': {'$ref': 'PlusAclentryResource'}, 'type': 'array'},
                                    'kind': {'default': 'plus#acl',
                                             'description': 'Identifies this resource as a collection of access controls. Value: "plus#acl".',
                                             'type': 'string'}},
                     'type': 'object'},
             'Activity': {'id': 'Activity',
                          'properties': {'access': {'$ref': 'Acl', 'description': 'Identifies who has access to see this activity.'},
                                         'actor': {'description': 'The person who performed this activity.',
                                                   'properties': {'clientSpecificActorInfo': {'description': 'Actor info specific to particular clients.',
                                                                                              'properties': {'youtubeActorInfo': {'description': 'Actor info '
                                                                                                                                                 'specific to '
                                                                                                                                                 'YouTube '
                                                                                                                                                 'clients.',
                                                                                                                                  'properties': {'channelId': {'description': 'ID '
                                                                                                                                                                              'of '
                                                                                                                                                                              'the '
                                                                                                                                                                              'YouTube '
                                                                                                                                                                              'channel '
                                                                                                                                                                              'owned '
                                                                                                                                                                              'by '
                                                                                                                                                                              'the '
                                                                                                                                                                              'Actor.',
                                                                                                                                                               'type': 'string'}},
                                                                                                                                  'type': 'object'}},
                                                                                              'type': 'object'},
                                                                  'displayName': {'description': 'The name of the actor, suitable for display.',
                                                                                  'type': 'string'},
                                                                  'id': {'description': "The ID of the actor's Person resource.", 'type': 'string'},
                                                                  'image': {'description': 'The image representation of the actor.',
                                                                            'properties': {'url': {'description': "The URL of the actor's profile photo. To "
                                                                                                                  'resize the image and crop it to a square, '
                                                                                                                  'append the query string ?sz=x, where x is '
                                                                                                                  'the dimension in pixels of each side.',
                                                                                                   'type': 'string'}},
                                                                            'type': 'object'},
                                                                  'name': {'description': 'An object representation of the individual components of name.',
                                                                           'properties': {'familyName': {'description': 'The family name ("last name") of the '
                                                                                                                        'actor.',
                                                                                                         'type': 'string'},
                                                                                          'givenName': {'description': 'The given name ("first name") of the '
                                                                                                                       'actor.',
                                                                                                        'type': 'string'}},
                                                                           'type': 'object'},
                                                                  'url': {'description': "The link to the actor's Google profile.", 'type': 'string'},
                                                                  'verification': {'description': 'Verification status of actor.',
                                                                                   'properties': {'adHocVerified': {'description': 'Verification for one-time '
                                                                                                                                   'or manual processes.',
                                                                                                                    'type': 'string'}},
                                                                                   'type': 'object'}},
                                                   'type': 'object'},
                                         'address': {'description': 'Street address where this activity occurred.', 'type': 'string'},
                                         'annotation': {'description': 'Additional content added by the person who shared this activity, applicable only when '
                                                                       'resharing an activity.',
                                                        'type': 'string'},
                                         'crosspostSource': {'description': 'If this activity is a crosspost from another system, this property specifies the '
                                                                            'ID of the original activity.',
                                                             'type': 'string'},
                                         'etag': {'description': 'ETag of this response for caching purposes.', 'type': 'string'},
                                         'geocode': {'description': 'Latitude and longitude where this activity occurred. Format is latitude followed by '
                                                                    'longitude, space separated.',
                                                     'type': 'string'},
                                         'id': {'description': 'The ID of this activity.', 'type': 'string'},
                                         'kind': {'default': 'plus#activity',
                                                  'description': 'Identifies this resource as an activity. Value: "plus#activity".',
                                                  'type': 'string'},
                                         'location': {'$ref': 'Place', 'description': 'The location where this activity occurred.'},
                                         'object': {'description': 'The object of this activity.',
                                                    'properties': {'actor': {'description': "If this activity's object is itself another activity, such as "
                                                                                            'when a person reshares an activity, this property specifies the '
                                                                                            "original activity's actor.",
                                                                             'properties': {'clientSpecificActorInfo': {'description': 'Actor info specific to '
                                                                                                                                       'particular clients.',
                                                                                                                        'properties': {'youtubeActorInfo': {'description': 'Actor '
                                                                                                                                                                           'info '
                                                                                                                                                                           'specific '
                                                                                                                                                                           'to '
                                                                                                                                                                           'YouTube '
                                                                                                                                                                           'clients.',
                                                                                                                                                            'properties': {'channelId': {'description': 'ID '
                                                                                                                                                                                                        'of '
                                                                                                                                                                                                        'the '
                                                                                                                                                                                                        'YouTube '
                                                                                                                                                                                                        'channel '
                                                                                                                                                                                                        'owned '
                                                                                                                                                                                                        'by '
                                                                                                                                                                                                        'the '
                                                                                                                                                                                                        'Actor.',
                                                                                                                                                                                         'type': 'string'}},
                                                                                                                                                            'type': 'object'}},
                                                                                                                        'type': 'object'},
                                                                                            'displayName': {'description': "The original actor's name, which "
                                                                                                                           'is suitable for display.',
                                                                                                            'type': 'string'},
                                                                                            'id': {'description': 'ID of the original actor.',
                                                                                                   'type': 'string'},
                                                                                            'image': {'description': 'The image representation of the original '
                                                                                                                     'actor.',
                                                                                                      'properties': {'url': {'description': 'A URL that points '
                                                                                                                                            'to a thumbnail '
                                                                                                                                            'photo of the '
                                                                                                                                            'original actor.',
                                                                                                                             'type': 'string'}},
                                                                                                      'type': 'object'},
                                                                                            'url': {'description': "A link to the original actor's Google "
                                                                                                                   'profile.',
                                                                                                    'type': 'string'},
                                                                                            'verification': {'description': 'Verification status of actor.',
                                                                                                             'properties': {'adHocVerified': {'description': 'Verification '
                                                                                                                                                             'for '
                                                                                                                                                             'one-time '
                                                                                                                                                             'or '
                                                                                                                                                             'manual '
                                                                                                                                                             'processes.',
                                                                                                                                              'type': 'string'}},
                                                                                                             'type': 'object'}},
                                                                             'type': 'object'},
                                                                   'attachments': {'description': 'The media objects attached to this activity.',
                                                                                   'items': {'properties': {'content': {'description': 'If the attachment is '
                                                                                                                                       'an article, this '
                                                                                                                                       'property contains a '
                                                                                                                                       'snippet of text from '
                                                                                                                                       'the article. It can '
                                                                                                                                       'also include '
                                                                                                                                       'descriptions for other '
                                                                                                                                       'types.',
                                                                                                                        'type': 'string'},
                                                                                                            'displayName': {'description': 'The title of the '
                                                                                                                                           'attachment, such '
                                                                                                                                           'as a photo caption '
                                                                                                                                           'or an article '
                                                                                                                                           'title.',
                                                                                                                            'type': 'string'},
                                                                                                            'embed': {'description': 'If the attachment is a '
                                                                                                                                     'video, the embeddable '
                                                                                                                                     'link.',
                                                                                                                      'properties': {'type': {'description': 'Media '
                                                                                                                                                             'type '
                                                                                                                                                             'of '
                                                                                                                                                             'the '
                                                                                                                                                             'link.',
                                                                                                                                              'type': 'string'},
                                                                                                                                     'url': {'description': 'URL '
                                                                                                                                                            'of '
                                                                                                                                                            'the '
                                                                                                                                                            'link.',
                                                                                                                                             'type': 'string'}},
                                                                                                                      'type': 'object'},
                                                                                                            'fullImage': {'description': 'The full image URL '
                                                                                                                                         'for photo '
                                                                                                                                         'attachments.',
                                                                                                                          'properties': {'height': {'description': 'The '
                                                                                                                                                                   'height, '
                                                                                                                                                                   'in '
                                                                                                                                                                   'pixels, '
                                                                                                                                                                   'of '
                                                                                                                                                                   'the '
                                                                                                                                                                   'linked '
                                                                                                                                                                   'resource.',
                                                                                                                                                    'format': 'uint32',
                                                                                                                                                    'type': 'integer'},
                                                                                                                                         'type': {'description': 'Media '
                                                                                                                                                                 'type '
                                                                                                                                                                 'of '
                                                                                                                                                                 'the '
                                                                                                                                                                 'link.',
                                                                                                                                                  'type': 'string'},
                                                                                                                                         'url': {'description': 'URL '
                                                                                                                                                                'of '
                                                                                                                                                                'the '
                                                                                                                                                                'image.',
                                                                                                                                                 'type': 'string'},
                                                                                                                                         'width': {'description': 'The '
                                                                                                                                                                  'width, '
                                                                                                                                                                  'in '
                                                                                                                                                                  'pixels, '
                                                                                                                                                                  'of '
                                                                                                                                                                  'the '
                                                                                                                                                                  'linked '
                                                                                                                                                                  'resource.',
                                                                                                                                                   'format': 'uint32',
                                                                                                                                                   'type': 'integer'}},
                                                                                                                          'type': 'object'},
                                                                                                            'id': {'description': 'The ID of the attachment.',
                                                                                                                   'type': 'string'},
                                                                                                            'image': {'description': 'The preview image for '
                                                                                                                                     'photos or videos.',
                                                                                                                      'properties': {'height': {'description': 'The '
                                                                                                                                                               'height, '
                                                                                                                                                               'in '
                                                                                                                                                               'pixels, '
                                                                                                                                                               'of '
                                                                                                                                                               'the '
                                                                                                                                                               'linked '
                                                                                                                                                               'resource.',
                                                                                                                                                'format': 'uint32',
                                                                                                                                                'type': 'integer'},
                                                                                                                                     'type': {'description': 'Media '
                                                                                                                                                             'type '
                                                                                                                                                             'of '
                                                                                                                                                             'the '
                                                                                                                                                             'link.',
                                                                                                                                              'type': 'string'},
                                                                                                                                     'url': {'description': 'Image '
                                                                                                                                                            'URL.',
                                                                                                                                             'type': 'string'},
                                                                                                                                     'width': {'description': 'The '
                                                                                                                                                              'width, '
                                                                                                                                                              'in '
                                                                                                                                                              'pixels, '
                                                                                                                                                              'of '
                                                                                                                                                              'the '
                                                                                                                                                              'linked '
                                                                                                                                                              'resource.',
                                                                                                                                               'format': 'uint32',
                                                                                                                                               'type': 'integer'}},
                                                                                                                      'type': 'object'},
                                                                                                            'objectType': {'description': 'The type of media '
                                                                                                                                          'object. Possible '
                                                                                                                                          'values include, but '
                                                                                                                                          'are not limited to, '
                                                                                                                                          'the following '
                                                                                                                                          'values:  \n'
                                                                                                                                          '- "photo" - A '
                                                                                                                                          'photo. \n'
                                                                                                                                          '- "album" - A photo '
                                                                                                                                          'album. \n'
                                                                                                                                          '- "video" - A '
                                                                                                                                          'video. \n'
                                                                                                                                          '- "article" - An '
                                                                                                                                          'article, specified '
                                                                                                                                          'by a link.',
                                                                                                                           'type': 'string'},
                                                                                                            'thumbnails': {'description': 'If the attachment '
                                                                                                                                          'is an album, this '
                                                                                                                                          'property is a list '
                                                                                                                                          'of potential '
                                                                                                                                          'additional '
                                                                                                                                          'thumbnails from the '
                                                                                                                                          'album.',
                                                                                                                           'items': {'properties': {'description': {'description': 'Potential '
                                                                                                                                                                                   'name '
                                                                                                                                                                                   'of '
                                                                                                                                                                                   'the '
                                                                                                                                                                                   'thumbnail.',
                                                                                                                                                                    'type': 'string'},
                                                                                                                                                    'image': {'description': 'Image '
                                                                                                                                                                             'resource.',
                                                                                                                                                              'properties': {'height': {'description': 'The '
                                                                                                                                                                                                       'height, '
                                                                                                                                                                                                       'in '
                                                                                                                                                                                                       'pixels, '
                                                                                                                                                                                                       'of '
                                                                                                                                                                                                       'the '
                                                                                                                                                                                                       'linked '
                                                                                                                                                                                                       'resource.',
                                                                                                                                                                                        'format': 'uint32',
                                                                                                                                                                                        'type': 'integer'},
                                                                                                                                                                             'type': {'description': 'Media '
                                                                                                                                                                                                     'type '
                                                                                                                                                                                                     'of '
                                                                                                                                                                                                     'the '
                                                                                                                                                                                                     'link.',
                                                                                                                                                                                      'type': 'string'},
                                                                                                                                                                             'url': {'description': 'Image '
                                                                                                                                                                                                    'url.',
                                                                                                                                                                                     'type': 'string'},
                                                                                                                                                                             'width': {'description': 'The '
                                                                                                                                                                                                      'width, '
                                                                                                                                                                                                      'in '
                                                                                                                                                                                                      'pixels, '
                                                                                                                                                                                                      'of '
                                                                                                                                                                                                      'the '
                                                                                                                                                                                                      'linked '
                                                                                                                                                                                                      'resource.',
                                                                                                                                                                                       'format': 'uint32',
                                                                                                                                                                                       'type': 'integer'}},
                                                                                                                                                              'type': 'object'},
                                                                                                                                                    'url': {'description': 'URL '
                                                                                                                                                                           'of '
                                                                                                                                                                           'the '
                                                                                                                                                                           'webpage '
                                                                                                                                                                           'containing '
                                                                                                                                                                           'the '
                                                                                                                                                                           'image.',
                                                                                                                                                            'type': 'string'}},
                                                                                                                                     'type': 'object'},
                                                                                                                           'type': 'array'},
                                                                                                            'url': {'description': 'The link to the '
                                                                                                                                   'attachment, which should '
                                                                                                                                   'be of type text/html.',
                                                                                                                    'type': 'string'}},
                                                                                             'type': 'object'},
                                                                                   'type': 'array'},
                                                                   'content': {'description': 'The HTML-formatted content, which is suitable for display.',
                                                                               'type': 'string'},
                                                                   'id': {'description': 'The ID of the object. When resharing an activity, this is the ID of '
                                                                                         'the activity that is being reshared.',
                                                                          'type': 'string'},
                                                                   'objectType': {'description': 'The type of the object. Possible values include, but are not '
                                                                                                 'limited to, the following values:  \n'
                                                                                                 '- "note" - Textual content. \n'
                                                                                                 '- "activity" - A Google+ activity.',
                                                                                  'type': 'string'},
                                                                   'originalContent': {'description': 'The content (text) as provided by the author, which is '
                                                                                                      'stored without any HTML formatting. When creating or '
                                                                                                      'updating an activity, this value must be supplied as '
                                                                                                      'plain text in the request.',
                                                                                       'type': 'string'},
                                                                   'plusoners': {'description': "People who +1'd this activity.",
                                                                                 'properties': {'selfLink': {'description': 'The URL for the collection of '
                                                                                                                            "people who +1'd this activity.",
                                                                                                             'type': 'string'},
                                                                                                'totalItems': {'description': "Total number of people who +1'd "
                                                                                                                              'this activity.',
                                                                                                               'format': 'uint32',
                                                                                                               'type': 'integer'}},
                                                                                 'type': 'object'},
                                                                   'replies': {'description': 'Comments in reply to this activity.',
                                                                               'properties': {'selfLink': {'description': 'The URL for the collection of '
                                                                                                                          'comments in reply to this activity.',
                                                                                                           'type': 'string'},
                                                                                              'totalItems': {'description': 'Total number of comments on this '
                                                                                                                            'activity.',
                                                                                                             'format': 'uint32',
                                                                                                             'type': 'integer'}},
                                                                               'type': 'object'},
                                                                   'resharers': {'description': 'People who reshared this activity.',
                                                                                 'properties': {'selfLink': {'description': 'The URL for the collection of '
                                                                                                                            'resharers.',
                                                                                                             'type': 'string'},
                                                                                                'totalItems': {'description': 'Total number of people who '
                                                                                                                              'reshared this activity.',
                                                                                                               'format': 'uint32',
                                                                                                               'type': 'integer'}},
                                                                                 'type': 'object'},
                                                                   'url': {'description': 'The URL that points to the linked resource.', 'type': 'string'}},
                                                    'type': 'object'},
                                         'placeId': {'description': 'ID of the place where this activity occurred.', 'type': 'string'},
                                         'placeName': {'description': 'Name of the place where this activity occurred.', 'type': 'string'},
                                         'provider': {'description': 'The service provider that initially published this activity.',
                                                      'properties': {'title': {'description': 'Name of the service provider.', 'type': 'string'}},
                                                      'type': 'object'},
                                         'published': {'description': 'The time at which this activity was initially published. Formatted as an RFC 3339 '
                                                                      'timestamp.',
                                                       'format': 'date-time',
                                                       'type': 'string'},
                                         'radius': {'description': 'Radius, in meters, of the region where this activity occurred, centered at the latitude '
                                                                   'and longitude identified in geocode.',
                                                    'type': 'string'},
                                         'title': {'description': 'Title of this activity.', 'type': 'string'},
                                         'updated': {'description': 'The time at which this activity was last updated. Formatted as an RFC 3339 timestamp.',
                                                     'format': 'date-time',
                                                     'type': 'string'},
                                         'url': {'description': 'The link to this activity.', 'type': 'string'},
                                         'verb': {'description': "This activity's verb, which indicates the action that was performed. Possible values "
                                                                 'include, but are not limited to, the following values:  \n'
                                                                 '- "post" - Publish content to the stream. \n'
                                                                 '- "share" - Reshare an activity.',
                                                  'type': 'string'}},
                          'type': 'object'},
             'ActivityFeed': {'id': 'ActivityFeed',
                              'properties': {'etag': {'description': 'ETag of this response for caching purposes.', 'type': 'string'},
                                             'id': {'description': 'The ID of this collection of activities. Deprecated.', 'type': 'string'},
                                             'items': {'description': 'The activities in this page of results.',
                                                       'items': {'$ref': 'Activity'},
                                                       'type': 'array'},
                                             'kind': {'default': 'plus#activityFeed',
                                                      'description': 'Identifies this resource as a collection of activities. Value: "plus#activityFeed".',
                                                      'type': 'string'},
                                             'nextLink': {'description': 'Link to the next page of activities.', 'type': 'string'},
                                             'nextPageToken': {'description': 'The continuation token, which is used to page through large result sets. '
                                                                              'Provide this value in a subsequent request to return the next page of results.',
                                                               'type': 'string'},
                                             'selfLink': {'description': 'Link to this activity resource.', 'type': 'string'},
                                             'title': {'description': 'The title of this collection of activities, which is a truncated portion of the '
                                                                      'content.',
                                                       'type': 'string'},
                                             'updated': {'description': 'The time at which this collection of activities was last updated. Formatted as an RFC '
                                                                        '3339 timestamp.',
                                                         'format': 'date-time',
                                                         'type': 'string'}},
                              'type': 'object'},
             'Comment': {'id': 'Comment',
                         'properties': {'actor': {'description': 'The person who posted this comment.',
                                                  'properties': {'clientSpecificActorInfo': {'description': 'Actor info specific to particular clients.',
                                                                                             'properties': {'youtubeActorInfo': {'description': 'Actor info '
                                                                                                                                                'specific to '
                                                                                                                                                'YouTube '
                                                                                                                                                'clients.',
                                                                                                                                 'properties': {'channelId': {'description': 'ID '
                                                                                                                                                                             'of '
                                                                                                                                                                             'the '
                                                                                                                                                                             'YouTube '
                                                                                                                                                                             'channel '
                                                                                                                                                                             'owned '
                                                                                                                                                                             'by '
                                                                                                                                                                             'the '
                                                                                                                                                                             'Actor.',
                                                                                                                                                              'type': 'string'}},
                                                                                                                                 'type': 'object'}},
                                                                                             'type': 'object'},
                                                                 'displayName': {'description': 'The name of this actor, suitable for display.',
                                                                                 'type': 'string'},
                                                                 'id': {'description': 'The ID of the actor.', 'type': 'string'},
                                                                 'image': {'description': 'The image representation of this actor.',
                                                                           'properties': {'url': {'description': "The URL of the actor's profile photo. To "
                                                                                                                 'resize the image and crop it to a square, '
                                                                                                                 'append the query string ?sz=x, where x is '
                                                                                                                 'the dimension in pixels of each side.',
                                                                                                  'type': 'string'}},
                                                                           'type': 'object'},
                                                                 'url': {'description': 'A link to the Person resource for this actor.', 'type': 'string'},
                                                                 'verification': {'description': 'Verification status of actor.',
                                                                                  'properties': {'adHocVerified': {'description': 'Verification for one-time '
                                                                                                                                  'or manual processes.',
                                                                                                                   'type': 'string'}},
                                                                                  'type': 'object'}},
                                                  'type': 'object'},
                                        'etag': {'description': 'ETag of this response for caching purposes.', 'type': 'string'},
                                        'id': {'description': 'The ID of this comment.', 'type': 'string'},
                                        'inReplyTo': {'description': 'The activity this comment replied to.',
                                                      'items': {'properties': {'id': {'description': 'The ID of the activity.', 'type': 'string'},
                                                                               'url': {'description': 'The URL of the activity.', 'type': 'string'}},
                                                                'type': 'object'},
                                                      'type': 'array'},
                                        'kind': {'default': 'plus#comment',
                                                 'description': 'Identifies this resource as a comment. Value: "plus#comment".',
                                                 'type': 'string'},
                                        'object': {'description': 'The object of this comment.',
                                                   'properties': {'content': {'description': 'The HTML-formatted content, suitable for display.',
                                                                              'type': 'string'},
                                                                  'objectType': {'default': 'comment',
                                                                                 'description': 'The object type of this comment. Possible values are:  \n'
                                                                                                '- "comment" - A comment in reply to an activity.',
                                                                                 'type': 'string'},
                                                                  'originalContent': {'description': 'The content (text) as provided by the author, stored '
                                                                                                     'without any HTML formatting. When creating or updating a '
                                                                                                     'comment, this value must be supplied as plain text in '
                                                                                                     'the request.',
                                                                                      'type': 'string'}},
                                                   'type': 'object'},
                                        'plusoners': {'description': "People who +1'd this comment.",
                                                      'properties': {'totalItems': {'description': "Total number of people who +1'd this comment.",
                                                                                    'format': 'uint32',
                                                                                    'type': 'integer'}},
                                                      'type': 'object'},
                                        'published': {'description': 'The time at which this comment was initially published. Formatted as an RFC 3339 '
                                                                     'timestamp.',
                                                      'format': 'date-time',
                                                      'type': 'string'},
                                        'selfLink': {'description': 'Link to this comment resource.', 'type': 'string'},
                                        'updated': {'description': 'The time at which this comment was last updated. Formatted as an RFC 3339 timestamp.',
                                                    'format': 'date-time',
                                                    'type': 'string'},
                                        'verb': {'default': 'post',
                                                 'description': "This comment's verb, indicating what action was performed. Possible values are:  \n"
                                                                '- "post" - Publish content to the stream.',
                                                 'type': 'string'}},
                         'type': 'object'},
             'CommentFeed': {'id': 'CommentFeed',
                             'properties': {'etag': {'description': 'ETag of this response for caching purposes.', 'type': 'string'},
                                            'id': {'description': 'The ID of this collection of comments.', 'type': 'string'},
                                            'items': {'description': 'The comments in this page of results.', 'items': {'$ref': 'Comment'}, 'type': 'array'},
                                            'kind': {'default': 'plus#commentFeed',
                                                     'description': 'Identifies this resource as a collection of comments. Value: "plus#commentFeed".',
                                                     'type': 'string'},
                                            'nextLink': {'description': 'Link to the next page of activities.', 'type': 'string'},
                                            'nextPageToken': {'description': 'The continuation token, which is used to page through large result sets. Provide '
                                                                             'this value in a subsequent request to return the next page of results.',
                                                              'type': 'string'},
                                            'title': {'description': 'The title of this collection of comments.', 'type': 'string'},
                                            'updated': {'description': 'The time at which this collection of comments was last updated. Formatted as an RFC '
                                                                       '3339 timestamp.',
                                                        'format': 'date-time',
                                                        'type': 'string'}},
                             'type': 'object'},
             'PeopleFeed': {'id': 'PeopleFeed',
                            'properties': {'etag': {'description': 'ETag of this response for caching purposes.', 'type': 'string'},
                                           'items': {'description': 'The people in this page of results. Each item includes the id, displayName, image, and '
                                                                    'url for the person. To retrieve additional profile data, see the people.get method.',
                                                     'items': {'$ref': 'Person'},
                                                     'type': 'array'},
                                           'kind': {'default': 'plus#peopleFeed',
                                                    'description': 'Identifies this resource as a collection of people. Value: "plus#peopleFeed".',
                                                    'type': 'string'},
                                           'nextPageToken': {'description': 'The continuation token, which is used to page through large result sets. Provide '
                                                                            'this value in a subsequent request to return the next page of results.',
                                                             'type': 'string'},
                                           'selfLink': {'description': 'Link to this resource.', 'type': 'string'},
                                           'title': {'description': 'The title of this collection of people.', 'type': 'string'},
                                           'totalItems': {'description': 'The total number of people available in this list. The number of people in a '
                                                                         'response might be smaller due to paging. This might not be set for all collections.',
                                                          'format': 'int32',
                                                          'type': 'integer'}},
                            'type': 'object'},
             'Person': {'id': 'Person',
                        'properties': {'aboutMe': {'description': 'A short biography for this person.', 'type': 'string'},
                                       'ageRange': {'description': 'The age range of the person. Valid ranges are 17 or younger, 18 to 20, and 21 or older. '
                                                                   "Age is determined from the user's birthday using Western age reckoning.",
                                                    'properties': {'max': {'description': "The age range's upper bound, if any. Possible values include, but "
                                                                                          'are not limited to, the following:  \n'
                                                                                          '- "17" - for age 17 \n'
                                                                                          '- "20" - for age 20',
                                                                           'format': 'int32',
                                                                           'type': 'integer'},
                                                                   'min': {'description': "The age range's lower bound, if any. Possible values include, but "
                                                                                          'are not limited to, the following:  \n'
                                                                                          '- "21" - for age 21 \n'
                                                                                          '- "18" - for age 18',
                                                                           'format': 'int32',
                                                                           'type': 'integer'}},
                                                    'type': 'object'},
                                       'birthday': {'description': "The person's date of birth, represented as YYYY-MM-DD.", 'type': 'string'},
                                       'braggingRights': {'description': 'The "bragging rights" line of this person.', 'type': 'string'},
                                       'circledByCount': {'description': 'For followers who are visible, the number of people who have added this person or '
                                                                         'page to a circle.',
                                                          'format': 'int32',
                                                          'type': 'integer'},
                                       'cover': {'description': 'The cover photo content.',
                                                 'properties': {'coverInfo': {'description': 'Extra information about the cover photo.',
                                                                              'properties': {'leftImageOffset': {'description': 'The difference between the '
                                                                                                                                'left position of the cover '
                                                                                                                                'image and the actual '
                                                                                                                                'displayed cover image. Only '
                                                                                                                                'valid for banner layout.',
                                                                                                                 'format': 'int32',
                                                                                                                 'type': 'integer'},
                                                                                             'topImageOffset': {'description': 'The difference between the top '
                                                                                                                               'position of the cover image '
                                                                                                                               'and the actual displayed cover '
                                                                                                                               'image. Only valid for banner '
                                                                                                                               'layout.',
                                                                                                                'format': 'int32',
                                                                                                                'type': 'integer'}},
                                                                              'type': 'object'},
                                                                'coverPhoto': {'description': "The person's primary cover image.",
                                                                               'properties': {'height': {'description': 'The height of the image.',
                                                                                                         'format': 'int32',
                                                                                                         'type': 'integer'},
                                                                                              'url': {'description': 'The URL of the image.', 'type': 'string'},
                                                                                              'width': {'description': 'The width of the image.',
                                                                                                        'format': 'int32',
                                                                                                        'type': 'integer'}},
                                                                               'type': 'object'},
                                                                'layout': {'description': 'The layout of the cover art. Possible values include, but are not '
                                                                                          'limited to, the following values:  \n'
                                                                                          '- "banner" - One large image banner.',
                                                                           'type': 'string'}},
                                                 'type': 'object'},
                                       'currentLocation': {'description': '(this field is not currently used)', 'type': 'string'},
                                       'displayName': {'description': 'The name of this person, which is suitable for display.', 'type': 'string'},
                                       'domain': {'description': "The hosted domain name for the user's Google Apps account. For instance, example.com. The "
                                                                 'plus.profile.emails.read or email scope is needed to get this domain name.',
                                                  'type': 'string'},
                                       'emails': {'description': 'A list of email addresses that this person has, including their Google account email '
                                                                 'address, and the public verified email addresses on their Google+ profile. The '
                                                                 'plus.profile.emails.read scope is needed to retrieve these email addresses, or the email '
                                                                 'scope can be used to retrieve just the Google account email address.',
                                                  'items': {'properties': {'type': {'description': 'The type of address. Possible values include, but are not '
                                                                                                   'limited to, the following values:  \n'
                                                                                                   '- "account" - Google account email address. \n'
                                                                                                   '- "home" - Home email address. \n'
                                                                                                   '- "work" - Work email address. \n'
                                                                                                   '- "other" - Other.',
                                                                                    'type': 'string'},
                                                                           'value': {'description': 'The email address.', 'type': 'string'}},
                                                            'type': 'object'},
                                                  'type': 'array'},
                                       'etag': {'description': 'ETag of this response for caching purposes.', 'type': 'string'},
                                       'gender': {'description': "The person's gender. Possible values include, but are not limited to, the following "
                                                                 'values:  \n'
                                                                 '- "male" - Male gender. \n'
                                                                 '- "female" - Female gender. \n'
                                                                 '- "other" - Other.',
                                                  'type': 'string'},
                                       'id': {'description': 'The ID of this person.', 'type': 'string'},
                                       'image': {'description': "The representation of the person's profile photo.",
                                                 'properties': {'isDefault': {'description': "Whether the person's profile photo is the default one",
                                                                              'type': 'boolean'},
                                                                'url': {'description': "The URL of the person's profile photo. To resize the image and crop it "
                                                                                       'to a square, append the query string ?sz=x, where x is the dimension '
                                                                                       'in pixels of each side.',
                                                                        'type': 'string'}},
                                                 'type': 'object'},
                                       'isPlusUser': {'description': 'Whether this user has signed up for Google+.', 'type': 'boolean'},
                                       'kind': {'default': 'plus#person',
                                                'description': 'Identifies this resource as a person. Value: "plus#person".',
                                                'type': 'string'},
                                       'language': {'description': "The user's preferred language for rendering.", 'type': 'string'},
                                       'name': {'description': "An object representation of the individual components of a person's name.",
                                                'properties': {'familyName': {'description': 'The family name (last name) of this person.', 'type': 'string'},
                                                               'formatted': {'description': 'The full name of this person, including middle names, suffixes, '
                                                                                            'etc.',
                                                                             'type': 'string'},
                                                               'givenName': {'description': 'The given name (first name) of this person.', 'type': 'string'},
                                                               'honorificPrefix': {'description': 'The honorific prefixes (such as "Dr." or "Mrs.") for this '
                                                                                                  'person.',
                                                                                   'type': 'string'},
                                                               'honorificSuffix': {'description': 'The honorific suffixes (such as "Jr.") for this person.',
                                                                                   'type': 'string'},
                                                               'middleName': {'description': 'The middle name of this person.', 'type': 'string'}},
                                                'type': 'object'},
                                       'nickname': {'description': 'The nickname of this person.', 'type': 'string'},
                                       'objectType': {'description': 'Type of person within Google+. Possible values include, but are not limited to, the '
                                                                     'following values:  \n'
                                                                     '- "person" - represents an actual person. \n'
                                                                     '- "page" - represents a page.',
                                                      'type': 'string'},
                                       'occupation': {'description': 'The occupation of this person.', 'type': 'string'},
                                       'organizations': {'description': 'A list of current or past organizations with which this person is associated.',
                                                         'items': {'properties': {'department': {'description': 'The department within the organization. '
                                                                                                                'Deprecated.',
                                                                                                 'type': 'string'},
                                                                                  'description': {'description': "A short description of the person's role in "
                                                                                                                 'this organization. Deprecated.',
                                                                                                  'type': 'string'},
                                                                                  'endDate': {'description': 'The date that the person left this organization.',
                                                                                              'type': 'string'},
                                                                                  'location': {'description': 'The location of this organization. Deprecated.',
                                                                                               'type': 'string'},
                                                                                  'name': {'description': 'The name of the organization.', 'type': 'string'},
                                                                                  'primary': {'description': 'If "true", indicates this organization is the '
                                                                                                             "person's primary one, which is typically "
                                                                                                             'interpreted as the current one.',
                                                                                              'type': 'boolean'},
                                                                                  'startDate': {'description': 'The date that the person joined this '
                                                                                                               'organization.',
                                                                                                'type': 'string'},
                                                                                  'title': {'description': "The person's job title or role within the "
                                                                                                           'organization.',
                                                                                            'type': 'string'},
                                                                                  'type': {'description': 'The type of organization. Possible values include, '
                                                                                                          'but are not limited to, the following values:  \n'
                                                                                                          '- "work" - Work. \n'
                                                                                                          '- "school" - School.',
                                                                                           'type': 'string'}},
                                                                   'type': 'object'},
                                                         'type': 'array'},
                                       'placesLived': {'description': 'A list of places where this person has lived.',
                                                       'items': {'properties': {'primary': {'description': 'If "true", this place of residence is this '
                                                                                                           "person's primary residence.",
                                                                                            'type': 'boolean'},
                                                                                'value': {'description': 'A place where this person has lived. For example: '
                                                                                                         '"Seattle, WA", "Near Toronto".',
                                                                                          'type': 'string'}},
                                                                 'type': 'object'},
                                                       'type': 'array'},
                                       'plusOneCount': {'description': "If a Google+ Page, the number of people who have +1'd this page.",
                                                        'format': 'int32',
                                                        'type': 'integer'},
                                       'relationshipStatus': {'description': "The person's relationship status. Possible values include, but are not limited "
                                                                             'to, the following values:  \n'
                                                                             '- "single" - Person is single. \n'
                                                                             '- "in_a_relationship" - Person is in a relationship. \n'
                                                                             '- "engaged" - Person is engaged. \n'
                                                                             '- "married" - Person is married. \n'
                                                                             '- "its_complicated" - The relationship is complicated. \n'
                                                                             '- "open_relationship" - Person is in an open relationship. \n'
                                                                             '- "widowed" - Person is widowed. \n'
                                                                             '- "in_domestic_partnership" - Person is in a domestic partnership. \n'
                                                                             '- "in_civil_union" - Person is in a civil union.',
                                                              'type': 'string'},
                                       'skills': {'description': "The person's skills.", 'type': 'string'},
                                       'tagline': {'description': 'The brief description (tagline) of this person.', 'type': 'string'},
                                       'url': {'description': "The URL of this person's profile.", 'type': 'string'},
                                       'urls': {'description': 'A list of URLs for this person.',
                                                'items': {'properties': {'label': {'description': 'The label of the URL.', 'type': 'string'},
                                                                         'type': {'description': 'The type of URL. Possible values include, but are not '
                                                                                                 'limited to, the following values:  \n'
                                                                                                 '- "otherProfile" - URL for another profile. \n'
                                                                                                 '- "contributor" - URL to a site for which this person is a '
                                                                                                 'contributor. \n'
                                                                                                 '- "website" - URL for this Google+ Page\'s primary '
                                                                                                 'website. \n'
                                                                                                 '- "other" - Other URL.',
                                                                                  'type': 'string'},
                                                                         'value': {'description': 'The URL value.', 'type': 'string'}},
                                                          'type': 'object'},
                                                'type': 'array'},
                                       'verified': {'description': 'Whether the person or Google+ Page has been verified.', 'type': 'boolean'}},
                        'type': 'object'},
             'Place': {'id': 'Place',
                       'properties': {'address': {'description': 'The physical address of the place.',
                                                  'properties': {'formatted': {'description': 'The formatted address for display.', 'type': 'string'}},
                                                  'type': 'object'},
                                      'displayName': {'description': 'The display name of the place.', 'type': 'string'},
                                      'id': {'description': 'The id of the place.', 'type': 'string'},
                                      'kind': {'default': 'plus#place',
                                               'description': 'Identifies this resource as a place. Value: "plus#place".',
                                               'type': 'string'},
                                      'position': {'description': 'The position of the place.',
                                                   'properties': {'latitude': {'description': 'The latitude of this position.',
                                                                               'format': 'double',
                                                                               'type': 'number'},
                                                                  'longitude': {'description': 'The longitude of this position.',
                                                                                'format': 'double',
                                                                                'type': 'number'}},
                                                   'type': 'object'}},
                       'type': 'object'},
             'PlusAclentryResource': {'id': 'PlusAclentryResource',
                                      'properties': {'displayName': {'description': 'A descriptive name for this entry. Suitable for display.',
                                                                     'type': 'string'},
                                                     'id': {'description': 'The ID of the entry. For entries of type "person" or "circle", this is the ID of '
                                                                           'the resource. For other types, this property is not set.',
                                                            'type': 'string'},
                                                     'type': {'description': 'The type of entry describing to whom access is granted. Possible values are:  \n'
                                                                             '- "person" - Access to an individual. \n'
                                                                             '- "circle" - Access to members of a circle. \n'
                                                                             '- "myCircles" - Access to members of all the person\'s circles. \n'
                                                                             '- "extendedCircles" - Access to members of all the person\'s circles, plus all '
                                                                             'of the people in their circles. \n'
                                                                             '- "domain" - Access to members of the person\'s Google Apps domain. \n'
                                                                             '- "public" - Access to anyone on the web.',
                                                              'type': 'string'}},
                                      'type': 'object'}},
 'servicePath': 'plus/v1/',
 'title': 'Google+ API',
 'version': 'v1'}