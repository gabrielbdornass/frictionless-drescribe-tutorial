from frictionless import Schema

schema = Schema.describe('./data-raw/country-1.csv')
schema.get_field('id').title = 'Identifier'
schema.get_field('neighbor_id').title = 'Identifier of the neighbor'
schema.get_field('name').title = 'Name of the country'
schema.get_field('population').title = 'Population'
schema.get_field('population').description = "According to the year 2020's data"
schema.get_field('population').constraints['minimum'] = 0
schema.foreign_keys.append(
    {'fields': ['neighbor_id'], 'reference': {'resource': '', 'fields': ['id']}}
)
schema.to_yaml('schemas/country.schema-full.yaml')
