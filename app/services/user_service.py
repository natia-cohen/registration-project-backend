from app.database import users_collection
from bson import ObjectId


def create_user(user):
    user_dict = user.dict()
    result = users_collection.insert_one(user_dict)
    return str(result.inserted_id)


def get_users():
    return [
        {"id": str(user["_id"]), "email": user["email"]}
        for user in users_collection.find()
    ]


def update_user(user_id, user):
    result = users_collection.update_one(
        {"_id": ObjectId(user_id)}, {"$set": user.dict()}
    )
    return result.matched_count > 0


def delete_user(user_id):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count > 0

def get_user_by_email(email, password=None):
    query = {"email": email}
    if password:
        query["password"] = password
    return users_collection.find_one(query)


# from app.database import users_collection
# from bson import ObjectId

# def create_user(user):
#     user_dict = user.dict()
#     result = users_collection.insert_one(user_dict)
#     return str(result.inserted_id)

# def get_users():
#     return [
#         {"id": str(user["_id"]), "username": user["username"], "email": user["email"]}
#         for user in users_collection.find()
#     ]

# def update_user(user_id, user):
#     result = users_collection.update_one(
#         {"_id": ObjectId(user_id)}, {"$set": user.dict()}
#     )
#     return result.matched_count > 0

# def delete_user(user_id):
#     result = users_collection.delete_one({"_id": ObjectId(user_id)})
#     return result.deleted_count > 0
