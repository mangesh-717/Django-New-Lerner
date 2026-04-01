# import uuid
# def save():
       
#     account_number = uuid.uuid4()
#     for i in range(10):
#         print(account_number[i])
# save()
        # Ensure the generated account number is unique
        # while Account.objects.filter(account_number=self.account_number).exists():
        #     self.account_number = uuid.uuid4()

        # super().save(*args, **kwargs)

import uuid

def save():
    account_number = uuid.uuid4()

    # Accessing individual components
    print("UUID as a string:", str(account_number))
    print("UUID as bytes:", account_number.bytes)
    print("UUID as an int:", account_number.int)

    # Accessing the individual bytes of the UUID
    for byte in account_number.bytes:
        print(byte)

save()
