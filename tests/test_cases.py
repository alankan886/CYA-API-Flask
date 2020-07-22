attr_names = "id, username, password, boards"

users_info = [
    (1, "testusername1", "testpassword1", [(1, "testboard1")]),
    (2, "testusername2", "testpassword2", [(2, "testboard2")]),
    (3, "abc", "123", [(3, "abcboard")])
]

invalid_users_info = [
    (900, "testusername1", "wrongpassword1", [(1, "wrongboard1")]),
    (901, "wrongusername2", "testpassword2", [(2, "wrongboard2")]),
    (902, "321", "xyz", [(3, "xyzboard")])
]

# The post register is tested with different data. Due to existing data already exists in database from init_database, 
# inserting identitcal data will cause error.
# user id can duplicate because it's auto-incremented in db.
user_post_register_test_info = [
    (1, "testusername10", "testpassword10", [(1, "testboard10")]),
    (2, "testusername20", "testpassword20", [(2, "testboard20")]),
    (3, "xyz", "123", [(3, "xyzboard")])
]

board_post_board_by_id_test_info = [
    (1, "testusername1", "testpassword1", [(4, "testboard100")]),
    (2, "testusername2", "testpassword2", [(5, "testboard200")]),
    (3, "abc", "123", [(6, "abcboard300")])
]
