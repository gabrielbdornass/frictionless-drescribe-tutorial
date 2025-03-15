from frictionless import Schema, describe

resource = describe('country-2.csv')
resource.dialect.header_rows = [2]
resource.dialect.get_control('csv').delimiter = ';'
resource.schema = 'country.schema.yaml'
resource.to_yaml('country.resource-cleaned.yaml')
