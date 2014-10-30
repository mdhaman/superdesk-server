Feature: Category Resource

    @auth
    Scenario: List empty categories
        Given empty "categories"
        When we get "/categories"
        Then we get list with 0 items

    @auth
    Scenario: Create a new category
        When we post to "categories"
            """
            {"name": "National", "code": "A"}
            """
        Then we get response code 201

    @auth
    Scenario: Test category code validation
        When we post to "categories"
            """
            {"name": "National", "code": "A"}
            """
        Then we get response code 201
        When we post to "categories"
            """
            {"name": "Nationaltest", "code": "A"}
            """
        Then we get response code 400
            """
            {"_status": "ERR", "_issues": {"code": {"unique": 1}}}
            """
        When we post to "categories"
            """
            {"name": "Nationaltest", "code": "3"}
            """
        Then we get response code 400
            """
            {"_status": "ERR", "_issues": {"code": "value does not match regex '^[a-zA-Z]{1}$'"}}
            """
        When we post to "categories"
            """
            {"name": "Nationaltest", "code": ""}
            """
        Then we get response code 400
            """
            {"_status": "ERR", "_issues": {"code": "value does not match regex '^[a-zA-Z]{1}$'"}}
            """
        When we post to "categories"
            """
            {"name": "Nationaltest", "code": "#"}
            """
        Then we get response code 400
            """
            {"_status": "ERR", "_issues": {"code": "value does not match regex '^[a-zA-Z]{1}$'"}}
            """

    @auth
    Scenario: Test category name validation
        When we post to "categories"
            """
            {"name": "National", "code": "A"}
            """
        Then we get response code 201
        When we post to "categories"
            """
            {"name": "National", "code": "E"}
            """
        Then we get response code 400
            """
            {"_status": "ERR", "_issues": {"name": {"unique": 1}}}
            """
        When we post to "categories"
            """
            {"name": "", "code": "E"}
            """
        Then we get response code 400
            """
            {"_status": "ERR", "_issues": {"name": {"minlength": 1}}}
            """