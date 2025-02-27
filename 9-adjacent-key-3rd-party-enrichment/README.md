# We want to parse through some claim data to determine if the provider is likely able to treat diabetes. The claim data is stored in a dictionary which we need to parse to find relevant information. We often need to pull supporting information from the claim data as well, so let's make a general purpose function to help to find the adjacent key's value.

Based on the value of a specified key, we want to be able to extract the adjacent key's value. For instance - I want to find the value of “url” where the step's value is “exit”. 

```
{
    'a': {
        'step': 'authorize',
        'url': 'https://example.com/authorize'
    },
    'b': {
        'step': 'enter',
        'url': 'https://example.com/enter'
    },
    'c': [
        {
            'step': 'exit',
            'url': 'https://example.com/exit'
        },
        {
            'step': 'other',
            'url': 'https://example.com/other'
        }
    ]    
}
```

Once we have the general purpose function, we can use it to extract the information we need from the claim data. In this case, we want to find the NPI number so that we can query the specialty taxonomy from NPI Registry. Once we have the NPI, implement `get_treatment_ability` to leverage the `_predict_can_treat_diabetes` and return a dictionary with the following keys:

- `can_treat_diabetes`: boolean
- `provider_name`: string




# Goal

Implement the provided method so all unit test pass

See [root readme](../../README.md) to install python

# Running tests
From the `interviews` directory
```
cd ./9-adjacent-key-3rd-party-enrichment/python
python -m unittest tests.methods
```
