from typing import Union, List, Dict, Any, Optional


CLAIM_DICT = {
            'authentication': {
                'field': 'auth_url',
                'value': 'https://example.com/authorize'
            },
            'provider': {
                'field': 'npi',
                'value': '1326405838'
            },
            'claim': [
                {
                    'field': 'paid_date',
                    'value': '2024-01-01'
                },
                {
                    'field': 'source_url',
                    'value': 'https://example.com/other'
                }
            ]    
        }

def get_adjacent_key(
    in_obj: Union[Dict[str, Any], List[Any]],
    search_key: str,
    search_values: Union[str, List[str]],
    return_key: str
) -> Optional[Union[str, int, Dict[str, Any]]]:    
    #------------------------------------
    # implement me
    #------------------------------------
    return None

def _predict_can_treat_diabetes(taxonomy_code: str) -> bool:
    if taxonomy_code == '152W00000X':
        return False
    return False


def get_taxonomy_code(npi: str) -> str:
    # https://npiregistry.cms.hhs.gov/api/?version=2.1&number={NPI}
    #------------------------------------
    # implement me
    #------------------------------------
    pass

def get_treatment_ability() -> Dict[str, Any]:
    
    npi = get_adjacent_key(CLAIM_DICT, 'field', 'npi', 'value')
    #------------------------------------
    # implement me
    #------------------------------------
    return