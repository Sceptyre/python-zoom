import json
import os

# Prep
os.makedirs('out', exist_ok=True)

spec = None

module_template = \
"""from ..base import _BaseAPI

class {module_name}(_BaseAPI):
    def list_{module_name}(self):
        res = self.request('GET', f'phone/{module_name}', params)

        return res.json()
    def create_{module_name_singular}(self): 
        res = self.request('GET', f'phone/{module_name}', params)

        return res.json()
    def get_{module_name_singular}(self, {module_name_singular}_id): 
        res = self.request('GET', f'phone/{module_name}/{{{module_name_singular}_id}}', params)

        return res.json()
    def update_{module_name_singular}(self, {module_name_singular}_id): 
        res = self.request('GET', f'phone/{module_name}/{{{module_name_singular}_id}}', params)

        return res.json()
    def delete_{module_name_singular}(self, {module_name_singular}_id): 
        res = self.request('GET', f'phone/{module_name}/{{{module_name_singular}_id}}', params)

        return res.json()
"""

with open('ZoomPhoneAPISpec.json', 'r', encoding='utf8') as f:
    spec = json.loads(f.read())

def module_from_spec_path_definition(spec_path: str, spec_path_definition: dict) -> str:
    module_name = "".join([i.title() for i in spec_path.split('/')[2].split('_')])

    class_template = f"""from ..base import _BaseAPI

class {module_name}API(_BaseAPI):
    """

    method_map = dict(
        get     = 'get',
        post    = 'create',
        put     = 'update',
        patch   = 'update',
        delete  = 'delete'
    )

    for method, action in spec_path_definition.items():
        path_variables = []
        for parameter in action.get('parameters', []):
            if parameter['in'] == 'path': path_variables.append(parameter['name'])
            
        print(action)

        description = action['description'].replace('\n', '\n\t\t\t')

        class_template += \
        f"""def {method_map[method]}_{spec_path.split('/')[2]}(self {', ' + ', '.join(path_variables) if action.get('parameters') else ''}):
        \"\"\"
            {description}
        \"\"\"

        # TBD
        return

        res = self.request(
            '{method.upper()}',
            f'{spec_path}'
        )

        return res.json()
        
        """

    return class_template

for k,v in spec['paths'].items():
    with open(f"out/{k.split('/')[2]}.py", 'w+') as f:
        f.write(module_from_spec_path_definition(k,v))