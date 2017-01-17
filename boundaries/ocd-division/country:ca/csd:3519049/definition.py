from datetime import date

import boundaries

boundaries.register('King wards',
    file='King.shp',
    domain='King, ON',
    last_updated=date(2016, 11, 23),
    name_func=lambda f: 'Ward %s' % f.get('WARD_NUMBE'),
    id_func=boundaries.attr('WARD_NUMBE'),
    authority='Township of King',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3519049'},
    ogr2ogr='''-where "WARD_NUMBE<>0"''',
    base_file='ward.shp',
)