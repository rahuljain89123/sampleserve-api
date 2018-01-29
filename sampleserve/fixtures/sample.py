import datetime

sample = [
    (3, {'import_id': None, 'date_collected': '2007-05-01', 'date_analyzed': '2007-05-01', 'date_extracted': '2007-05-01', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 1, 'schedule_id': None, 'active': True, 'id': 3}),
    (4, {'import_id': None, 'date_collected': '2007-07-18', 'date_analyzed': '2007-07-18', 'date_extracted': '2007-07-18', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 1, 'schedule_id': None, 'active': True, 'id': 4}),
    (5, {'import_id': None, 'date_collected': '2007-11-21', 'date_analyzed': '2007-11-21', 'date_extracted': '2007-11-21', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 1, 'schedule_id': None, 'active': True, 'id': 5}),
    (6, {'import_id': None, 'date_collected': '2008-03-10', 'date_analyzed': '2008-03-10', 'date_extracted': '2008-03-10', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 1, 'schedule_id': None, 'active': True, 'id': 6}),
    (7, {'import_id': None, 'date_collected': '2008-06-13', 'date_analyzed': '2008-06-13', 'date_extracted': '2008-06-13', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 1, 'schedule_id': None, 'active': True, 'id': 7}),
    (8, {'import_id': None, 'date_collected': '2007-05-01', 'date_analyzed': '2007-05-01', 'date_extracted': '2007-05-01', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 2, 'schedule_id': None, 'active': True, 'id': 8}),
    (9, {'import_id': None, 'date_collected': '2007-07-18', 'date_analyzed': '2007-07-18', 'date_extracted': '2007-07-18', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 2, 'schedule_id': None, 'active': True, 'id': 9}),
    (10, {'import_id': None, 'date_collected': '2007-11-21', 'date_analyzed': '2007-11-21', 'date_extracted': '2007-11-21', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 2, 'schedule_id': None, 'active': True, 'id': 10}),
    (11, {'import_id': None, 'date_collected': '2008-03-10', 'date_analyzed': '2008-03-10', 'date_extracted': '2008-03-10', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 2, 'schedule_id': None, 'active': True, 'id': 11}),
    (12, {'import_id': None, 'date_collected': '2008-06-13', 'date_analyzed': '2008-06-13', 'date_extracted': '2008-06-13', 'paid_level_1': False, 'paid_level_2': False, 'site_id': 2, 'schedule_id': None, 'active': True, 'id': 12}),
    (1287, {'import_id': None, 'date_collected': '2013-01-17', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 79, 'schedule_id': 19753, 'active': True, 'id': 1287}),
    (1288, {'import_id': 48, 'date_collected': '2012-12-12', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 57, 'schedule_id': None, 'active': False, 'id': 1288}),
    (1289, {'import_id': 51, 'date_collected': '2013-01-08', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 49, 'schedule_id': None, 'active': False, 'id': 1289}),
    (1290, {'import_id': 53, 'date_collected': '2013-01-11', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 74, 'schedule_id': None, 'active': True, 'id': 1290}),
    (1291, {'import_id': None, 'date_collected': '2013-02-06', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 8, 'schedule_id': 19762, 'active': True, 'id': 1291}),
    (1292, {'import_id': None, 'date_collected': '2013-02-11', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 35, 'schedule_id': 19772, 'active': True, 'id': 1292}),
    (1293, {'import_id': None, 'date_collected': '2013-02-13', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 18, 'schedule_id': 19769, 'active': True, 'id': 1293}),
    (1294, {'import_id': None, 'date_collected': '2013-02-21', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 11, 'schedule_id': 19768, 'active': True, 'id': 1294}),
    (1295, {'import_id': 58, 'date_collected': '2013-02-12', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 35, 'schedule_id': None, 'active': False, 'id': 1295}),
    (1296, {'import_id': None, 'date_collected': '2013-03-18', 'date_analyzed': None, 'date_extracted': None, 'paid_level_1': False, 'paid_level_2': False, 'site_id': 14, 'schedule_id': 19825, 'active': True, 'id': 1296}),
]
