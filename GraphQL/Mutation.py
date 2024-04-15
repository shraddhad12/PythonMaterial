from graphene import ObjectType, InputObjectType, Schema, String, Int, Field, Mutation

class PersonInput(InputObjectType):
    name = String(required=True)
    age = Int(required=True)


class Person(ObjectType):
    name = String()
    age = Int()

class CreatePerson(Mutation):
    class Arguments:
        person_data = PersonInput(required=True)

    person = Field(Person)

    def mutate(root, info, person_data=None):
        person = Person(
            name=person_data.name,
            age=person_data.age
        )
        return person
    
# ... the Mutation Class


class MyMutations(ObjectType):
    create_person = CreatePerson.Field()

# We must define a query for our schema
class Query(ObjectType):
    person = Field(Person)
    def resolve_person(root, info, name):
        return f'Hello {name}!'

schema = Schema(query=Query, mutation=MyMutations)

mutation = '''
    mutation {
        createPerson(name:"Peter", age:22) {
            name
            age
        }
    }
'''
schema.execute(mutation)

query = '''
    query {
        Person{
            name
        }
    }
'''
result = schema.execute(mutation)
print(result.data)

result = schema.execute(query)
print(result.data)