import re
import rstr
from copy import deepcopy

JOURNAL_LIKE_BIBJSON = {
    "alternative_title": "Alternative Title",
    "apc": {
        "max": [
            {"currency": "GBP", "price": 2}
        ],
        "url": "http://apc.com",
        "has_apc": True
    },
    "article": {
        "license_display": ["Embed"],
        "license_display_example_url": "http://licence.embedded",
        "orcid": True,
        "i4oc_open_citations": False
    },
    "boai": True,
    "copyright": {
        "author_retains": True,
        "url": "http://copyright.com"
    },
    "deposit_policy": {
        "has_policy" : True,
        "service": ["Sherpa/Romeo", "Store it"],
        "url": "http://deposit.policy"
    },
    "discontinued_date": "2001-01-01",
    "editorial": {
        "review_process": ["Open peer review", "some bloke checks it out"],
        "review_url": "http://review.process",
        "board_url": "http://editorial.board"
    },
    "eissn": "9876-5432",
    "is_replaced_by": ["2222-2222"],
    "institution": {
        "name": "Society Institution",
        "country": "US"
    },
    "keywords": ["word", "key"],
    "language": ["EN", "FR"],
    "license": [
        {
            "type": "Publisher's own license",
            "BY": True,
            "NC": True,
            "ND": False,
            "SA": False,
            "url": "http://licence.url"
        }
    ],
    "other_charges": {
        "has_other_charges" : True,
        "url": "http://other.charges"
    },
    "pid_scheme": {
        "has_pid_scheme" : True,
        "scheme": ["DOI", "ARK", "PURL", "PIDMachine"],
    },
    "pissn": "1234-5678",
    "plagiarism": {
        "detection": True,
        "url": "http://plagiarism.screening"
    },
    "preservation": {
        "has_preservation" : True,
        "service": ["LOCKSS", "CLOCKSS", "A safe place"],
        "national_library": ["Trinity", "Imperial"],
        "url": "http://digital.archiving.policy"
    },
    "publication_time_weeks": 8,
    "publisher": {
        "name": "The Publisher",
        "country": "US"
    },
    "ref": {
        "oa_statement": "http://oa.statement",
        "journal": "http://journal.url",
        "aims_scope": "http://aims.scope",
        "author_instructions": "http://author.instructions.com",
        "license_terms": "http://licence.url"
    },
    "replaces": ["1111-1111"],
    "subject": [
        {"scheme": "LCC", "term": "Economic theory. Demography",
         "code": "HB1-3840"},
        {"scheme": "LCC", "term": "Social Sciences", "code": "H"}
    ],
    "title": "The Title",
    "waiver": {
        "has_waiver" : True,
        "url": "http://waiver.policy"
    }
}

JOURNAL_SOURCE = {
    "id": "abcdefghijk_journal",
    "created_date": "2000-01-01T00:00:00Z",
    "last_manual_update": "2001-01-01T00:00:00Z",
    "last_updated": "2002-01-01T00:00:00Z",
    "admin": {
        "bulk_upload": "bulk_1234567890",
        "current_application": "qwertyuiop",
        "editor_group": "editorgroup",
        "editor": "associate",
        "in_doaj": False,
        "notes" : [
            {"note" : "Second Note", "date" : "2014-05-22T00:00:00Z", "id" : "1234"},
            {"note": "First Note", "date": "2014-05-21T14:02:45Z", "id" : "abcd"}
        ],
        "owner": "publisher",
        "related_applications": [
            {"application_id": "asdfghjkl", "date_accepted": "2018-01-01T00:00:00Z"},
            {"application_id": "zxcvbnm"}
        ],
        "seal": False,
        "ticked": True
    },
    "bibjson": JOURNAL_LIKE_BIBJSON
}

ISSN = r'^\d{4}-\d{3}(\d|X|x){1}$'
ISSN_COMPILED = re.compile(ISSN)

def make_many_journal_sources(count=2, in_doaj=False):
    journal_sources = []
    for i in range(0, count):
        template = deepcopy(JOURNAL_SOURCE)
        template['id'] = 'journalid{0}'.format(i)
        # now some very quick and very dirty date generation
        fakemonth = i
        if fakemonth < 1:
            fakemonth = 1
        if fakemonth > 9:
            fakemonth = 9
        template['created_date'] = "2000-0{fakemonth}-01T00:00:00Z".format(fakemonth=fakemonth)
        template["bibjson"]["pissn"] = rstr.xeger(ISSN_COMPILED)
        template["bibjson"]["eissn"] = rstr.xeger(ISSN_COMPILED)
        template['admin']['in_doaj'] = in_doaj
        template['bibjson']['title'] = 'Test Title {}'.format(i)
        journal_sources.append(deepcopy(template))
    return journal_sources