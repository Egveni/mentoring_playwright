import requests


from src.baseclasses.response import Response

from src.schemas.user import User


def test_getting_users_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validate(User)
    print(make_number)

# 'meta': 
# {'pagination': {
#     'total': 2800, 
#     'pages': 280, 
#     'page': 1, 
#     'limit': 10, 
#     'links': {
#         'previous': None, 
#         'current': 'https://gorest.co.in/public/v1/users?page=1', 
#         'next': 'https://gorest.co.in/public/v1/users?page=2'
#         }
#         }
#         }, 
# 'data': [
#     {
#         'id': 7996814, 
#         'name': 'Bhooshit Banerjee', 
#         'email': 'banerjee_bhooshit@oberbrunner.example', 
#         'gender': 'female', 
#         'status': 'active'}, 
#         {
#             'id': 7996813, 
#             'name': 'Amb. Anasuya Jha', 
#             'email': 'amb_jha_anasuya@corwin.example', 
#             'gender': 'male', 
#             'status': 'active'}, 
#             {'id': 7996812, 
#             'name': 'Gajaadhar Bhattathiri',
#              'email': 'bhattathiri_gajaadhar@watsica.example', 
#              'gender': 'female', 
#              'status': 'active'}, 
#              {'id': 7996811, 
#              'name': 'Kanaka Guneta', 
#              'email': 'guneta_kanaka@hoeger-bergstrom.test', 
#              'gender': 'male', 
#              'status': 'active'}, 
#              {'id': 7996810, 
#              'name': 'Acharyasuta Reddy', 
#              'email': 'reddy_acharyasuta@schumm.test', 
#              'gender': 'female', 
#              'status': 'active'}, 
#              {'id': 7996809, 
#              'name': 'Agneya Shah',
#               'email': 'agneya_shah@streich.example', 
#               'gender': 'female',
#                'status': 'active'}, 
#                {'id': 7996808, 
#                'name': 'Lalita Asan', 
#                'email': 'lalita_asan@bashirian.test', 
#                'gender': 'male', 
#                'status': 'active'},
#                 {'id': 7996807, 
#                 'name': 'Aditeya Kaul',
#                  'email': 'aditeya_kaul@heller.example', 
#                  'gender': 'male',
#                   'status': 'inactive'},
#                    {'id': 7996806, 
#                    'name': 'Dharitri Iyer',
#                     'email': 'dharitri_iyer@lueilwitz.example', 
#                     'gender': 'female', 
#                     'status': 'inactive'},
#                      {'id': 7996805, 
#                      'name': 'Ganapati Gowda', 
#                      'email': 'gowda_ganapati@murray.test', 
#                      'gender': 'female', 
#                      'status': 'inactive'}]}