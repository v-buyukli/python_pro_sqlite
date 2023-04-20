from faker import Faker


def generate_customers(number=10):
    faker = Faker()
    customers = [
        {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "email": faker.email()
        }
        for _ in range(number)
    ]
    return customers
