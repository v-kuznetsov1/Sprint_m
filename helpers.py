from faker import Faker
   
def generate_user_data():
        
    faker = Faker()
    user_data = {
        "email": faker.email(),
        "password": faker.password()
        }
        
    return user_data
        