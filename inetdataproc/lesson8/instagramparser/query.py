from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    mongo_base = client.instagram_users
    users = mongo_base['users']
    follow = mongo_base['follow']

    user_name = 'data_science_beginners'
    user = users.find_one({'name': user_name})

    print('FOLLOWERS')
    followers = follow.find({'follow_type': 'follower', 'user_id': user['user_id']})
    for one in followers:
        print(users.find_one({'user_id': one['follow_id']}, {'name': True, '_id': False}))

    print('FOLLOWING')
    following = follow.find({'follow_type': 'following', 'user_id': user['user_id']})
    for one in following:
        print(users.find_one({'user_id': one['follow_id']}, {'name': True, '_id': False}))
